---
name: huawei-cloud-find-skills
description: |
  Invoke this skill to search, list, query, discover, browse, find and install any Huawei Cloud (华为云) agent skill. Triggers include: "华为云", "华为云有什么skill", "华为云相关skill", "华为云agent skill 市场", "华为云skill类目", "explore Huawei Cloud skills", "show Huawei Cloud skill categories", "does a Huawei Cloud skill exist for...", "which Huawei Cloud skills exist", "搜索华为云技能", "查询华为云skill列表", "有没有管理ECS/OBS/RDS的skill", "帮我找 XX 华为云skill", "介绍 XX Skill 内容", "华为云 XX Skill 具体做什么", "安装华为云Skill".
---

> [!IMPORTANT]
> **For any Huawei Cloud query or management task:**
> 1. **Search** — use this skill (`huawei-cloud-find-skills`) to find the relevant Skill.
> 2. **Install** — install the matched Skill (see [Step 3](#step-3-install-skill)).
> 3. **Execute** — follow the installed Skill's instructions to fulfill the request.

## Overview

This skill enables users to efficiently search, discover, and install Huawei Cloud skills.

<!-- cli-install-version: 3.8.0 -->

**Dependency**: Quality telemetry is collected automatically via `skill-quality-cli` (installed by `scripts/ensure_cli.sh` if absent).

## Step 0: Install skill-quality-cli (optional, ensured if absent)

```bash
> **⚠️ 强制要求：执行本 skill 的任何 hcloud 命令必须用 `skill-quality-cli run --skill-name huawei-cloud-find-skills -- ` 包裹，禁止裸调 hcloud。**

bash scripts/ensure_cli.sh   # 幂等确保(缺则就绪一次, 已装跳过; 不自动升级)
export PATH="$HOME/.local/bin:$PATH"
skill-quality-cli version    # 确认可用
```

> `skill-quality-cli` 未安装时由 `scripts/ensure_cli.sh` **自动就绪**(幂等); **不会自动升级**(需手动 `skill-quality-cli upgrade`)。
> 未安装/离线时静默跳过, 不影响业务流程。升级与关闭上报见 [references/cli-installation-guide.md](references/cli-installation-guide.md)。

## Scenario Description

This skill enables users to:

- **Search Skills**: Find skills by keyword, category, or both (matched against name, description, and triggers)
- **Browse Categories**: Explore available skill categories
- **View Skill Details**: Fetch full SKILL.md content from GitHub for specific skills
- **Install Skills**: Guide users through skill installation via `npx skills add` (GitCode default), `npx clawhub install`, or fallback GitHub method

**Architecture**: GitCode API v5 (`index.json` + `cn-en-map.json`) → HTTP GET (base64 decode) → In-memory search → GitHub raw fetch for details → Install

### Use Cases

- "Find a skill for managing ECS instances"
- "What Huawei Cloud skills are available for OBS?"
- "华为云有哪些 VPC 相关的 skill?"
- "Browse all available Huawei Cloud skills"
- "Install a skill for RDS management"
- "帮我找一个华为云网络相关的skill"

## Prerequisites

- **Python 3.6+** must be installed and available as `python` (or `python3`) in `PATH`
- **Network access** to `gitcode.com` (API v5 for index) and `github.com` / `raw.githubusercontent.com` (for skill details)

### Step 0: Check Python Environment

> **MANDATORY**: Before running any script command, verify Python is available.

```bash
# Check Python availability
python --version   # or: python3 --version
```

If the command fails or returns Python 2.x:

1. **Install Python 3**: Download from [python.org](https://www.python.org/downloads/) or use a package manager:
   ```bash
   # macOS
   brew install python3
   # Ubuntu/Debian
   sudo apt-get install python3
   # Windows — download installer from python.org, check "Add Python to PATH"
   ```
2. **Verify after install**: Run `python --version` again to confirm Python 3.6+ is available
3. **If `python` points to Python 2**: Use `python3` instead of `python` in all commands below

### Step 0.5: Check KooCLI Version (NON-BLOCKING)

> **OPTIONAL**: A KooCLI (`hcloud`) availability/version check that **never blocks the flow**.
> Skills installed later may depend on KooCLI; this step warns early, then **always
> continues to Step 1** regardless of the outcome.

```bash
# Check KooCLI availability & version (non-blocking)
python scripts/check-koocli.py
```

→ [scripts/check-koocli.py](scripts/check-koocli.py) (Python — cross-platform)

| Outcome | Behavior |
|---------|----------|
| `hcloud` installed and version OK (≥ 3.0.0) | **Silent pass** — no output |
| `hcloud` installed but too old | Prints an upgrade reminder (`hcloud update -y`) |
| `hcloud` not installed | Prints an install reminder (official KooCLI guide link) |

> The script always exits `0` — it is informational only and never interrupts
> search or installation.
- **`skill-quality-cli`** — ensured by `bash scripts/ensure_cli.sh` (idempotent, skips if present)
  - Upgrade: run `skill-quality-cli upgrade` manually (no auto-upgrade)
  - Disable telemetry report: set `SKILL_QUALITY_REPORT=0`
  - Upgrade: run `skill-quality-cli upgrade` manually (no auto-upgrade)
  - Disable telemetry report: set `SKILL_QUALITY_REPORT=0`
## Repository Info

```
INDEX_REPO=developer-skill/skills-group-contribution
INDEX_BRANCH=test-for-index
SKILLS_REPO=huaweicloud/huaweicloud-skills
SKILLS_BRANCH=master
RAW_BASE=https://raw.githubusercontent.com/$SKILLS_REPO/$SKILLS_BRANCH
```

## Index Source

The search script fetches the skill index from GitCode API v5 via HTTP GET (base64 auto-decoded):

```
SKILLS_INDEX_URL=https://gitcode.com/api/v5/repos/developer-skill/skills-group-contribution/contents/skills-index/index.json?ref=test-for-index
SKILLS_CN_EN_MAP_URL=https://gitcode.com/api/v5/repos/developer-skill/skills-group-contribution/contents/skills-index/cn-en-map.json?ref=test-for-index
```


## Core Workflow and Core Commands

### Step 1: Search Skills

> **MANDATORY**: The agent MUST execute the search script to search the skill index. Do NOT read the JSON file directly — always use the script.

Given `keyword` (from AI-understood user intent) and optional `category`, run the search script:

```powershell
# PowerShell
python scripts/search-skills.py -k "<keyword>"
python scripts/search-skills.py -k "<keyword>" -c "<category>"
python scripts/search-skills.py -c "<category>"
```

```bash
# Bash
python scripts/search-skills.py -k "<keyword>"
python scripts/search-skills.py -k "<keyword>" -c "<category>"
python scripts/search-skills.py -c "<category>"
```

→ [scripts/search-skills.py](scripts/search-skills.py) (Python — cross-platform)

**What the script does**:
1. Fetches `index.json` and `cn-en-map.json` via HTTP GET from GitCode API v5 (auto-decodes base64 content)
2. Expands keywords via `cn-en-map.json` (bidirectional CN↔EN, e.g., "ECS" → "ECS, 弹性云服务器, 云服务器")
3. Scores each skill: name match **+10**, trigger match **+8**, description match **+5**, service match **+3**
4. Sorts by score descending, outputs formatted results with matched keywords
5. Reports every result's skill name to the install-count API (`skills/<category>/<service>/<name>`) as an exposure impression — fire-and-forget, never blocks or fails the search
6. **Auto-reports execution quality via `skill-quality-cli`** (resolved as: PATH binary →
   `~/.local/bin/skill-quality-cli`, manually installed) — `report
   --skill-name huawei-cloud-find-skills --status success|sys_fail|biz_fail` is fired on
   **every** run (success and failure paths), fire-and-forget. When `skill-quality-cli` is
   not installed, reporting is skipped silently. No action needed from the
   caller; when the whole command is already wrapped with `skill-quality-cli run`
   (SKILL_TRACE_ID set), the script skips its own report to avoid double counting

**Fallback iteration** (if no results): 1) Switch CN↔EN keywords 2) Expand keywords 3) Remove category filter 4) Try synonyms 5) List all skills

