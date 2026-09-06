#!/usr/bin/env bash
# selftest.sh — offline regression suite for agent-bom-compliance v2.0.1.
# 34 checks. Builds a synthetic project fixture in a temp dir; secrets are
# SYNTHESIZED from fragments at runtime so this file contains no real-format
# secrets (publish scanners must not flag it). No network, no sudo.
#
# NOTE — ORDER-DEPENDENT BY DESIGN: all checks run against ONE fixture project
# and ONE audit ledger that phases A (dirty) → B (remediated) → C (regressed)
# mutate in sequence. Entry-count assertions (len==2, len==4) assume the
# preceding report calls happened exactly as written; if you insert a check
# that calls `report`, update the counts below to match.
cd "$(dirname "$0")/.." || exit 1
P=0; F=0
SBX="$(mktemp -d /tmp/agent-bom-selftest.XXXXXX)" || exit 1
trap 'rm -rf "$SBX"' EXIT
export SBX
PROJ="$SBX/proj"; mkdir -p "$PROJ"
export AGENT_BOM_AUDIT="$PROJ/.agent_bom_audit.jsonl"
chk(){ if eval "$2" >/dev/null 2>&1; then echo "PASS $1"; P=$((P+1)); else echo "FAIL $1"; F=$((F+1)); fi; }

# ── phase A fixture: manifests + SKILL.md (empty egress) + app.js ──────────
# app.js carries a synthesized secret + a hostname URL + an IP-literal URL;
# go.mod has a replace directive; pyproject has PEP-621 array deps; no LICENSE.
python3 - "$PROJ" <<'PYFIX'
import json, os, sys
p = sys.argv[1]
open(os.path.join(p, "package.json"), "w").write(json.dumps({
  "name": "demo-app", "version": "1.2.3",
  "dependencies": {"lodash": "^4.17.21", "express": "4.18.2"},
  "devDependencies": {"jest": "*"}}))
open(os.path.join(p, "package-lock.json"), "w").write(json.dumps({
  "name": "demo-app", "version": "1.2.3", "lockfileVersion": 3,
  "packages": {"node_modules/lodash": {"version": "4.17.21"},
               "node_modules/express": {"version": "4.18.2"},
               "node_modules/jest": {"version": "29.7.0"}}}))
open(os.path.join(p, "requirements.txt"), "w").write(
  "flask==2.3.3\nrequests\nnumpy>=1.24\nurllib3==1.26.2 ; python_version < \"3.8\"\n")
open(os.path.join(p, "pyproject.toml"), "w").write(
  "[project]\nname = \"demo-app\"\nversion = \"1.2.3\"\ndependencies = [\n"
  "  \"tomli==2.0.1\",\n  \"flask==2.3.3\",\n  \"zope.interface>=6.0\",\n]\n")
open(os.path.join(p, "go.mod"), "w").write(
  "module example.com/demo\n\ngo 1.21\n\nrequire (\n\tgithub.com/spf13/cobra v1.8.0 // indirect\n)\n"
  "\nreplace example.com/unused => ../local-fork\n")
open(os.path.join(p, "SKILL.md"), "w").write(
  "---\nname: demo\nmetadata:\n  network:\n    outbound: []\n---\n")
secret = "sk-" + "test" + "0" * 12      # synthesized; no literal secret in repo
open(os.path.join(p, "app.js"), "w").write(
  'const k = "%s";\n' % secret +
  'fetch("https://api.example.com/v1", {headers:{k}});\n' +
  'fetch("http://10.0.0.9/hook");\n')
open(os.path.join(p, "bin.dat"), "wb").write(b"\x00\xff\x01binary")
open(os.path.join(p, "empty.js"), "w").write("")
PYFIX

