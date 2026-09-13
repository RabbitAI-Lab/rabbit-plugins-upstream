# Recipes — httrack skill v2.0.0

All recipes go through `scripts/mirror.py`. Add `--json` for the machine report.

## 1. Snapshot one page (documentation, article, evidence)

```bash
python3 scripts/mirror.py snapshot "https://docs.example.org/ref/page" -o ./snap --json
```

Fetches exactly the URL plus its inline assets (CSS/JS/images/fonts), follows
NO links — safe, small, quick. Resume an interrupted snapshot with `--resume`.

## 2. Bounded mirror of a site

```bash
python3 scripts/mirror.py mirror "https://example.org" -o ./mirror \
  --depth 2 --sockets 2 --json
```

Defaults are polite: `-s2` (always obey robots), 2 sockets, same-address
travel. Depth is link-hops from the seed (`--depth 0` = seed only, assets may
be missing — use `snapshot` for that instead).

## 3. Incremental update / continue

Same command you originally ran, plus `--resume`. HTTrack resumes from its
cache (`hts-cache`) instead of recrawling. Works after timeouts and errors.

## 4. Filtered mirrors (scan rules)

```bash
# collect just PDFs under this address
python3 scripts/mirror.py mirror "https://example.org" -o ./pdfs \
  --depth 3 --allow '*.pdf' --deny '*'

# everything except forums and login pages
python3 scripts/mirror.py mirror "https://example.org" -o ./mirror --depth 2 \
  --deny '*/forums/*' --deny '*/login*'
```

Patterns are globs handed to HTTrack as `+pat`/`−pat` scan rules. Sign and
spaces are rejected at the wrapper — pass plain globs only.

## 5. Time-boxed research crawl

```bash
python3 scripts/mirror.py mirror "https://example.org" -o ./research \
  --depth 3 --max-time 900 --max-mb 200 --json
```

`--max-time` maps to `-E` (mirror time limit); `--max-mb` maps to `-M` (overall
size ceiling). On timeouts the wrapper reports a warning and you continue with
`--resume`.

## 6. Loop it (agent pattern)

```python
import json, subprocess
def mirror(url, out, **kw):
    argv = ["python3", "scripts/mirror.py", "mirror", url, "-o", out, "--json"]
    for k, v in kw.items():
        argv += ["--" + k.replace("_", "-"), str(v)]
    p = subprocess.run(argv, capture_output=True, text=True)
    return p.returncode, json.loads(p.stdout)
rc, rep = mirror("https://example.org", "./mirror", depth=2, max_time=600)
if rc:                     # 3 missing binary, 4 run failed, 2 my fault
    ...retry with rc==4 and resume=True...
print(rep["result"]["files"], rep["result"]["bytes"])
```