The process should persist until the skill is found or its absence is confirmed. In the event of total failure, notify the user of the specific steps that were attempted.

### Step 2: View Skill Details (optional)

Fetch the full SKILL.md content from GitHub for intent validation. Skip this step if the search results from Step 1 are sufficiently informative.

```bash
# URL pattern — use the skill's category, service, and name from index
DETAIL_URL="https://raw.githubusercontent.com/huaweicloud/huaweicloud-skills/master/skills/${category}/${service}/${name}/SKILL.md"
```

The agent can fetch this URL using `curl` or its web-fetch tool, then present the skill's full documentation to the user.

### Step 3: Install Skill

> **MANDATORY**: Before installing, the agent MUST call the install-count API to record the installation. Then use one of the install commands below. Option A is the default; Option C is a fallback when Option A is unavailable.

#### Step 3.1: Record Install Count

Before executing the install command, call the install-count API. The `skill_id` is constructed from the search results in Step 1: `skills/<category>/<service>/<skill-name>`.

> **IMPORTANT**: The `category` and `service` values MUST be taken directly from the Step 1 search output (format: `name (category/service)`). Do NOT guess or hardcode them.
>

```bash
curl -s -X POST "https://devdata2.huaweicloud.com/rest/developer/fwdo/rest/developer/servlet/hdskillservice/v1/obs/findcounts/increment" -H "Accept: application/json, text/plain, */*" -H "Content-Type: application/json" -H "Origin: https://skills.huaweicloud.com" -H "Referer: https://skills.huaweicloud.com/" -d "{\"skill_id\":\"skills/<category>/<service>/<skill-name>\"}"
```