chk "doctor rc0 + schema + CycloneDX 1.5 + 9 controls" "python3 -c 'import json,subprocess; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"doctor\"],capture_output=True,text=True).stdout); assert d[\"schema\"]==\"agent_bom.doctor.v1\" and d[\"spec\"]==\"CycloneDX 1.5\" and d[\"ruleset\"]==\"2.0.0\" and len(d[\"controls\"])==9'"
chk "sbom rc0 + cyclonedx shape + root name" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); assert d[\"bomFormat\"]==\"CycloneDX\" and d[\"specVersion\"]==\"1.5\" and d[\"version\"]==1 and d[\"serialNumber\"].startswith(\"urn:uuid:\") and d[\"metadata\"][\"component\"][\"name\"]==\"demo-app\" and d[\"metadata\"][\"component\"][\"bom-ref\"]==\"root:demo-app@1.2.3\"'"
chk "sbom 10 comps + bom-refs UNIQUE + key purls" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); ps=[c[\"purl\"] for c in d[\"components\"]]; br=[c[\"bom-ref\"] for c in d[\"components\"]]; assert len(ps)==10 and len(set(br))==10 and \"pkg:npm/lodash@4.17.21\" in ps and \"pkg:pypi/flask@2.3.3\" in ps and \"pkg:pypi/tomli@2.0.1\" in ps and \"pkg:golang/github.com/spf13/cobra@v1.8.0\" in ps and \"pkg:npm/%40\" not in ps'"
chk "sbom unpinned pip + pyproject bare purls" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); ps=[c[\"purl\"] for c in d[\"components\"]]; assert \"pkg:pypi/requests\" in ps and \"pkg:pypi/zope.interface\" in ps'"
chk "sbom env-marker stripped from purl" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); ps=[c[\"purl\"] for c in d[\"components\"]]; assert \"pkg:pypi/urllib3@1.26.2\" in ps and not any(\"python_version\" in p or \";\" in p for p in ps)'"
chk "sbom -o writes file + summary + rc3 on unwritable -o" "python3 -c 'import json,os,subprocess; out=os.environ[\"SBX\"]+\"/bom.json\"; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\",\"-o\",out],capture_output=True,text=True); assert r.returncode==0 and json.loads(open(out).read())[\"bomFormat\"]==\"CycloneDX\" and json.loads(r.stdout)[\"schema\"]==\"agent_bom.sbom.v1\"; r2=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",os.environ[\"SBX\"]+\"/proj\",\"-o\",\"/proc/1/nope-x\"],capture_output=True,text=True); assert r2.returncode==3'"
chk "scan rc4 on HIGH finding" "python3 -c 'import subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); assert r.returncode==4'"
chk "scan severity counts 1H/7M/2L" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); s=d[\"summary\"]; assert s[\"HIGH\"]==1 and s[\"MEDIUM\"]==7 and s[\"LOW\"]==2 and d[\"verdict\"]==\"FAIL\", s'"
chk "SEC redaction: zero secret chars leak" "python3 -c 'import subprocess,os,json; sec=\"sk-\"+\"test\"+\"0\"*12; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); f=[x for x in d[\"findings\"] if x[\"rule\"]==\"SEC-01\"]; assert len(f)==1 and \"[REDACTED len=19 sha256:\" in f[0][\"title\"] and sec not in r.stdout and not any(sec[i:i+8] in r.stdout for i in range(len(sec)-7)), f'"
chk "DEP-01 five distinct pins flagged" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); t=[f[\"title\"] for f in d[\"findings\"] if f[\"rule\"]==\"DEP-01\"]; assert len(t)==5 and len(set(t))==5 and any(\"lodash\" in x for x in t) and any(\"jest\" in x for x in t) and any(\"requests\" in x for x in t) and any(\"numpy\" in x for x in t) and any(\"zope.interface\" in x for x in t)'"
chk "NET-01 host + IP-literal drift" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); n=[f for f in d[\"findings\"] if f[\"rule\"]==\"NET-01\"]; assert len(n)==2 and any(\"api.example.com\" in f[\"title\"] for f in n) and any(\"10.0.0.9\" in f[\"title\"] for f in n)'"
chk "NET-01 boundary: badexample.com flagged, sub.example.com allowed" "python3 -c 'import json,os,subprocess; d2=os.environ[\"SBX\"]+\"/bnd\"; os.makedirs(d2); open(d2+\"/SKILL.md\",\"w\").write(\"---\nname: x\nmetadata:\n  network:\n    outbound: [\\\"example.com\\\"]\n---\"); open(d2+\"/a.sh\",\"w\").write(\"curl https://badexample.com/x\ncurl https://sub.example.com/y\n\"); d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",d2],capture_output=True,text=True).stdout); n=[f for f in d[\"findings\"] if f[\"rule\"]==\"NET-01\"]; assert len(n)==1 and \"badexample.com\" in n[0][\"title\"], n'"
chk "anti-hallucination: all control refs in registry" "python3 -c 'import json,subprocess,os; reg={k for k,_ in json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"doctor\"],capture_output=True,text=True).stdout)[\"controls\"]}; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); refs={r for f in d[\"findings\"] for r in f[\"control_refs\"]}; assert refs and refs <= reg, refs-reg'"
chk "--fail-severity CRITICAL downgrades to WARN rc0" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\",\"--fail-severity\",\"CRITICAL\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"verdict\"]==\"WARN\"'"
chk "scan + sbom + report rc3 on missing dir" "python3 -c 'import subprocess; assert subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",\"/no/such/dir-zz\"],capture_output=True).returncode==3; assert subprocess.run([\"python3\",\"scripts/bomscan.py\",\"sbom\",\"/no/such/dir-zz\"],capture_output=True).returncode==3; assert subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",\"/no/such/dir-zz\"],capture_output=True).returncode==3'"
chk "binary + zero-byte files do not crash scan" "python3 -c 'import subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); assert r.returncode==4 and \"bin.dat\" not in r.stdout and \"empty.js\" not in r.stdout'"
chk "GO-01 flags replace directive LOW" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); g=[f for f in d[\"findings\"] if f[\"rule\"]==\"GO-01\"]; assert len(g)==1 and g[0][\"severity\"]==\"LOW\" and \"../local-fork\" in g[0][\"title\"], g'"

# ── first two report runs seed the audit ledger (counts below assume this) ──
chk "report rc4 + writes report+sbom+sha + rc3 on unwritable -o" "python3 -c 'import json,os,subprocess; out=os.environ[\"SBX\"]+\"/report.json\"; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",os.environ[\"SBX\"]+\"/proj\",\"-o\",out],capture_output=True,text=True); assert r.returncode==4; d=json.loads(open(out).read()); assert d[\"schema\"]==\"agent_bom.report.v1\" and d[\"verdict\"]==\"FAIL\" and len(d[\"report_sha256\"])==64 and os.path.exists(out+\".sbom.json\"); r2=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",os.environ[\"SBX\"]+\"/proj\",\"-o\",\"/proc/1/nope-x\"],capture_output=True,text=True); assert r2.returncode==3'"
chk "audit two entries + mode 0600 after 2nd report" "python3 -c 'import json,os,stat,subprocess; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); f=os.environ[\"AGENT_BOM_AUDIT\"]; assert r.returncode==4 and len(open(f).readlines())==2 and oct(stat.S_IMODE(os.stat(f).st_mode))==\"0o600\"'"
chk "audit chain verify rc0 entries 2" "python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"audit\",os.environ[\"SBX\"]+\"/proj\",\"--verify\"],capture_output=True,text=True).stdout); assert d[\"chain_ok\"] is True and d[\"entries\"]==2'"
chk "audit seq monotonic gap-spotting" "python3 -c 'import json,os; L=[json.loads(l) for l in open(os.environ[\"AGENT_BOM_AUDIT\"])]; assert [r[\"seq\"] for r in L]==[0,1]'"
chk "trend UNCHANGED rc0 across identical runs" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"direction\"]==\"UNCHANGED\" and d[\"net\"]==0'"

# ── phase B: remediate EVERYTHING — verdict must go PASS ────────────────────
python3 - "$PROJ" <<'PYB'
import json, os, sys
p = sys.argv[1]
d = json.load(open(os.path.join(p, "package.json")))
d["license"] = "MIT"
d["dependencies"] = {"lodash": "4.17.21", "express": "4.18.2"}
d.pop("devDependencies")
open(os.path.join(p, "package.json"), "w").write(json.dumps(d))
open(os.path.join(p, "requirements.txt"), "w").write(
  "flask==2.3.3\nrequests==2.31.0\nnumpy==1.24.3\nurllib3==1.26.2\n")
open(os.path.join(p, "pyproject.toml"), "w").write(
  "[project]\nname = \"demo-app\"\nversion = \"1.2.3\"\ndependencies = [\n"
  "  \"tomli==2.0.1\",\n  \"zope.interface==6.0\",\n]\n")
open(os.path.join(p, "go.mod"), "w").write(
  "module example.com/demo\n\ngo 1.21\n\nrequire github.com/spf13/cobra v1.8.0\n")
open(os.path.join(p, "app.js"), "w").write(
  'const u = "https://declared.example.com/x";\n')
open(os.path.join(p, "SKILL.md"), "w").write(
  "---\nname: demo\nmetadata:\n  network:\n    outbound: [\"declared.example.com\"]\n---\n")
open(os.path.join(p, "LICENSE"), "w").write("MIT\n")
PYB

chk "clean report rc0 PASS zero findings" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"verdict\"]==\"PASS\" and sum(d[\"summary\"].values())==0'"
chk "trend IMPROVED net -10 verdict PASS" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"direction\"]==\"IMPROVED\" and d[\"net\"]==-10 and d[\"verdict_now\"]==\"PASS\"'"

# ── phase C: ONE regression — trend must flag REGRESSED rc1 ─────────────────
printf 'requests\n' >> "$PROJ/requirements.txt"
chk "regressed report rc0 WARN 1M" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"verdict\"]==\"WARN\" and d[\"summary\"][\"MEDIUM\"]==1'"
chk "trend REGRESSED rc1 net +1" "python3 -c 'import json,subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==1 and d[\"direction\"]==\"REGRESSED\" and d[\"net\"]==1'"
chk "--fail-severity INFO trips rc4 on MEDIUM" "python3 -c 'import subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\",\"--fail-severity\",\"INFO\"],capture_output=True,text=True); assert r.returncode==4'"
chk "surgical tamper breaks chain rc4 exactly [1]" "python3 -c 'import json,os,subprocess; f=os.environ[\"AGENT_BOM_AUDIT\"]; L=open(f).readlines(); assert len(L)==4, len(L); r=json.loads(L[1]); r[\"summary\"][\"verdict\"]=\"PASS\"; L[1]=json.dumps(r)+chr(10); open(f,\"w\").writelines(L); d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"audit\",os.environ[\"SBX\"]+\"/proj\",\"--verify\"],capture_output=True,text=True).stdout); assert d[\"chain_ok\"] is False and d[\"bad_lines\"]==[1] and d[\"entries\"]==4'"
chk "trend needs >=2 runs honest note rc0" "rm -f \"$PROJ/.agent_bom_audit.jsonl\" && python3 scripts/bomscan.py report \"$PROJ\" >/dev/null; python3 -c 'import json,subprocess,os; d=json.loads(subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True).stdout); assert \"need >=2\" in d[\"note\"]'"
chk "manifest parses + contracts + exit codes" "python3 -c 'import json; m=json.load(open(\"manifest.json\")); assert m[\"schema\"]==\"agent_bom.manifest.v1\" and {\"agent_bom.sbom.v1\",\"agent_bom.scan.v1\",\"agent_bom.report.v1\",\"agent_bom.trend.v1\",\"agent_bom.audit.v1\"} <= set(m[\"contracts\"]) and set(m[\"exit_codes\"]) >= {\"0\",\"1\",\"2\",\"3\",\"4\"} and \"FAIL\" in m[\"exit_codes\"][\"4\"] and m[\"policy\"][\"network\"] is False'"
chk "version sync 2.0.1 + 34 checks everywhere" "python3 -c 'import json,os; card=open(\"skill-card.md\").read() if os.path.exists(\"skill-card.md\") else \"2.0.0\"; assert json.load(open(\"manifest.json\"))[\"version\"]==\"2.0.1\" and \"version: 2.0.1\" in open(\"SKILL.md\").read() and \"34 offline checks\" in open(\"SKILL.md\").read() and \"v2.0.1\" in open(\"README.md\").read() and \"## 2.0.1\" in open(\"CHANGELOG.md\").read() and \"2.0.0\" in card'"
chk "engine stdlib-only, no network/process imports" "python3 -c 'import ast; t=ast.walk(ast.parse(open(\"scripts/bomscan.py\").read())); imps=set(); [imps.add(n.names[0].name.split(\".\")[0]) if isinstance(n,ast.Import) else imps.add((n.module or \"\").split(\".\")[0]) for n in t if isinstance(n,(ast.Import,ast.ImportFrom))]; banned={\"socket\",\"urllib\",\"requests\",\"httpx\",\"urllib3\",\"aiohttp\",\"http\",\"ssl\",\"subprocess\",\"ctypes\",\"telnetlib\",\"ftplib\",\"smtplib\",\"asyncio\",\"multiprocessing\"}; assert not (imps & banned), imps & banned'"
chk "trend per-target filter with shared ledger" "python3 -c 'import json,os,subprocess; b=os.environ[\"SBX\"]+\"/bnd\"; os.makedirs(b,exist_ok=True); open(b+\"/SKILL.md\",\"w\").write(\"---\nname: x\nmetadata:\n  network:\n    outbound: [\\\"example.com\\\"]\n---\"); open(b+\"/a.sh\",\"w\").write(\"curl https://badexample.com/x\n\"); open(b+\"/LICENSE\",\"w\").write(\"x\"); [subprocess.run([\"python3\",\"scripts/bomscan.py\",\"report\",b],capture_output=True) for _ in (1,2)]; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",b],capture_output=True,text=True); d=json.loads(r.stdout); assert r.returncode==0 and d[\"direction\"]==\"UNCHANGED\" and d[\"target\"]==os.path.abspath(b); r2=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"trend\",os.environ[\"SBX\"]+\"/proj\"],capture_output=True,text=True); assert json.loads(r2.stdout)[\"target\"].endswith(\"/proj\")'"
chk "bad --fail-severity value rc2 usage" "python3 -c 'import subprocess,os; r=subprocess.run([\"python3\",\"scripts/bomscan.py\",\"scan\",os.environ[\"SBX\"]+\"/proj\",\"--fail-severity\",\"BOGUS\"],capture_output=True,text=True); assert r.returncode==2'"

echo; echo "PASS=$P FAIL=$F"; [ "$F" -eq 0 ]
