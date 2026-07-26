# Red Flag Rules (30+)

> Full catalog of red-flag patterns `skill-auditor` scans for.
> Keep in sync with `scripts/score.py` `RULES` dict.
>
> Severity weights:
> - **CRITICAL** = 25 pts — direct credential exfil, RCE
> - **HIGH** = 15 pts — strong malicious indicators
> - **MEDIUM** = 10 pts — suspicious, needs review
> - **LOW** = 5 pts — minor concerns / bad practice

Score is additive, capped at 100. See [scoring.md](./scoring.md) for the full model.

---

## CRITICAL (25 pts each)

| Rule ID | Pattern | Rationale |
|---|---|---|
| `CRED_SSH` | Reads `~/.ssh/` (id_rsa, id_ed25519, known_hosts, config) | SSH private keys = full server access |
| `CRED_AWS` | Reads `~/.aws/credentials` or `~/.aws/config` | AWS keys = cloud account takeover |
| `CRED_KEYCHAIN` | `security find-generic-password` (macOS), `secret-tool` (Linux), Windows Credential Manager | OS keychain = stored passwords |
| `CRED_COOKIES` | Reads Chrome/Safari/Firefox cookie DB, session storage | Steals logged-in sessions |
| `IDENTITY_FILES` | Reads/writes `MEMORY.md`, `USER.md`, `SOUL.md`, `IDENTITY.md` | Core agent identity manipulation |
| `RCE_EVAL` | `eval(`, `exec(` with f-string / input / argv | Arbitrary code execution |
| `RCE_PICKLE` | `pickle.loads(`, `yaml.load(` without `Loader=SafeLoader` | Deserialization RCE |
| `EXFIL_LARGE` | Reads >10 user files + prepares network upload | Data exfiltration pattern |
| `PERM_SUDO` | `sudo `, `os.getSudo`, modifies `/etc/sudoers` | Privilege escalation |

---

## HIGH (15 pts each)

| Rule ID | Pattern | Rationale |
|---|---|---|
| `NET_CURL_PIPED` | `curl ... \| sh`, `curl ... \| bash`, `wget ... \| bash` | Remote code execution |
| `NET_IP_LITERAL` | Network call to `http://123.45.67.89/` (raw IP) | Evades DNS-based audit |
| `NET_PASTEBIN` | Uploads to `pastebin.com`, `paste.ee`, `0bin`, `hastebin` | Common credential drop |
| `NET_UNKNOWN_HOST` | Network call to non-allowlisted domain | See trust-database.md for allowlist |
| `OBFUSCATE_BASE64` | `base64 -d` / `base64.b64decode` on string >120 chars | Obfuscated payload |
| `OBFUSCATE_HEX_BLOB` | Long hex string >200 chars in code | Encoded binary / payload |
| `OBFUSCATE_MINIFIED` | Minified JS in `.md`/`.sh` file | Hidden logic |
| `SHELL_TRUE` | `subprocess.run(..., shell=True)` with external input | Command injection |
| `SUPPLY_PIP_URL` | `pip install https://` / `npm install https://` (not registry) | Typosquat / malware host |
| `FILE_WRITE_OUTSIDE` | Writes to `~/.bashrc`, `~/.zshrc`, `/etc/`, `~/Library/LaunchAgents/` | Persistence / system modification |
| `PERM_CHMOD_777` | `chmod 777` on any path | World-writable, persistence precursor |

---

## MEDIUM (10 pts each)

| Rule ID | Pattern | Rationale |
|---|---|---|
| `NET_NO_TLS` | `http://` network call (not https) | MITM risk |
| `NET_TOR` | `.onion` URL or tor proxy reference | Anonymous network = high-risk |
| `CRED_ENV_TOKEN` | Reads `*_TOKEN`, `*_API_KEY`, `*_SECRET` env vars without `primaryEnv` in frontmatter | Undeclared credential access |
| `DYN_IMPORT` | `importlib.import_module(...)` with external input | Loads arbitrary modules |
| `FILE_DELETE` | `os.remove` / `rm` outside workspace | Destructive |
| `NET_TELEMETRY` | Sends analytics/telemetry without opt-in | Privacy violation |
| `SUPPLY_PKG_LIST` | Installs packages without listing in `metadata.openclaw.install` | Supply chain risk |
| `PERM_BROAD_SCOPE` | Requests OAuth scopes like `repo`, `admin:*`, `user` | Over-broad permissions |
| `PERM_REQUEST_KEY` | Asks user to paste API key/password in chat | Should use system keychain |

---

## LOW (5 pts each)

| Rule ID | Pattern | Rationale |
|---|---|---|
| `MISSING_FRONTMATTER` | SKILL.md missing `name` or `description` | Required by spec |
| `NO_LICENSE` | No LICENSE file in skill folder | Usage rights unclear |
| `NO_VERSION` | No `version` field in frontmatter | Supply chain audit harder |
| `HARDCODED_PATH` | Absolute paths like `/Users/foo/` or `C:\Users\` | Portability + audit issue |
| `EVAL_NO_INPUT` | `eval()` / `exec()` but input appears static | Still bad practice |
| `SLEEP_LONG` | `time.sleep(>60)` or `sleep 60+` | Possible timing evasion / C2 beacon |

---

## Allowlist (Network)

`NET_UNKNOWN_HOST` triggers when the script sees a network call to a domain not in the allowlist below. Edit `references/trust-database.md` to add domains.

Default allowlist (high-reputation infrastructure):

- `github.com`, `api.github.com`, `raw.githubusercontent.com`
- `clawhub.ai`
- `pypi.org`, `files.pythonhosted.org`
- `registry.npmjs.org`
- `openai.com`, `api.openai.com`
- `anthropic.com`, `api.anthropic.com`
- `googleapis.com`
- `cloudflare.com`, `workers.cloudflare.com`
- `api.open-meteo.com` — public free weather API, no key required

Everything else is unknown → HIGH severity.

---

## Contributing New Rules

1. Add the rule to `scripts/score.py` `RULES` dict.
2. Add the detection pattern to `scripts/vet.py`.
3. Add a row to the appropriate severity table above.
4. Add a test case to `tests/test_vet.py`.
5. Document the rationale (one line on why this pattern is suspicious).