> This is a fire-and-forget request. Do NOT block the install flow on its success or failure.

#### Step 3.2: Execute Install Command

> **MANDATORY**: Every install command below MUST be wrapped with
> `skill-quality-cli run --skill-name huawei-cloud-find-skills -- ...` so the install
> flow automatically reports execution quality (fire-and-forget). This cannot be
> skipped — the quality report is bound to the main flow.

```bash
# Option A: npx skills add from GitCode (default)
skill-quality-cli run --skill-name huawei-cloud-find-skills -- npx skills add https://gitcode.com/huaweicloud/huaweicloud-skills.git#master --skill <skill-name> -y

# Option B: npx clawhub install (OpenClaw ecosystem)
skill-quality-cli run --skill-name huawei-cloud-find-skills -- npx clawhub install <skill-name> -y

# Option C (fallback): npx skills add from GitHub
skill-quality-cli run --skill-name huawei-cloud-find-skills -- npx skills add huaweicloud/huaweicloud-skills --skill <skill-name> -y
```

> When `skill-quality-cli` is not on PATH, use the absolute path from Step 0
> (`~/.local/bin/skill-quality-cli`). When `skill-quality-cli` is not installed,
> execute the install command as-is and skip reporting.

If all installation attempts fail, report the error message to the user. Do NOT attempt any method outside the commands above.

## Parameter Confirmation

| Parameter | Required/Optional | Description | Default |
|-----------|-------------------|-------------|---------|
| `Keyword` | Optional | Search keyword (matched against name, description, triggers, service) | None |
| `Category` | Optional | Category code for filtering (e.g., "computing", "storage", "network") | None |
| `skill-name` | Required (Step 3) | Exact skill name for installing | None |
| `SKILL_QUALITY_DISABLE` | Optional | Set to `1` to disable quality reporting entirely (local debugging) | `0` |
| `SKILL_QUALITY_TRIGGER` | Optional | Trigger type reported (`agent` / `workflow` / `auto` / `manual`) | `agent` |
| `SKILL_QUALITY_SESSION_ID` | Optional | Reporting session id (explicit, provided by caller) — empty to skip report | None |
| `SKILL_QUALITY_CLI_HOME` | Optional | Directory containing `skill-quality-cli` if not on `PATH` | `~/.local/bin` |
| `SKILL_QUALITY_REPORT` | Optional | Set to `0` to disable reporting entirely (opt-out) | `1` |

## References

| Document | Description |
|----------|-------------|
| GitCode API v5 `index.json` | Skill index fetched via HTTP GET (base64 decoded) |
| GitCode API v5 `cn-en-map.json` | Chinese-English keyword mapping fetched via HTTP GET (base64 decoded) |
| [scripts/search-skills.py](scripts/search-skills.py) | Search script (Python) — fetches from GitCode API v5, expands keywords, scores, sorts, reports search-result exposures |
| [scripts/check-koocli.py](scripts/check-koocli.py) | Step 0.5 non-blocking KooCLI (`hcloud`) availability/version check |
| [references/cli-installation-guide.md](references/cli-installation-guide.md) | Manual installation guide for `skill-quality-cli` (quality reporting, optional) |
| [references/iam-policies.md](references/iam-policies.md) | IAM 权限说明 — 本 Skill 仅访问公开接口，无需任何 IAM 凭证/策略 |
| [references/verification-method.md](references/verification-method.md) | 验证方法 — 各场景的验证步骤与预期结果 |
| [references/acceptance-criteria.md](references/acceptance-criteria.md) | 验收标准 — 功能/数据/安全/文件规范验收项 |

## Search Heuristics

> Optional reference for keyword-to-category hints. The agent can infer categories from `index.json` without these.

- Cloud infrastructure keywords (ecs, bms, vpc, obs, rds, ...) → likely `computing`, `network`, `storage`, etc.
- Tool keywords (cli, terraform, koo) → likely `devtools`
- Management keywords (monitoring, alarm, log) → likely `monitoring`

## Troubleshooting

### Issue: `python` is not recognized as a command

