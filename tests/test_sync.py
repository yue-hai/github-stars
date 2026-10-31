import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import sync
import build

def item(i, name=None):
    name = name or f'owner/repo{i}'
    return {'starred_at':'2026-10-31T00:00:00Z','repo':{'id':i,'full_name':name,'html_url':'https://github.com/'+name,'private':False,'stargazers_count':1,'description':'test','language':'Python','archived':False}}

def response(data):
    return io.StringIO(json.dumps(data))

class SyncTests(unittest.TestCase):
    def test_pagination_exact_hundred(self):
        calls=[]
        def opener(req, **kwargs):
            calls.append(req.full_url)
            return response([item(i) for i in range(100)] if len(calls)==1 else [])
        self.assertEqual(len(sync.fetch(opener)),100)
        self.assertIn('page=2',calls[-1])

    def test_bad_response_duplicate_private(self):
        private=item(1)
        private['repo']['private']=True
        for data in [{'message':'rate limited'},[item(1),item(1)],[private]]:
            with self.assertRaises(ValueError): sync.fetch(lambda *a,**k: response(data))

    def test_no_change(self):
        self.assertFalse(sync.plan({'items':[item(1),item(2)]},[item(2),item(1)])[0])

    def test_add_remove_rename(self):
        old={'items':[item(i) for i in range(10)]}
        new=[item(i) for i in range(1,11)]
        new[0]['repo']['full_name']='new/renamed'
        changed,events=sync.plan(old,new)
        self.assertTrue(changed)
        self.assertEqual({x['type'] for x in events},{'added','no_longer_publicly_visible','renamed'})

    def test_suspicious_drop(self):
        old={'items':[item(i) for i in range(100)]}
        for new in [[],[item(1)]]:
            with self.assertRaises(ValueError): sync.plan(old,new)
        self.assertTrue(sync.plan(old,[],True)[0])

    def test_failure_preserves_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'data').mkdir()
            p=root/'data/stars.json'
            original=json.dumps({'items':[item(1)]})
            p.write_text(original)
            with patch.object(sync,'ROOT',root),patch.object(sys,'argv',['sync.py']):
                with patch.object(sync,'fetch',side_effect=RuntimeError('network')):
                    with self.assertRaises(RuntimeError): sync.main()
                with patch.object(sync,'fetch',side_effect=[[item(1)],[item(2)]]):
                    with self.assertRaises(ValueError): sync.main()
            self.assertEqual(p.read_text(),original)
            self.assertEqual(len(list((root/'data').iterdir())),1)

    def test_atomic_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'test.json'
            sync.atomic_json(p,{'中文':'ok'})
            self.assertEqual(json.loads(p.read_text()),{'中文':'ok'})

    def test_rename_preserves_curation_new_pending(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/'data').mkdir()
            (root/'data/stars.json').write_text(json.dumps({'items':[item(1,'new/name'),item(2)]}))
            (root/'data/identities.json').write_text(json.dumps({'1':['old/name','new/name']}))
            (root/'data/curation.tsv').write_text(chr(9).join(['old/name','AI 与智能助手','测试','保留用途','AI','保留备注'])+chr(10))
            with patch.object(build,'ROOT',root): _,rows=build.load()
            self.assertEqual(rows[0]['summary'],'保留用途')
            self.assertEqual(rows[0]['note'],'保留备注')
            self.assertEqual(rows[1]['category'],'待分类')

if __name__=='__main__': unittest.main()
