#!/usr/bin/env python3
from pathlib import Path
import re,subprocess,sys
root=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]
required=['SKILL.md','README.md','CHANGELOG.md','AGENT_DISCOVERY.md','agent-manifest.json','docs/WORKFLOW_PLAYBOOK.md','docs/MODEL_COMPATIBILITY.md','integrations/tool-spec.json','integrations/mcp_server.py','integrations/adapters.py','integrations/README.md','scripts/forge.py','scripts/model_adapters.py','scripts/common.py','scripts/extract_dual_ocr.py','scripts/reasoning_team_correct.py','scripts/reasoning_team_enrich.py','scripts/verify_flashcards.py','scripts/build_selfcontained_html.py','scripts/fidelity_audit.py','scripts/qa_gates.py','scripts/verify_zip.py','templates/guide.css','templates/app.js','templates/build_manifest.json','templates/providers.example.json']
missing=[x for x in required if not (root/x).is_file()]
if missing:raise SystemExit('FAIL missing: '+', '.join(missing))
skill=(root/'SKILL.md').read_text('utf8')
for token in ['name: persian-pdf-studyguide-forge','version: 1.5.1','categories:','topics:','requires:','emoji:','model_agnostic: true']:
 if token not in skill:raise SystemExit('FAIL frontmatter token: '+token)
r=subprocess.run([sys.executable,str(root/'scripts/self_test.py')]);raise SystemExit(r.returncode)