**Cause**: Python 3 is not installed or not in `PATH`
**Solution**: Install Python 3.6+ and ensure it is added to `PATH`. On Windows, re-run the installer and check "Add Python to PATH". Alternatively, use `python3` if available.

### Issue: `skill-quality-cli: command not found` (exit 127)

**Cause**: `skill-quality-cli` is not installed, or installed into `~/.local/bin/`
but that directory is not on the current shell's `PATH`.
**Solution**: Follow [references/cli-installation-guide.md](references/cli-installation-guide.md)
to install manually, then run `export PATH="$HOME/.local/bin:$PATH"` in the current shell.
The search script resolves `skill-quality-cli` on PATH → `~/.local/bin/skill-quality-cli`
automatically; when unavailable, reporting is skipped silently and business flow is unaffected.

### Issue: Script fails with `SyntaxError: invalid syntax`

**Cause**: System `python` points to Python 2.x (the script requires Python 3.6+)
**Solution**: Run with `python3` explicitly: `python3 scripts/search-skills.py -k "<keyword>"`

### Issue: Script fails with "Failed to fetch index.json"

**Cause**: GitCode API v5 URL unreachable
**Solution**: Verify network connectivity to `gitcode.com`

### Issue: GitCode API v5 returns 404

**Cause**: File path incorrect or the branch is not `test-for-index`
**Solution**: Verify the skill's `category`, `service`, and `name` from search results

### Issue: Search returns no results

**Cause**: Keywords don't match any skill
**Solution**:
1. Try broader keywords
2. Switch between Chinese and English keywords (e.g., "对象存储" → "obs")
3. List all skills: `python scripts/search-skills.py -c "computing"`

## Notes

- This skill is **read-only** and does not create any cloud resources
- **No cache management needed** — index is fetched fresh from GitCode API v5 each run
- **Network required** — index data is hosted on GitCode, fetched via HTTP GET (base64 decoded)
- **MUST use script to search** — do not read index.json directly
- Index repo: `https://gitcode.com/developer-skill/skills-group-contribution` (branch: `test-for-index`)
- Skills repo: `https://github.com/huaweicloud/huaweicloud-skills` (branch: `master`)
- **KooCLI**: the search/install flow itself is pure Python + HTTP (no service-level
  hcloud commands, no `--cli-region`). Step 0.5 performs only a non-blocking KooCLI
  availability/version check (`hcloud version` via `scripts/check-koocli.py`) to warn
  about a missing/outdated CLI before installing skills that depend on it.

<!-- cli-inject-version: 3.8.0 -->
## Quality Reporting (Unified CLI)

> CLI installation is **manual and optional** — see
> [references/cli-installation-guide.md](references/cli-installation-guide.md).
> This skill does not auto-install or bundle any reporting CLI.
> `session_id` is **explicitly passed by the caller** (via `SKILL_QUALITY_SESSION_ID`
> or `.quality_report.json`); the CLI never reads host session storage.

**💡 Hard-bound reporting (cannot be skipped):** the search main flow (Step 1) and
install flow (Step 3) trigger a quality report **automatically on every run** — see
below. Running the bare script still reports (resolution: `skill-quality-cli` on PATH →
`~/.local/bin/skill-quality-cli`); reporting failures are fire-and-forget and never block
the business flow. When no `skill-quality-cli` is installed, reporting is skipped silently.

### Mode 1 (recommended, automatic) — wrap the whole execution
For script/command-style skills, wrap the entire command with `run`:
```bash
skill-quality-cli run --skill-name huawei-cloud-find-skills -- <your command>
```
`search-skills.py` detects the wrapper (SKILL_TRACE_ID) and skips its own report —
exactly one report per run.

### Mode 2 (multi-step / instruction-style skills)
Report once per step (callable multiple times):
```bash
skill-quality-cli report --skill-name huawei-cloud-find-skills --status <success|sys_fail|biz_fail|cancel>
```

> **⚠️ Mandatory rule: any hcloud command or install command executed by this skill MUST be wrapped with `skill-quality-cli run` — bare hcloud/install calls are strictly forbidden.** (When `skill-quality-cli` is not installed, proceed with the business command as-is.)

### Reporting opt-out
Telemetry is on by default. To disable reporting entirely (rare), set
`SKILL_QUALITY_REPORT=0` (or `SKILL_QUALITY_DISABLE=1`) in the environment.

### CLI upgrade
Upgrade is **manual**: run `skill-quality-cli upgrade` (or re-install following
[references/cli-installation-guide.md](references/cli-installation-guide.md)).
No auto-upgrade occurs.

<!-- clawhub-compliance: v1.4 -->
