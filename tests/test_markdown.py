import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import build
import markdown_catalog as md

class MarkdownTests(unittest.TestCase):
    def test_complete_catalog_and_links(self):
        snapshot,rows=build.load()
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            md.write_catalog(root,snapshot,rows,build.CATEGORIES)
            all_text=(root/'catalog/all.md').read_text()
            for row in rows:
                self.assertEqual(all_text.count('**['+row['name']+']'),1)
            pages=list((root/'catalog').glob('*.md'))
            self.assertEqual(len(pages),12)
            home=(root/'README.md').read_text()
            self.assertLess(len(home.splitlines()),120)
            self.assertNotIn('| ---',home)
            for page in [root/'README.md',*pages]:
                for target in re.findall(r'\]\(([^)]+)\)',page.read_text()):
                    if target.startswith(('http','#')):continue
                    if target.startswith(('docs/','data/')) or target=='index.html':continue
                    self.assertTrue((page.parent/target).exists(),target)
            before={p.relative_to(root):p.read_bytes() for p in [root/'README.md',*pages]}
            md.write_catalog(root,snapshot,rows,build.CATEGORIES)
            self.assertEqual(before,{p:p2.read_bytes() for p,p2 in [(p,root/p) for p in before]})

    def test_pending_populates_then_clears(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            row=dict(name='owner/new',url='https://github.com/owner/new',summary='待审核',category='待分类',subcategory='待复核',tags=[],status='未归档',note='待复核',starred_at='2026-10-31')
            snapshot={'fetched_at':'2026-10-31'}
            md.write_catalog(root,snapshot,[row],build.CATEGORIES+['待分类'])
            self.assertIn('owner/new',(root/'catalog/pending.md').read_text())
            md.write_catalog(root,snapshot,[],build.CATEGORIES)
            self.assertNotIn('owner/new',(root/'catalog/pending.md').read_text())

    def test_untrusted_summary_is_escaped(self):
        escaped=md.text('<script>*[bad]*</script>')
        self.assertNotIn('<script>',escaped)
        self.assertIn(chr(92)+'*',escaped)

if __name__=='__main__':unittest.main()
