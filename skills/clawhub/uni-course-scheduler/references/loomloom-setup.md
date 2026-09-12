# LoomLoom Cloud Execution Guide (Buyer Guide)

## What is LoomLoom?

LoomLoom is a batch LLM cloud execution platform that runs structured tasks in parallel
through a fixed pipeline and returns structured results. This Skill's "Cloud Standard
Mode" runs through the LoomLoom marketplace.

This Skill supports **two cloud platforms**; choose based on your payment method
(see "Which platform should I choose?" below).

## Which platform should I choose? (read before first use)

The same Skill can connect to either platform; **your payment method decides**, not
your nationality or IP:

| | **Shengsuanyun (China mainland)** | **CogFoundry (International)** |
|---|---|---|
| Payment | China mainland payment (Alipay / WeChat / UnionPay) | International credit card (Visa / Mastercard) |
| Price | ¥0.5 / run | $0.10 / run |
| Server | `https://loomloom.shengsuanyun.com/loom/v1` | `https://loomloom.cogfoundry.ai/loom/v1` |
| Key console | console.shengsuanyun.com | CogFoundry console |
| Token env | `LOOMLOOM_TOKEN_SHENGSUANYUN` | `LOOMLOOM_TOKEN_COGFOUNDRY` |

> **How to choose**: If you can pay with China mainland methods → use Shengsuanyun.
> If you can pay with an international credit card → use CogFoundry.
> Not sure which you can top up? Check both and pick the one you can actually pay on.

## Install LoomLoom

> 🔴 **Token security warning (READ FIRST)**: Your Token / API key is **as sensitive as a
> password** — anyone with it can run paid jobs on your account.
> **NEVER paste your Token into any AI conversation, chat window, group chat, or public channel.**
> If a Token was ever exposed (e.g. pasted into a chat), go to the platform console and
> **revoke and regenerate it immediately**.
> Recommended: use interactive `loomloom login` below (the key never passes through a chat),
> prefer storing the key securely (e.g. a git-ignored `.env`, macOS Keychain, or `loomloom login`) — never paste it into a conversation.

### Option A: One-command install (recommended)

Paste the following into any AI assistant (**do NOT include your Token**; log in
interactively with `loomloom login` afterwards):

> Please install LoomLoom in this project: use the official release install script
> (never `curl | bash` from an untrusted source). Pin to a specific reviewed release
> tag & commit, and verify the artifact checksum after install (see below).
> Server: 【the server of your chosen platform, see table above】
> After installing, run `doctor` once to check everything works.

**Supply-chain hygiene (recommended):**
- Install from the official signed release (tagged version + checksum), not by cloning the mutable `main` branch.
- Verify remote / tag / commit / checksum before load; keep the CLI updated through a documented, reviewed bump.
- Run the CLI with the minimum privileges needed; keep cloud tokens only in local env/config files, never in project files shared with agents.

**Log in after install (recommended — key never passes through a chat):**
```bash
loomloom login -s <server-of-your-platform>   # enter the key interactively
loomloom doctor -s <server-of-your-platform>  # verify login
```

### Option B: Manual install

1. Apply for an API key on your chosen platform's console (Shengsuanyun:
   console.shengsuanyun.com; CogFoundry: CogFoundry console) — **keep the key only in
   your local files, never paste it into any conversation**
2. Clone a specific reviewed tag & commit (NOT the live `main` branch), then verify the release checksum/signature before use:
   ```bash
   git clone --branch <reviewed-tag> --depth 1 https://gitee.com/cogfoundry/loomloom.git
   cd loomloom && cat <published checksum> && <verify>  # e.g. pip/installer integrity
   ```
3. Configure credentials securely — **do not store the token in plaintext in your shell rc files (`~/.zshrc`/`~/.bashrc`)**, which risks exposing your key to other tools and scripts. Prefer, in order:
   - **Best — dedicated env file, git-ignored, never committed:**
     ```bash
     cat > /path/to/project/.env <<EOF
     LOOMLOOM_SERVER='https://loomloom.shengsuanyun.com/loom/v1'
     LOOMLOOM_TOKEN_SHENGSUANYUN='your-shengsuanyun-api-key'
     EOF
     chmod 600 /path/to/project/.env        # owner-only read
     ```
     Load per session (does not persist plaintext in rc files):
     ```bash
     set -a; source /path/to/project/.env; set +a
     ```
   - **Good (macOS)** — store in the macOS Keychain:
     ```bash
     security add-generic-password -s loomloom -a "$USER" -w 'your-shengsuanyun-api-key'
     export LOOMLOOM_TOKEN_SHENGSUANYUN=$(security find-generic-password -s loomloom -a "$USER" -w)
     ```
   - **Good (all platforms)** — use `loomloom login` which manages the credential via the CLI, then `loomloom doctor` to verify.
   - Use the server/token variable names of the row you chose:
     - Shengsuanyun (China mainland payment): `LOOMLOOM_SERVER='https://loomloom.shengsuanyun.com/loom/v1'` + `LOOMLOOM_TOKEN_SHENGSUANYUN`.
     - CogFoundry (international credit card): `LOOMLOOM_SERVER='https://loomloom.cogfoundry.ai/loom/v1'` + `LOOMLOOM_TOKEN_COGFOUNDRY`.
   - Keep the token only in local env/config/Keychain; never in a conversation.
> **Security note:** If you keep using shell rc exports at all, keep them untracked and never push; prefer `.env`/Keychain/`login` above.


4. Verify (with your chosen platform's server):
   ```bash
   source ~/.zshrc
   loomloom doctor
   ```

## No LoomLoom? The Skill still works

When LoomLoom is not installed, this Skill runs in **Local Quick Mode**:
the agent searches the course catalog online, recommends courses for your goals,
builds a timetable, and performs conflict detection on its own.
Excel generation and validation scripts behave identically in both modes.

## Cloud execution flow (marketplace buyer path)

1. **Collect the catalog locally first (mandatory)**: the agent searches the school's
   official program handbook/course catalog online and organizes the catalog text.
   The cloud pipeline has NO internet access — an empty catalog only yields placeholder output.

2. **Find the SkillBot and download the workbook**:
   ```bash
   loomloom market list
   loomloom market show <listing-id>
   loomloom market workbook download <listing-id> --output-file input.xlsx
   ```

3. **Fill in the workbook**: one student per row — school, education system, major,
   year level, planning mode, goals & schedule preferences, the course catalog text
   (collected in step 1), and semester info.

4. **Validate + quote**:
   ```bash
   loomloom market workbook validate <listing-id> --file input.xlsx
   loomloom market workbook quote <listing-id> --file input.xlsx
   ```

5. **Show the platform's estimated fee to the student and get explicit confirmation**
   (never submit without confirmation).

6. **Execute** (generate a new client-request-id per run):
   ```bash
   loomloom market workbook run <listing-id> --file input.xlsx \
     --confirm --client-request-id <unique-id>
   ```

7. **Fetch results**:
   ```bash
   loomloom usage list
   loomloom usage get <run-transaction-id>
   ```

8. Map the results into this Skill's JSON input format (see cloud-output-format.md),
   then pass them to `scripts/generate_excel.py` and `scripts/generate_ics.py`.

> Note: the cloud pipeline's internal prompts and step definitions are the author's
> private assets. Buyers call the Listing and never need (and cannot) inspect internals.
