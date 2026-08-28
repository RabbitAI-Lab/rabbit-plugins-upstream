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
> or write the key into your local `~/.zshrc` file — never paste it into a conversation.

### Option A: One-command install (recommended)

Paste the following into any AI assistant (**do NOT include your Token**; log in
interactively with `loomloom login` afterwards):

> Please install LoomLoom in this project: installation is at
> https://github.com/Cogfoundry-ai/loomloom or
> https://gitee.com/cogfoundry/loomloom
> Server: 【the server of your chosen platform, see table above】
> After installing, run `doctor` once to check everything works.

**Log in after install (recommended — key never passes through a chat):**
```bash
loomloom login -s <server-of-your-platform>   # enter the key interactively
loomloom doctor -s <server-of-your-platform>  # verify login
```

### Option B: Manual install

1. Apply for an API key on your chosen platform's console (Shengsuanyun:
   console.shengsuanyun.com; CogFoundry: CogFoundry console) — **keep the key only in
   your local files, never paste it into any conversation**
2. Clone the repo and install per its README:
   ```bash
   git clone https://gitee.com/cogfoundry/loomloom.git
   ```
3. Configure environment variables in `~/.zshrc` or `~/.bashrc` (**use the server and
   token variable name of the row you chose**):
   - Shengsuanyun (China mainland payment):
     ```bash
     export LOOMLOOM_SERVER='https://loomloom.shengsuanyun.com/loom/v1'
     export LOOMLOOM_TOKEN_SHENGSUANYUN='your-shengsuanyun-api-key'
     ```
   - CogFoundry (international credit card):
     ```bash
     export LOOMLOOM_SERVER='https://loomloom.cogfoundry.ai/loom/v1'
     export LOOMLOOM_TOKEN_COGFOUNDRY='your-cogfoundry-api-key'
     ```
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
