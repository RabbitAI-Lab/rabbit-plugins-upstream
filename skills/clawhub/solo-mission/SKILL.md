---
name: solo-mission
description: >
  Use this skill for ANY interaction with the SOLO Mission Platform — creating missions,
  hiring humans, managing conversations, handling on-chain escrow (EscrowVault on Base
  Sepolia), recovering stuck funds, or operating as an autonomous agent on
  solomission.ai. Trigger on phrases like "create a mission", "browse humans",
  "hire a participant", "settle a mission", "claim refund", "emergency refund",
  "SOLO platform", or any mention of the SOLO Mission API.
  Also trigger when the user asks you to act as a SOLO agent, register an agent,
  or send USDC (Sepolia) rewards to participants.
license: MIT-0
compatibility: >
  Requires curl and jq. On-chain (USDC) missions additionally require Foundry cast and openssl.
metadata:
  author: SOLO Research Ltd.
  version: "1.0.0"
  openclaw:
    primaryEnv: SOLO_AGENT_KEY
---

# SOLO Mission Platform Skill

You are operating on the SOLO Mission Platform — a marketplace where AI agents hire
humans for tasks and pay them via on-chain escrow (EscrowVault, Base Sepolia) or
manual transfer.

## Private Key Security — MANDATORY

**NEVER ask for `PRIVATE_KEY` or any wallet secret through chat, messages, or any
conversation channel.**

Only check for `$PRIVATE_KEY` and `$WALLET_ADDRESS` when you are about to sign an
on-chain transaction — specifically before calling `approve()` or `createTask()` after
`create_mission` returns `funding_params`, or before any cancel/refund `cast send`.
The `create_mission` and `confirm_funding` API calls do not need them. If those
variables are missing when you reach a signing step, stop and send this exact message
to the operator:

> "On-chain transactions require `PRIVATE_KEY` and `WALLET_ADDRESS` to be set as
> environment variables before starting this session. Please configure them on the
> server and restart. Do not share the private key through chat."

Then halt — do not attempt to locate, decrypt, or request the key any other way.
Off-chain missions do not need these variables — proceed normally without them.

**API base URL:** `https://api.mission.projectsolo.ai`  
**Auth header:** `X-Agent-Key: $SOLO_AGENT_KEY` — required on every request except registration.

> **Only persist `mission_id` as the stable identifier.** Before every action, call
> `GET /agent/missions/:id` or the relevant params endpoint to get current values
> from the API. Every params endpoint (`cancel-params`, `emergency-refund-params`,
> `refund-params`) returns the exact `task_id` and `escrow_vault_address` you need
> for the on-chain call — use those, not anything cached locally.

---

## Reference Files

Load these only when the task requires them — do not load all at once:

| File | Load when… |
|---|---|
| `references/rest-api.md` | Looking up endpoint details, request/response shapes, filters, or error codes |
| `references/onchain.md` | Funding a mission, calling `createTask`, `cancelTask`, `emergencyRefund`, or `claimRefund` on EscrowVault |
| `references/stuck-recovery.md` | `settlement_deadline` passed without settlement, `settle_mission` returned `refundable`, or the Session-Start Scan found a mission outside your current state (`requires_sponsor_action` set) |
| `references/wallet-setup.md` | Creating an on-chain mission for the first time and no Sponsor wallet or signing tool is already available |

> **Media review missions** — if `type` is `media_review` on any mission, read the
> [Media Review Missions](#media-review-missions) section below before taking action.

---

## Onboarding — First-Time Setup

Run this section **only when no state file exists** (fresh start with no mission in
progress). If a state file is present, skip directly to
[Session Start](#session-start--always-do-this-first).

---

### Step 1 — Agent key

Check whether `$SOLO_AGENT_KEY` is set:

```bash
if [ -n "$SOLO_AGENT_KEY" ]; then
  # Verify it works
  CHECK=$(curl -s "https://api.mission.projectsolo.ai/agent/missions?limit=1" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY")
  if echo "$CHECK" | jq -e '.missions' > /dev/null 2>&1; then
    echo "Agent key valid."
  else
    echo "Agent key set but rejected — re-registering."
    unset SOLO_AGENT_KEY
  fi
fi

if [ -z "$SOLO_AGENT_KEY" ]; then
  # Ask for a name, then register
  # (prompt the operator): "What name should this agent use? (e.g. solo-agent)"
  AGENT_NAME="<operator answer>"
  REGISTER=$(curl -s -X POST https://api.mission.projectsolo.ai/agent/register \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"$AGENT_NAME\"}")
  SOLO_AGENT_KEY=$(echo $REGISTER | jq -r '.api_key')
  export SOLO_AGENT_KEY

  # Persist immediately — api_key is returned only once
  mkdir -p .claude
  SETTINGS=".claude/settings.local.json"
  if [ -f "$SETTINGS" ]; then
    TMP=$(mktemp)
    jq --arg k "$SOLO_AGENT_KEY" '.env.SOLO_AGENT_KEY = $k' "$SETTINGS" > "$TMP" \
      && mv "$TMP" "$SETTINGS"
  else
    jq -n --arg k "$SOLO_AGENT_KEY" '{env: {SOLO_AGENT_KEY: $k}}' > "$SETTINGS"
  fi
  echo "Agent registered and key saved. Do NOT print the key value in chat."
fi
```

`agent_id` format: `{name}-{8 hex chars}`. Note it — it appears in conversation IDs.

---

### Step 2 — Mission parameters

Ask the operator these questions **in order**, one at a time. Wait for each answer
before moving to the next. Do not assume defaults — confirm every field.

**Q1 — Goal**
> "What is the goal of this mission? Describe what you want hired humans to do."

Use the answer as the basis for `title` (≤ 100 chars, summarised) and `description`
(expand to ≤ 2000 chars with Markdown formatting: `## What I need`, `## Reward`).

**Q2 — Mission type**
> "What type of mission is this?"
>
> - `coffee_chat` — a 1:1 conversation or call (e.g. user interview, feedback session)
> - `opinion` — written opinion or short-form qualitative feedback
> - `survey` — structured answers to predefined questions
> - `general` — any open-ended task or deliverable
> - `media_review` — participants rate uploaded audio, images, or video (1–5 stars)

**Q3 — Reward type**
> "How do you want to pay participants?"
>
> - **Off-chain** — you pay manually after the mission settles; no crypto wallet needed now
> - **On-chain (USDC)** — automatic payout via EscrowVault smart contract on Base Sepolia; requires a funded Sponsor wallet and Foundry `cast`

**Q4 — Reward per participant**
> "How much should each participant receive? (e.g. '5 USDC')"

For on-chain missions, this becomes `reward_per_human` (whole USDC units). For
off-chain, it becomes the `reward_usdt` display reference.

**Q5 — Max participants**
> "How many participants do you want to hire at most? (e.g. 10)"

This sets `max_humans`. For on-chain missions this determines the required `budget` —
see the formula under [On-chain (with `budget` field)](#on-chain-with-budget-field).

**Q6 — Hiring window**
> "How long should the hiring window stay open? (e.g. '48 hours' — this is how long humans have to apply and be hired)"

For off-chain missions this maps to `expires_in_hours`. For on-chain it maps to
`hiring_duration_hours`.

**Q7 — Work duration (on-chain only)**
> "After the hiring window closes, how long do participants have to complete the work? (e.g. '72 hours')"

This is `work_duration_hours`. The settlement deadline = end of hiring window + work duration.
Settle at least 30 minutes before this deadline — plan accordingly.

After collecting all answers, **show a confirmation summary** before creating anything:

```
Mission Summary
───────────────────────────────
Goal:        <Q1 summary>
Type:        <Q2>
Reward:      <Q4> per person × <Q5> max = <total> (Q3: off-chain / on-chain)
Hiring:      <Q6>
Work window: <Q7 or "N/A for off-chain">
───────────────────────────────
Proceed? (yes / no / edit)
```

Do not call `create_mission` until the operator confirms.

---

### Step 3 — On-chain signing setup (on-chain only)

Skip this step entirely for off-chain missions.

**3a — Check Foundry `cast`**

```bash
if ! command -v cast > /dev/null 2>&1; then
  echo "Foundry cast not found. Install it with:"
  echo "  curl -L https://foundry.paradigm.xyz | bash && foundryup"
  echo "Then restart this session."
  exit 1
fi
cast --version
```

**3b — Check wallet env vars**

```bash
if [ -z "$WALLET_ADDRESS" ] || [ -z "$PRIVATE_KEY" ]; then
  cat <<'MSG'
On-chain missions require two environment variables set BEFORE this session starts.
Set them on the server (never paste them into chat):

  export WALLET_ADDRESS="0xYourSponsorWalletAddress"
  export PRIVATE_KEY="0xYourPrivateKey"

Then restart this session. If you need to create a new wallet, read:
  references/wallet-setup.md
MSG
  exit 1
fi
```

> **Security rule:** never ask the operator to type or paste `PRIVATE_KEY` in chat.
> If it is missing at this step, stop and show the message above — nothing else.

**3c — Check USDC balance**

```bash
USDC="0x036CbD53842c5426634e7929541eC2318f3dCF7e"
BALANCE_HEX=$(cast call $USDC "balanceOf(address)(uint256)" $WALLET_ADDRESS \
  --rpc-url https://sepolia.base.org 2>/dev/null)
# Convert 6-decimal raw amount to human USDC
BALANCE_USDC=$(echo "$BALANCE_HEX" | awk '{printf "%.2f", $1 / 1000000}')
REQUIRED=$(echo "<Q4_reward> * <Q5_max_humans>" | bc)

echo "Wallet: $WALLET_ADDRESS"
echo "USDC balance (Base Sepolia): $BALANCE_USDC"
echo "Required for this mission:   $REQUIRED"

if awk "BEGIN{exit !($BALANCE_USDC < $REQUIRED)}"; then
  echo "ERROR: Insufficient USDC. Top up the wallet before proceeding."
  echo "Faucet: https://faucet.circle.com (select Base Sepolia, USDC)"
  exit 1
fi
echo "Balance OK — proceeding."
```

**3d — Confirm wallet**

Show the operator:
> "Sponsor wallet: `$WALLET_ADDRESS`  
> Balance: `$BALANCE_USDC` USDC (Base Sepolia)  
> This wallet will sign all on-chain transactions. Confirm to continue."

Wait for confirmation before proceeding.

---

### Step 4 — Hand off

Once the operator confirms the summary (Step 2) and wallet (Step 3, if on-chain):

1. Proceed to [Creating a Mission](#creating-a-mission) with the collected parameters.
2. After the mission is created and state is written, jump to
   [Session Start](#session-start--always-do-this-first) Step 2 (stuck-mission scan)
   and then enter the monitoring loop.

---

## Session Start — Always Do This First

### Step 1 — Resume from state file

Before anything else, check whether a state file exists. The default path is
`./mission-state.json`; use `$STATE_FILE` if set.

```bash
STATE_FILE="${STATE_FILE:-./mission-state.json}"
if [ -f "$STATE_FILE" ]; then
  PHASE=$(jq -r '.phase' "$STATE_FILE")
  MISSION_ID=$(jq -r '.mission_id // empty' "$STATE_FILE")
  echo "Resuming: phase=$PHASE mission_id=${MISSION_ID:-none}"
  if [ "$PHASE" = "done" ] || [ "$PHASE" = "error" ]; then
    echo "Mission already in terminal phase=$PHASE — nothing to do."
    exit 0
  fi
else
  echo "No state file found — starting fresh."
fi
```

If resuming, jump directly to the appropriate phase in the
[Monitoring Loop](#monitoring-loop--state-machine) section without re-creating the mission.
Re-watch any `watched_conversations` and `watched_mission_id` recorded in the state file.

### Step 2 — Scan for stuck missions

Even when resuming, scan all missions for unresolved on-chain obligations:

```bash
PAGE=1
while true; do
  RESULT=$(curl -s "https://api.mission.projectsolo.ai/agent/missions?limit=100&page=$PAGE" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY")
  # Flagged by reconciler
  echo $RESULT | jq '.missions[] | select(.requires_sponsor_action != null) | {mission_id, requires_sponsor_action}'
  # Expired on-chain missions the reconciler hasn't flagged yet (up to 5-min lag)
  # "refundable" means settle_mission ran on-chain but Firestore write failed — treat same as stuck
  echo $RESULT | jq '.missions[] | select(.status == "expired" and .onchain_status != null and (.onchain_status == "funded" or .onchain_status == "qualified" or .onchain_status == "refundable")) | {mission_id, onchain_status}'
  HAS_NEXT=$(echo $RESULT | jq -r '.pagination.has_next')
  [ "$HAS_NEXT" = "true" ] || break
  PAGE=$((PAGE+1))
done
```

Resolve each result immediately before proceeding — read `references/stuck-recovery.md`
for exact steps. The reconciler has up to 5-minute lag; check `settlement_deadline`
directly on each mission doc rather than relying solely on the flag.

---

## State File

All session state must be persisted to a JSON file so that any interrupted session
can resume exactly where it left off. **Write the state file after every phase
transition and after every meaningful mutation** (new hire, new invite, etc.).

### Schema

```json
{
  "schema_version": 1,
  "phase": "idle",
  "mission_type": "general",
  "is_onchain": false,
  "mission_id": null,
  "watched_mission_id": null,
  "mission_status": null,
  "hiring_closes_at": null,
  "work_closes_at": null,
  "settlement_deadline": null,
  "expires_at": null,
  "qualified": false,
  "settled": false,
  "processed_uids": [],
  "hired_uids": [],
  "qualified_uids": [],
  "invited_uids": [],
  "watched_conversations": [],
  "conversations": {},
  "zero_rater_rounds": 0,
  "results": null,
  "config": {
    "min_rater_rating": 3.5,
    "invite_humans": false,
    "settle_buffer_secs": 1800,
    "wallet_address": null
  },
  "sub_log": [],
  "last_updated": "2026-01-01T00:00:00Z"
}
```

**Field notes:**
- `phase` — current state machine phase (see [Phase Reference](#phase-reference))
- `watched_mission_id` — mission ID currently registered with `watch_mission` (re-watch on resume)
- `watched_conversations` — list of conversation IDs to re-watch on resume
- `conversations` — per-conversation tracking object (see below)
- `zero_rater_rounds` — consecutive rounds with zero raters (`media_review` only)
- `results` — final output object written at `done` phase
- `expires_at` — ISO timestamp; set for off-chain missions from response.mission.expires_at
- `config.settle_buffer_secs` — how far before `settlement_deadline` to call settle (default 1800 = 30 min)
- `config.wallet_address` — Sponsor wallet address for on-chain `cast` calls; written during onboarding, read each tick instead of `$WALLET_ADDRESS` env var
- `qualified_uids` — for non-`media_review` missions: UIDs you explicitly qualify at finalize

**Per-conversation tracking** (keyed by `conversation_id`):
```json
{
  "uid": "<human_uid>",
  "fib_index": 0,
  "last_checked_at": null,
  "work_received": false,
  "follow_up_count": 0
}
```

### Atomic write pattern

Always write to a temp file then rename — this prevents corrupt state on interruption:

```bash
_write_state() {
  local TMP="${STATE_FILE}.tmp"
  # Pass updated JSON via stdin or argument
  jq --arg ts "$(date -u +%Y-%m-%dT%H:%M:%SZ)" '.last_updated = $ts' > "$TMP" \
    && mv "$TMP" "$STATE_FILE"
}

# Example: update phase
jq '.phase = "active_mission"' "$STATE_FILE" | _write_state
```

> **This function must be defined in the current shell before any monitoring loop code runs.** On fresh start the snippet above is executed once. On resume (script restart), source it from the same shell init or copy it verbatim at the top of your loop script before calling any phase handler.

### Phase reference

| Phase | Meaning | Default tick interval |
|---|---|---|
| `idle` | No active mission — create one | 5 s |
| `active_mission` | Mission live: hiring, conversations, monitoring deadlines | 60 s (120 s after 3 stable ticks) |
| `evaluating` | Mission settled — computing scores (`media_review` only) | 30 s |
| `done` | All work complete — close conversations, rate participants | terminal |
| `error` | Fatal error recorded in `sub_log` | 30 s then exit |

A "stable tick" is a loop iteration where nothing changed (no new applicants, no new
messages, no deadline crossed). After 3 consecutive stable ticks in `active_mission`,
extend the interval to 120 s to reduce API load.

---

## Creating a Mission

Two mission types: **off-chain** (manual payment, no escrow) and **on-chain**
(EscrowVault escrow, automated payout).

**Default to off-chain** unless the user explicitly asks for on-chain escrow,
automated payment, or mentions USDC escrow/EscrowVault. A reward described as
"1 USDC (Sepolia)" does not by itself mean on-chain — use off-chain with
`reward_usdt` as the reference amount.

**`type` must be one of:** `coffee_chat`, `opinion`, `survey`, `general`, `media_review`.

### Off-chain (no `budget` field)

```bash
MISSION=$(curl -s -X POST https://api.mission.projectsolo.ai/agent/missions \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{
    "type": "coffee_chat",
    "title": "Quick Chat: AI tools feedback",
    "description": "## What I need\n\nA **30-minute conversation** about AI tools.\n\n## Reward\n\n**20 USDC (Sepolia)** sent to your wallet on completion.",
    "requirements": { "skills": ["Software Development"], "languages": ["English"], "min_rating": 4.0 },
    "reward_usdt": 20,
    "max_humans": 3,
    "expires_in_hours": 48
  }')
MISSION_ID=$(echo $MISSION | jq -r '.mission.mission_id')
# status: "active" immediately
```

`reward_usdt` is a display-only reference — no escrow, no automatic payment. You pay
manually after settlement. Despite the field name, the actual currency is USDC (Sepolia).

**`auto_accept_applicants`** (optional, any mission type): when `true`, the platform
auto-hires applicants on apply — first-come first-served up to `max_humans`. No
`hire_participant` calls needed. Face verification is still required; on-chain missions
also require a bound Base wallet. Use for open `media_review` missions where you want
hands-off hiring:

```json
{
  "type": "media_review",
  "auto_accept_applicants": true,
  "max_humans": 20,
  "..."
}
```

### On-chain (with `budget` field)

```bash
MISSION=$(curl -s -X POST https://api.mission.projectsolo.ai/agent/missions \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{
    "type": "general",
    "title": "Data labelling task",
    "description": "## What I need\n\nLabel 50 images per batch.\n\n## Reward\n\n**5 USDC** per completion, paid automatically on Base.",
    "budget": 15.5,
    "max_humans": 3,
    "reward_per_human": 5,
    "hiring_duration_hours": 48,
    "work_duration_hours": 24
  }')
MISSION_ID=$(echo $MISSION | jq -r '.mission.mission_id')
# status: "pending_funding" — fund immediately
```

`budget` must satisfy `budget >= reward_per_human × max_humans + budget × platformFeeBps / 10000`
(`platformFeeBps` is currently `200`, i.e. 2% — the contract reserves this out of `budget`).
Add 3-5% headroom above `reward_per_human × max_humans` when picking `budget` — exact
equality is rejected with 400. Unused budget, including excess fee headroom, comes back
as `refundable_amount_raw` after `settle_mission`.

Both duration fields minimum 1 hour. Both `budget` and `reward_per_human` are in whole
USDC units — the backend converts them to `amount_raw` (6 decimals) in `funding_params`.
**Never pass `budget` directly to the contract** — always use `funding_params.amount_raw`.

After `create_mission`, **fund immediately** — `funding_params` expires in 1 hour.

### Funding sequence (Foundry `cast`)

See `references/onchain.md` for the full argument mapping. Quick reference:

```bash
# Read all fields from funding_params — never hardcode these
TASK_ID=$(echo $MISSION | jq -r '.funding_params.task_id')
TOKEN_ADDRESS=$(echo $MISSION | jq -r '.funding_params.token_address')
AMOUNT_RAW=$(echo $MISSION | jq -r '.funding_params.amount_raw')
BASE_POOL=$(echo $MISSION | jq -r '.funding_params.base_pool')
LOTTERY_REWARD_PER_WINNER=$(echo $MISSION | jq -r '.funding_params.lottery_reward_per_winner_raw // "0"')
LOTTERY_WINNER_COUNT=$(echo $MISSION | jq -r '.funding_params.lottery_winner_count // "0"')
QUALIFY_DEADLINE=$(echo $MISSION | jq -r '.funding_params.qualify_deadline')
SETTLEMENT_DEADLINE=$(echo $MISSION | jq -r '.funding_params.settlement_deadline')
SEED_COMMIT=$(echo $MISSION | jq -r '.funding_params.seed_commit')
ESCROW_VAULT_ADDRESS=$(echo $MISSION | jq -r '.funding_params.escrow_vault_address')
WALLET_ADDRESS=$(jq -r '.config.wallet_address' "$STATE_FILE")

NONCE=$(cast nonce $WALLET_ADDRESS --rpc-url https://sepolia.base.org)

# Step 1 — approve ERC20 spend (nonce N)
cast send $TOKEN_ADDRESS \
  "approve(address,uint256)" \
  $ESCROW_VAULT_ADDRESS $AMOUNT_RAW \
  --rpc-url https://sepolia.base.org \
  --private-key $PRIVATE_KEY \
  --nonce $NONCE

# Step 2 — create task (nonce N+1)
TX_HASH=$(cast send $ESCROW_VAULT_ADDRESS \
  "createTask(bytes32,address,uint96,uint96,uint96,uint16,uint64,uint64,bytes32)" \
  $TASK_ID $TOKEN_ADDRESS $AMOUNT_RAW $BASE_POOL \
  $LOTTERY_REWARD_PER_WINNER $LOTTERY_WINNER_COUNT \
  $QUALIFY_DEADLINE $SETTLEMENT_DEADLINE $SEED_COMMIT \
  --rpc-url https://sepolia.base.org \
  --private-key $PRIVATE_KEY \
  --nonce $((NONCE+1)) --json | jq -r '.transactionHash')

# Wait for receipt, then confirm
for i in $(seq 1 10); do
  S=$(cast receipt $TX_HASH --rpc-url https://sepolia.base.org --json 2>/dev/null | jq -r '.status // empty')
  [ "$S" = "1" ] && break; [ "$S" = "0" ] && echo "ERROR: createTask reverted" && exit 1; sleep 3
done
for ATTEMPT in 1 2 3; do
  R=$(curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/confirm-funding" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
    -d "{\"tx_hash\":\"$TX_HASH\"}")
  echo $R | jq -e '.success' > /dev/null && break; [ $ATTEMPT -lt 3 ] && sleep 5
done
```

> **Lost the tx hash?** Call `confirm_funding` with an empty body — the backend
> reads `EscrowVault.tasks(onchain_task_id)` directly and confirms if the task
> is funded on-chain.

> **`confirm_funding` returns 409 "On-chain task does not match..."?** The values
> actually passed to `createTask()` differ from `funding_params` — usually a
> hand-typed or re-derived value instead of one copied verbatim. The mission
> stays `pending_funding` forever under this `task_id`; **do not retry**. See
> the `confirm_funding` param-mismatch recovery in `references/stuck-recovery.md`
> (cancel on-chain to reclaim the escrow, then `create_mission` again).

**Field limits:** `title` ≤ 100 chars, `description` ≤ 2000 chars.

### After creating a mission — write state

After a successful `create_mission` (and `confirm_funding` for on-chain), write the
initial state before doing anything else:

```bash
jq -n \
  --arg phase "active_mission" \
  --arg mission_type "$MISSION_TYPE" \
  --argjson is_onchain "$IS_ONCHAIN" \
  --arg mission_id "$MISSION_ID" \
  --arg mission_status "active" \
  --arg hiring_closes_at "$(echo $MISSION | jq -r '.mission.hiring_closes_at // empty')" \
  --arg work_closes_at "$(echo $MISSION | jq -r '.mission.work_closes_at // empty')" \
  --argjson settlement_deadline "$(echo $MISSION | jq '.mission.settlement_deadline // null')" \
  --arg expires_at "$(echo $MISSION | jq -r '.mission.expires_at // empty')" \
  --arg wallet_address "${WALLET_ADDRESS:-}" \
  '{
    schema_version: 1,
    phase: $phase,
    mission_type: $mission_type,
    is_onchain: $is_onchain,
    mission_id: $mission_id,
    watched_mission_id: null,
    mission_status: $mission_status,
    hiring_closes_at: (if $hiring_closes_at == "" then null else $hiring_closes_at end),
    work_closes_at: (if $work_closes_at == "" then null else $work_closes_at end),
    settlement_deadline: $settlement_deadline,
    expires_at: (if $expires_at == "" then null else $expires_at end),
    qualified: false,
    settled: false,
    processed_uids: [],
    hired_uids: [],
    qualified_uids: [],
    invited_uids: [],
    watched_conversations: [],
    conversations: {},
    zero_rater_rounds: 0,
    results: null,
    config: {
      min_rater_rating: 3.5,
      invite_humans: false,
      settle_buffer_secs: 1800,
      wallet_address: $wallet_address
    },
    sub_log: [],
    last_updated: ""
  }' | _write_state
```

Then immediately call `watch_mission` and update `watched_mission_id` in the state file.

---

## After Publishing — Invite Humans

Do not wait for humans to find the mission. Proactively invite matching candidates.

1. Call `browse_humans` with filters matching mission `requirements`.
2. For each candidate (up to 10 per round):
   - Call `start_conversation` with a short invite and the mission link:
     `https://solomission.ai/missions/<mission_id>`
   - Immediately call `watch_conversation` with the returned `conversation_id`.
   - Write the `conversation_id` to `conversations` and `watched_conversations` in the state file.
   - Wait **6 seconds** between invites (write rate limit: 10 req/min → 1 per 6 s).
3. After 10 invites, fetch the next page and repeat until `max_humans` is reached.
4. Write all invited `human_uid`s to `invited_uids` in the state file — do not re-invite.

> **Re-invite caveat:** If `start_conversation` returns a conversation with
> `status: "archived"` or `"active"`, that human was already contacted.
> Check the `status` field before treating it as a new contact.

---

## Monitoring Loop — State Machine

This is the core loop that drives all missions to completion. Run it continuously
using `/loop 60s` (or `ScheduleWakeup`) while `phase !== 'done'`.

At the **start of every tick**, read the state file. At the **end of every tick**,
write any mutations back to the state file using the atomic write pattern.

```
idle ──────────────────────────────────────────────────────► active_mission
                                                                    │
                           ┌────────────────────────────────────────┘
                           │
                           ▼
                    active_mission ──────────────────────────────────────────► done
                           │                                                    ▲
                           │ (media_review only, on completed/refundable)       │
                           └──────────────────────► evaluating ─────────────────┘
```

Terminal states: `done`, `error` — stop the loop.

### Phase: idle

No active mission. Create one now. Follow [Creating a Mission](#creating-a-mission),
then write state and transition to `active_mission`.

### Phase: active_mission

Run every **60 s** (back off to **120 s** after 3+ consecutive stable ticks).
Execute each step in order; write state mutations before proceeding to the next step.

**Step 0 — Load state vars**

Run this at the top of every tick — do not use cached shell variables across ticks:

```bash
MISSION_ID=$(jq -r '.mission_id // empty' "$STATE_FILE")
IS_ONCHAIN=$(jq -r '.is_onchain' "$STATE_FILE")
MISSION_TYPE=$(jq -r '.mission_type' "$STATE_FILE")
MISSION_STATUS=$(jq -r '.mission_status // empty' "$STATE_FILE")
HIRING_CLOSES=$(jq -r '.hiring_closes_at // empty' "$STATE_FILE")
SDL=$(jq -r '.settlement_deadline // empty' "$STATE_FILE")
WALLET_ADDRESS=$(jq -r '.config.wallet_address // empty' "$STATE_FILE")
QUALIFIED=$(jq -r '.qualified' "$STATE_FILE")
SETTLED=$(jq -r '.settled' "$STATE_FILE")
```

**Step 1 — Emergency refund check (on-chain only)**

```bash
if [ "$IS_ONCHAIN" = "true" ] && [ -n "$SDL" ]; then
  NOW=$(date +%s)
  if [ "$NOW" -gt "$SDL" ]; then
    echo "settlement_deadline passed — triggering emergency refund"
    # Follow emergency refund flow in references/stuck-recovery.md
    jq '.phase = "done" | .mission_status = "cancelled"' "$STATE_FILE" | _write_state
    exit 0
  fi
fi
```

Act immediately — do not wait for `requires_sponsor_action` flag (up to 5-min lag).

**Step 2 — Process new applicants**

```bash
# One get_mission call covers all participants; average_rating is on the participant object
MISSION=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY")
PROCESSED=$(jq -r '.processed_uids[]' "$STATE_FILE")
MIN_RATING=$(jq -r '.config.min_rater_rating' "$STATE_FILE")

echo $MISSION | jq -c '.participants[] | select(.status == "applied")' | while read -r P; do
  UID=$(echo $P | jq -r '.uid')
  if echo "$PROCESSED" | grep -q "^$UID$"; then continue; fi

  # Read rating from the participant object — no extra API call needed
  RATING=$(echo $P | jq -r '.average_rating // 5')

  if awk "BEGIN{exit !(($RATING+0) >= ($MIN_RATING+0))}"; then
    curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/participants/$UID/hire" \
      -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
      -d "{}"
    jq --arg uid "$UID" '.hired_uids += [$uid] | .processed_uids += [$uid]' \
      "$STATE_FILE" | _write_state
  else
    curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/participants/$UID/reject" \
      -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
      -d "{\"reason\":\"Thank you for applying. We are looking for raters with a higher platform rating.\"}"
    jq --arg uid "$UID" '.processed_uids += [$uid]' "$STATE_FILE" | _write_state
  fi

  sleep 6  # 10 writes/min
done
```

**Step 3 — Invite humans (once, if configured)**

If `config.invite_humans` is `true` and `invited_uids` is empty, run the invite flow
from [After Publishing — Invite Humans](#after-publishing--invite-humans) once per mission.
Write `invited_uids` and `conversations` to state immediately after each invite.

**Step 4 — Monitor conversations (Fibonacci schedule)**

Poll each conversation in `conversations` according to its `fib_index`. Skip the check
if `now - last_checked_at < FIB[fib_index]` seconds.

On each check: call `GET /agent/conversations/:id/messages?since=<last_checked_at>`
(REST) or `get_pending_messages` (MCP). Then:

- **New human message** → reset `fib_index` to 0 for this conversation, respond (see
  [Responding to Messages](#responding-to-messages)), update `last_checked_at`.
- **No new messages** → advance `fib_index` by 1 (capped at 14), update `last_checked_at`.
- **Work submitted** (non-`media_review`) → set `work_received: true` on the conversation,
  acknowledge, write state.
- **Idle for 3+ unanswered follow-ups** → archive the conversation with `action: "archive"`.

```bash
_poll_conversation() {
  local CONV_ID=$1
  local FIB_IDX=$(jq -r --arg id "$CONV_ID" '.conversations[$id].fib_index // 0' "$STATE_FILE")
  local LAST=$(jq -r --arg id "$CONV_ID" '.conversations[$id].last_checked_at // empty' "$STATE_FILE")
  local FIB_SECS
  FIB_SECS=$(echo "1 1 2 3 5 8 13 21 34 55 89 144 233 377 600" | tr ' ' '\n' | sed -n "$((FIB_IDX+1))p")
  local NOW=$(date +%s)

  if [ -n "$LAST" ]; then
    local LAST_S=$(date -d "$LAST" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$LAST" +%s)
    if [ $((NOW - LAST_S)) -lt "$FIB_SECS" ]; then return; fi
  fi

  local QS=""
  [ -n "$LAST" ] && QS="?since=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$LAST'))")"
  MSGS=$(curl -s "https://api.mission.projectsolo.ai/agent/conversations/$CONV_ID/messages$QS" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY")

  local HUMAN_COUNT
  HUMAN_COUNT=$(echo $MSGS | jq '[.messages[] | select(.sender_type != "agent")] | length')
  local NOW_ISO=$(date -u +%Y-%m-%dT%H:%M:%SZ)

  if [ "$HUMAN_COUNT" -gt 0 ]; then
    NEW_IDX=0  # reset on activity
  else
    NEW_IDX=$((FIB_IDX < 14 ? FIB_IDX + 1 : 14))  # advance on silence
  fi

  jq --arg id "$CONV_ID" --argjson idx "$NEW_IDX" --arg ts "$NOW_ISO" \
    '.conversations[$id].fib_index = $idx | .conversations[$id].last_checked_at = $ts' \
    "$STATE_FILE" | _write_state

  # Return messages for the caller to handle
  echo $MSGS
}
```

**Fibonacci delay sequence** (seconds):

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Delay (s) | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 | 89 | 144 | 233 | 377 | 600 |

Start at index 0 (1 s). Reset to 0 on any new human message. Advance by 1 on silence.
Cap at index 14 (600 s = 10 min).

**Step 5 — Finalize qualification**

```bash
NOW=$(date +%s)

if [ "$QUALIFIED" = "false" ]; then
  SHOULD_FINALIZE=false

  if [ "$IS_ONCHAIN" = "true" ] && [ -n "$HIRING_CLOSES" ]; then
    # On-chain: finalize only after qualify_deadline (contract enforces this)
    HIRING_CLOSES_S=$(date -d "$HIRING_CLOSES" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$HIRING_CLOSES" +%s 2>/dev/null)
    [ -n "$HIRING_CLOSES_S" ] && [ "$NOW" -ge "$HIRING_CLOSES_S" ] && SHOULD_FINALIZE=true
  elif [ "$IS_ONCHAIN" = "false" ]; then
    # Off-chain: finalize once qualified_uids is non-empty, or when approaching expires_at
    EXPIRES_AT=$(jq -r '.expires_at // empty' "$STATE_FILE")
    QUALIFIED_COUNT=$(jq '.qualified_uids | length' "$STATE_FILE")
    if [ "$QUALIFIED_COUNT" -gt 0 ]; then
      SHOULD_FINALIZE=true
    elif [ -n "$EXPIRES_AT" ]; then
      EXPIRES_S=$(date -d "$EXPIRES_AT" +%s 2>/dev/null || date -j -f "%Y-%m-%dT%H:%M:%SZ" "$EXPIRES_AT" +%s 2>/dev/null)
      SETTLE_BUFFER=$(jq -r '.config.settle_buffer_secs // 1800' "$STATE_FILE")
      [ -n "$EXPIRES_S" ] && [ "$NOW" -ge "$((EXPIRES_S - SETTLE_BUFFER))" ] && SHOULD_FINALIZE=true
    fi
  fi

  if [ "$SHOULD_FINALIZE" = "true" ]; then
    if [ "$MISSION_TYPE" = "media_review" ]; then
      BODY='{}'
    else
      QUALIFIED_UIDS=$(jq -c '.qualified_uids' "$STATE_FILE")
      BODY="{\"qualified_human_uids\":$QUALIFIED_UIDS}"
    fi

    R=$(curl -s -X POST \
      "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/finalize-qualification" \
      -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
      -d "$BODY")
    HTTP_STATUS=$(echo $R | jq -r '.http_status // .status_code // empty')
    if echo $R | jq -e '.success' > /dev/null 2>&1 || echo $R | jq -e '.mission' > /dev/null 2>&1; then
      jq '.qualified = true' "$STATE_FILE" | _write_state
    elif [ "$HTTP_STATUS" = "409" ] || echo $R | jq -e '.error | type == "string" and contains("already")' > /dev/null 2>&1; then
      jq '.qualified = true' "$STATE_FILE" | _write_state  # already finalized
    fi
  fi
fi
```

> **`finalize_qualification` requires `qualify_deadline` passed on on-chain missions.**
> Off-chain missions: call any time after all hired participants have submitted work.
> For `media_review`: pass `{}` — `qualified_human_uids` is ignored.

**Step 6 — Settle mission**

```bash
NOW=$(date +%s)
SETTLED=$(jq -r '.settled' "$STATE_FILE")
QUALIFIED=$(jq -r '.qualified' "$STATE_FILE")
SETTLE_BUFFER=$(jq -r '.config.settle_buffer_secs // 1800' "$STATE_FILE")
SDL=$(jq -r '.settlement_deadline // empty' "$STATE_FILE")
MISSION_STATUS=$(jq -r '.mission_status // empty' "$STATE_FILE")

# On-chain: settle at least settle_buffer_secs before the deadline
# Off-chain: settle any time after qualified
SHOULD_SETTLE=false
if [ "$IS_ONCHAIN" = "true" ] && [ -n "$SDL" ]; then
  [ "$NOW" -ge "$((SDL - SETTLE_BUFFER))" ] && SHOULD_SETTLE=true
elif [ "$IS_ONCHAIN" = "false" ]; then
  [ "$QUALIFIED" = "true" ] && SHOULD_SETTLE=true
fi

if [ "$SETTLED" = "false" ] && [ "$QUALIFIED" = "true" ] && [ "$SHOULD_SETTLE" = "true" ] && \
   [ "$MISSION_STATUS" != "completed" ] && [ "$MISSION_STATUS" != "refundable" ] && \
   [ "$MISSION_STATUS" != "refunded" ]; then

  SETTLE_R=$(curl -s -X POST \
    "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/settle" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" -d '{}')
  NEW_STATUS=$(echo $SETTLE_R | jq -r '.mission.status // empty')

  if [ -z "$NEW_STATUS" ]; then
    echo "ERROR: settle_mission returned no status — not writing settled=true, will retry next tick"
  else
    # On-chain + refundable: claim unused budget BEFORE writing settled=true
    if [ "$IS_ONCHAIN" = "true" ] && [ "$NEW_STATUS" = "refundable" ]; then
      REFUND=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/refund-params" \
        -H "X-Agent-Key: $SOLO_AGENT_KEY")
      TASK_ID=$(echo $REFUND | jq -r '.refund_params.task_id')
      VAULT=$(echo $REFUND | jq -r '.refund_params.escrow_vault_address')
      TX_HASH=$(cast send $VAULT "claimRefund(bytes32,address)" $TASK_ID $WALLET_ADDRESS \
        --rpc-url https://sepolia.base.org --private-key $PRIVATE_KEY --json | jq -r '.transactionHash')
      REFUND_OK=false
      for i in $(seq 1 10); do
        S=$(cast receipt $TX_HASH --rpc-url https://sepolia.base.org --json 2>/dev/null | jq -r '.status // empty')
        if [ "$S" = "1" ]; then REFUND_OK=true; break; fi
        [ "$S" = "0" ] && echo "ERROR: claimRefund reverted" && break
        sleep 3
      done
      if [ "$REFUND_OK" = "true" ]; then
        for ATTEMPT in 1 2 3; do
          R=$(curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/confirm-refund" \
            -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
            -d "{\"tx_hash\":\"$TX_HASH\"}")
          echo $R | jq -e '.success' > /dev/null && break; [ $ATTEMPT -lt 3 ] && sleep 5
        done
        NEW_STATUS="refunded"
      else
        echo "claimRefund failed — will retry next tick (settled=true not written yet)"
      fi
    fi

    # Write settled=true only after refund is confirmed (or not needed for this mission)
    if [ "$IS_ONCHAIN" = "false" ] || [ "$NEW_STATUS" != "refundable" ]; then
      jq --arg s "$NEW_STATUS" '.settled = true | .mission_status = $s' "$STATE_FILE" | _write_state
    fi
  fi
fi
```

**Do not defer `claimRefund()` to a later tick.** Unused budget sits locked in
EscrowVault until you call it. Execute within the same tick that detect `refundable`.

**Step 7 — Phase transition**

```bash
CURRENT_STATUS=$(jq -r '.mission_status' "$STATE_FILE")

case "$CURRENT_STATUS" in
  completed|refunded)
    if [ "$MISSION_TYPE" = "media_review" ]; then
      jq '.phase = "evaluating"' "$STATE_FILE" | _write_state
    else
      jq '.phase = "done"' "$STATE_FILE" | _write_state
    fi
    ;;
  refundable)
    # claimRefund not yet confirmed — Step 6 will retry on the next tick
    echo "Mission still refundable — claimRefund pending, retrying next tick"
    ;;
  cancelled|expired)
    jq '.phase = "done"' "$STATE_FILE" | _write_state
    ;;
esac
```

### Phase: evaluating (media_review only)

Run every **30 s** until scores are computed or zero-rater limit is reached.

**Step 1 — Fetch tracks**

```bash
TRACKS=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/tracks" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY")
TOTAL_VOTES=$(echo $TRACKS | jq '[.tracks[].vote_counts.total] | add // 0')
```

**Step 2 — Handle zero raters**

```bash
if [ "$TOTAL_VOTES" -eq 0 ]; then
  ROUNDS=$(($(jq -r '.zero_rater_rounds' "$STATE_FILE") + 1))
  jq --argjson r "$ROUNDS" '.zero_rater_rounds = $r' "$STATE_FILE" | _write_state

  if [ "$ROUNDS" -ge 3 ]; then
    # Give up — three consecutive rounds with no raters
    jq '.phase = "done"' "$STATE_FILE" | _write_state
    echo "Zero raters after $ROUNDS rounds — giving up."
  else
    # Claim refund for the prior on-chain mission before resetting state
    ZR_IS_ONCHAIN=$(jq -r '.is_onchain' "$STATE_FILE")
    ZR_STATUS=$(jq -r '.mission_status // empty' "$STATE_FILE")
    ZR_MISSION_ID=$(jq -r '.mission_id // empty' "$STATE_FILE")
    ZR_WALLET=$(jq -r '.config.wallet_address // empty' "$STATE_FILE")
    if [ "$ZR_IS_ONCHAIN" = "true" ] && [ "$ZR_STATUS" = "refundable" ] && [ -n "$ZR_MISSION_ID" ] && [ -n "$ZR_WALLET" ]; then
      REFUND=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$ZR_MISSION_ID/refund-params" \
        -H "X-Agent-Key: $SOLO_AGENT_KEY")
      ZR_TASK_ID=$(echo $REFUND | jq -r '.refund_params.task_id')
      ZR_VAULT=$(echo $REFUND | jq -r '.refund_params.escrow_vault_address')
      TX_HASH=$(cast send $ZR_VAULT "claimRefund(bytes32,address)" $ZR_TASK_ID $ZR_WALLET \
        --rpc-url https://sepolia.base.org --private-key $PRIVATE_KEY --json | jq -r '.transactionHash')
      for i in $(seq 1 10); do
        S=$(cast receipt $TX_HASH --rpc-url https://sepolia.base.org --json 2>/dev/null | jq -r '.status // empty')
        [ "$S" = "1" ] && break; [ "$S" = "0" ] && echo "claimRefund reverted (may already be claimed)" && break; sleep 3
      done
      for ATTEMPT in 1 2 3; do
        R=$(curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$ZR_MISSION_ID/confirm-refund" \
          -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
          -d "{\"tx_hash\":\"$TX_HASH\"}")
        echo $R | jq -e '.success' > /dev/null && break; [ $ATTEMPT -lt 3 ] && sleep 5
      done
      echo "Refund claimed for zero-rater mission $ZR_MISSION_ID"
    fi

    # Reset mission fields — keep zero_rater_rounds and config (including wallet_address)
    # is_onchain resets to false; onboarding will re-ask reward type for the next run
    jq '
      .phase = "idle" |
      .is_onchain = false |
      .mission_id = null |
      .watched_mission_id = null |
      .mission_status = null |
      .hiring_closes_at = null |
      .work_closes_at = null |
      .settlement_deadline = null |
      .expires_at = null |
      .qualified = false |
      .settled = false |
      .processed_uids = [] |
      .hired_uids = [] |
      .qualified_uids = [] |
      .invited_uids = [] |
      .watched_conversations = [] |
      .conversations = {}
    ' "$STATE_FILE" | _write_state
    echo "Zero raters round $ROUNDS — resetting to idle to re-post same files."
  fi
  exit 0
fi
```

**Step 3 — Compute scores and write results**

```bash
# Weighted average star rating (1–5) per track → normalize to 0–100
RESULTS=$(echo $TRACKS | jq '[.tracks[] | {
  track_id,
  title,
  total_votes: .vote_counts.total,
  score: (
    if .vote_counts.total == 0 then 0
    else (
      (.vote_counts."1" * 1 +
       .vote_counts."2" * 2 +
       .vote_counts."3" * 3 +
       .vote_counts."4" * 4 +
       .vote_counts."5" * 5) / .vote_counts.total
    ) | (. - 1) / 4 * 100 | round
    end
  )
}] | sort_by(-.score)')

WINNER=$(echo $RESULTS | jq '.[0]')
WINNER_TITLE=$(echo $WINNER | jq -r '.title')
WINNER_SCORE=$(echo $WINNER | jq -r '.score')

jq --argjson results "$RESULTS" --argjson winner "$WINNER" \
  '.results = {scores: $results, winner: $winner} | .phase = "done"' \
  "$STATE_FILE" | _write_state

echo "Evaluation complete — winner: $WINNER_TITLE (score=$WINNER_SCORE/100)"
```

**Score formula:** weighted star average normalized to 0–100.
`score = ((1*c1 + 2*c2 + 3*c3 + 4*c4 + 5*c5) / total - 1) / 4 * 100`

For richer scoring, call `GET /agent/missions/:id/tracks/:tid/ratings` to get
`total_listen_seconds` per participant and factor in engagement depth (see
[Engagement scoring](#step-5--monitor-progress)).

### Phase: done

Execute in order, then stop the loop:

1. **Close all open conversations:**
   ```bash
   jq -r '.watched_conversations[]' "$STATE_FILE" | while read -r CONV_ID; do
     curl -s -X POST "https://api.mission.projectsolo.ai/agent/conversations/$CONV_ID/close" \
       -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" -d '{}'
   done
   ```

2. **Rate participants** (within 7 days of `completed_at`):
   ```bash
   jq -r '.hired_uids[]' "$STATE_FILE" | while read -r UID; do
     curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/participants/$UID/comment" \
       -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
       -d "{\"rating\":5,\"comment\":\"Clear communication and delivered on time.\"}"
   done
   ```

3. **Print results** (media_review):
   ```bash
   jq '.results' "$STATE_FILE"
   ```

4. **Stop the loop** — do not reschedule.

---

## Rate Limits and Backoff

| Type | Limit |
|---|---|
| Read (browse, list, get) | 60 req / min per IP |
| Write (create, send, hire) | 10 req / min per IP |

Space out write operations — one invite per 6 seconds maximum.

### 429 Exponential Backoff

On any HTTP 429 response, retry up to 4 times with exponential delay:

| Retry | Delay before retry |
|---|---|
| 1st | 20 s |
| 2nd | 40 s |
| 3rd | 80 s |
| 4th | 160 s |

After 4 failures, propagate the error — the outer loop will retry on the next tick.
If a 429 hits during a loop tick (not a specific operation), back off the entire tick
by 60 s before continuing.

```bash
_api_with_retry() {
  local CMD="$@"
  local DELAY=20
  for ATTEMPT in 0 1 2 3; do
    RESULT=$(eval "$CMD")
    if echo "$RESULT" | grep -q '"429"'; then
      [ $ATTEMPT -eq 3 ] && echo "ERROR: 429 after 4 attempts" && return 1
      echo "429 — retrying in ${DELAY}s"
      sleep $DELAY
      DELAY=$((DELAY * 2))
    else
      echo "$RESULT"
      return 0
    fi
  done
}
```

---

## Hiring Participants

When a human applies:
1. Call `get_mission` to see applicants and their `uid`.
2. Optionally call `get_human_profile` — check `average_rating >= min_rater_rating` (default 3.5).
3. Call `hire_participant` to accept — they can now start work.
4. Call `reject_participant` for applicants you don't want, with a polite reason.

Write `processed_uids` and `hired_uids` to state after each decision.

You may also reject a hired participant before calling `finalize_qualification` if
their work falls short. Remove them from `hired_uids` in state.

**If no participants deserve to qualify:** do not call `finalize_qualification` with
an empty list — the backend will reject it. Instead reject all hired participants,
then cancel the mission:

- **Off-chain:** `POST /agent/missions/$MISSION_ID/cancel` with no body — cancels directly, no contract interaction needed.

- **On-chain:** Let the API responses drive the flow — do not manually compute deadlines.

  **Step 1 — try cancel-params:**
  ```bash
  CANCEL=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/cancel-params" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY")
  ```
  - If `success: true` → hiring window is still open. Run `cancelTask()` then `confirm-cancel`:
    ```bash
    TASK_ID=$(echo $CANCEL | jq -r '.cancel_params.task_id')
    VAULT=$(echo $CANCEL | jq -r '.cancel_params.escrow_vault_address')
    TX_HASH=$(cast send $VAULT "cancelTask(bytes32)" $TASK_ID \
      --rpc-url https://sepolia.base.org --private-key $PRIVATE_KEY --json | jq -r '.transactionHash')
    for i in $(seq 1 10); do
      S=$(cast receipt $TX_HASH --rpc-url https://sepolia.base.org --json 2>/dev/null | jq -r '.status // empty')
      [ "$S" = "1" ] && break; [ "$S" = "0" ] && echo "ERROR: cancelTask reverted" && exit 1; sleep 3
    done
    for ATTEMPT in 1 2 3; do
      R=$(curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/confirm-cancel" \
        -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
        -d "{\"tx_hash\":\"$TX_HASH\"}")
      echo $R | jq -e '.success' > /dev/null && break; [ $ATTEMPT -lt 3 ] && sleep 5
    done
    ```
  - If `error: "qualify_deadline_passed"` → hiring window is closed. Proceed to Step 2.

  **Step 2 — try emergency-refund-params:**
  ```bash
  EREFUND=$(curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/emergency-refund-params" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY")
  ```
  - If `eligible: true` → settlement deadline has passed. Run `emergencyRefund()` then `confirm-emergency-refund`:
    ```bash
    TASK_ID=$(echo $EREFUND | jq -r '.emergency_refund_params.task_id')
    VAULT=$(echo $EREFUND | jq -r '.emergency_refund_params.escrow_vault_address')
    TX_HASH=$(cast send $VAULT "emergencyRefund(bytes32)" $TASK_ID \
      --rpc-url https://sepolia.base.org --private-key $PRIVATE_KEY --json | jq -r '.transactionHash')
    for i in $(seq 1 10); do
      S=$(cast receipt $TX_HASH --rpc-url https://sepolia.base.org --json 2>/dev/null | jq -r '.status // empty')
      [ "$S" = "1" ] && break; [ "$S" = "0" ] && echo "ERROR: emergencyRefund reverted" && exit 1; sleep 3
    done
    for ATTEMPT in 1 2 3; do
      R=$(curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/confirm-emergency-refund" \
        -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
        -d "{\"tx_hash\":\"$TX_HASH\"}")
      echo $R | jq -e '.success' > /dev/null && break; [ $ATTEMPT -lt 3 ] && sleep 5
    done
    ```
  - If `eligible: false, reason: "settlement_deadline_not_passed"` → between deadlines.
    The response includes `retry_after` (ISO timestamp). Write it to state and check again when that time passes.

---

## Mission Completion

### On-chain flow

```
create_mission → confirm_funding → hire_participant(s) →
finalize_qualification → settle_mission → confirm_refund (if status="refundable") → rate_participant(s)
```

`confirm_refund` is a mandatory immediate step when settle returns `status: "refundable"` —
execute within the same loop tick.

### Off-chain flow

```
create_mission → hire_participant(s) → finalize_qualification →
settle_mission → manual payment → rate_participant(s)
```

`settle_mission` requires the mission to be in `qualifying` status (i.e.,
`finalize_qualification` must be called first — returns 409 otherwise).

### Responding to messages

For all non-`media_review` mission types, participants deliver work via conversation.
When a hired participant sends a message:

- **Work submitted:** Respond immediately:
  > "Thank you for your submission! I've received your [work].
  > I'll review it and finalize payments once all submissions are assessed."
  
  Set `work_received: true` on the conversation in state.
  Add the participant's `uid` to `qualified_uids` in state if work meets requirements.

- **Question about the mission:** Answer it directly.

- **Idle after 3+ follow-up messages with no reply:** Archive the conversation —
  `close_conversation` with `action: "archive"`.

Do not call `finalize_qualification` until all hired participants have submitted
(or the deadline is approaching). For non-`media_review` missions, pass `qualified_uids`
from state as `qualified_human_uids`.

### On-chain deadline reference

| Deadline field | What to do |
|---|---|
| `hiring_closes_at` passed | Call `finalize_qualification` |
| 30 min before `work_closes_at` / `settlement_deadline` | Call `finalize_qualification` (if not done), then `settle_mission` |
| `settle_mission` returns `status: "refundable"` | Immediately `claimRefund()` + `confirm-refund` |
| `settlement_deadline` passed unsettled | Emergency refund immediately |

---

## Media Review Missions

A **media_review mission** (`type: "media_review"`) lets agents upload media items — audio tracks, images, or short videos — and collect structured human feedback. Hired participants review each item and submit a 1–5 star rating with an optional comment.

**Critical ordering rule:** the track list must be fully uploaded and confirmed **before**
any participant is hired. Once hiring starts, uploads are blocked. This ensures every
hired participant sees the same complete set of tracks.

---

### Step 1 — Create the mission

**Off-chain** (no escrow, manual payment):
```bash
MISSION=$(curl -s -X POST https://api.mission.projectsolo.ai/agent/missions \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{
    "type": "media_review",
    "title": "Rate these AI-generated tracks",
    "description": "## What I need\n\nListen to each track and give a rating.\n\n## Reward\n\n**5 USDC (Sepolia)** sent on completion.",
    "reward_usdt": 5,
    "max_humans": 20,
    "expires_in_hours": 72
  }')
MISSION_ID=$(echo $MISSION | jq -r '.mission.mission_id')
# status: "active" immediately
```

**On-chain** (USDC escrow, automated payout):
```bash
MISSION=$(curl -s -X POST https://api.mission.projectsolo.ai/agent/missions \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{
    "type": "media_review",
    "title": "Rate these AI-generated tracks",
    "description": "## What I need\n\nListen to each track and give a rating.\n\n## Reward\n\n**1 USDC** paid automatically on completion.",
    "budget": 20.5,
    "max_humans": 20,
    "reward_per_human": 1,
    "hiring_duration_hours": 48,
    "work_duration_hours": 72
  }')
MISSION_ID=$(echo $MISSION | jq -r '.mission.mission_id')
# status: "pending_funding" — do NOT fund yet, upload tracks first
```

---

### Step 2 — Upload all media items

**Do this before funding (on-chain) or before inviting anyone (off-chain).**

Upload each item in three steps: get a signed URL → PUT the file → confirm.

**Format rules (mobile-compatible only — iOS + Android):**

| Type | Allowed MIME types | Max size | Notes |
|---|---|---|---|
| Audio | `audio/mpeg` (MP3), `audio/mp4` (AAC/M4A) | 25 MB | Re-encode at 128–192 kbps if larger |
| Image | `image/jpeg`, `image/png`, `image/webp` | 10 MB | |
| Video | `video/mp4` | 200 MB | Must be faststart-encoded (moov atom first) for partial play |

- **Not allowed:** OGG (no iOS Safari), WAV (uncompressed), MOV (no Android), WebM (no iOS Safari)
- **Up to:** 20 items per mission

```bash
upload_item() {
  local FILE=$1 TITLE=$2 CONTENT_TYPE=$3 DURATION=$4
  # 1. Get signed URL
  UPLOAD=$(curl -s -X POST \
    "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/tracks/upload-url" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
    -d "{\"title\":\"$TITLE\",\"content_type\":\"$CONTENT_TYPE\"}")
  UPLOAD_URL=$(echo $UPLOAD | jq -r '.upload_url')
  TRACK_ID=$(echo $UPLOAD | jq -r '.track_id')

  # 2. PUT file directly to storage (signed URL expires in 15 min)
  curl -s -X PUT "$UPLOAD_URL" \
    -H "Content-Type: $CONTENT_TYPE" --data-binary @"$FILE"

  # 3. Confirm — validates size, sets upload_status:'ready'
  BODY="{\"title\":\"$TITLE\"}"
  [ -n "$DURATION" ] && BODY="{\"title\":\"$TITLE\",\"duration_seconds\":$DURATION}"
  curl -s -X POST \
    "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/tracks/$TRACK_ID/confirm" \
    -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
    -d "$BODY"
}

upload_item track1.mp3  "Track 1"  "audio/mpeg" 183
upload_item cover.jpg   "Cover Art" "image/jpeg"
# ... repeat for all items
```

> If the upload URL times out (15 min), call upload-url again — it creates a new
> pending doc. The old pending doc stays but does no harm; delete it with
> `DELETE /agent/missions/:id/tracks/:tid` if desired.

**On-chain only:** fund the mission after all tracks are uploaded:
```bash
# createTask() on-chain via cast (see references/onchain.md), then:
curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/confirm-funding" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{"tx_hash":"<TX_HASH>"}'
# status: "active" now — participants can apply
```

---

### Step 3 — Invite and hire participants

Same as any mission. Participants see the track list immediately after being hired.
See the regular hiring flow in [After Publishing — Invite Humans](#after-publishing--invite-humans).

---

### Step 4 — What participants experience (platform handles automatically)

Each hired participant opens the mission page and sees the media items. The platform records:

1. **Engagement sessions** — recorded automatically as the participant listens/views each item.
   Sent to `POST /missions/:id/tracks/:tid/play-session`. The agent does **not** trigger this.

2. **Ratings** — the participant selects 1–5 stars per item via `POST /missions/:id/tracks/:tid/vote`.
   This is what counts toward `review_progress`.

A participant's review is **complete** (`review_progress.completed_at` set) once they have
rated every ready track.

> **Mission deadline:** votes are blocked once `hiring_closes_at` has passed. Participants
> who haven't finished by then cannot be auto-qualified. **Do not call
> `finalize_qualification` until you have confirmed all participants have
> `review_progress.completed_at` set — or the deadline has genuinely passed.**

---

### Step 5 — Monitor progress

Poll `get_mission` to track completion per participant:

```bash
curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" \
  | jq '.participants[] | {uid, status, rated: .review_progress.rated_track_ids | length, done: (.review_progress.completed_at != null)}'
```

When `done: true`, acknowledge:
> "Thanks for reviewing all the items! Your feedback is recorded and payment will process at the deadline."

Check item scores at any time:
```bash
curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/tracks" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" \
  | jq '.tracks[] | {title, vote_counts}'
```

`vote_counts` gives a `{1,2,3,4,5,total}` star distribution. For richer analysis,
get per-participant engagement:
```bash
curl -s "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/tracks/$TRACK_ID/ratings" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY"
# → [{uid, rating, comment, total_listen_seconds, rated_at}]
```

Use `total_listen_seconds` with `track_duration_seconds` to weight engagement:

| Engagement | Weight |
|---|---|
| Listened > once (replayed) | 1.2× |
| ≥ 80 % listened | 1.0× |
| 40–79 % listened | 0.7× |
| < 40 % (early bail) | 0.3× |

---

### Step 6 — Finalize and settle

For `media_review`, `finalize-qualification` **ignores** any `qualified_human_uids` you pass.
It auto-qualifies every hired participant whose `review_progress.completed_at` is set.

```bash
curl -s -X POST "https://api.mission.projectsolo.ai/agent/missions/$MISSION_ID/finalize-qualification" \
  -H "X-Agent-Key: $SOLO_AGENT_KEY" -H "Content-Type: application/json" \
  -d '{}'
```

Then settle as normal (see [Phase: active_mission Step 6](#phase-active_mission)).
After settlement the loop transitions to `evaluating`.

---

### Complete flow reference

| Step | On-chain | Off-chain |
|---|---|---|
| 1. Create | `pending_funding` | `active` |
| 2. Upload tracks | During `pending_funding` | During `active`, **before first hire** |
| 3. Fund | `createTask()` → `confirm_funding` → `active` | N/A |
| 4. Invite + hire | During `active` | During `active` |
| 5. Participants play + vote | Platform records automatically | Same |
| 6. Finalize | After `hiring_closes_at` | Any time after deadline |
| 7. Settle | ≥30 min before `settlement_deadline` | Any time after finalize |
| 8. Evaluate | Loop phase `evaluating` | Same |
| 9. Rate participants | Within 7 days of `completed_at` | Same |

---

### Zero-participant outcome

If the mission closes with no completed ratings — all tracks have zero votes — treat
it as a no-data round:

- **Do not advance the iteration counter.** There is no score to refine from.
- **Do not regenerate media.** The items are still valid; the problem is visibility.
- The mission will be `refundable` — claim the full budget (on-chain) then re-create
  the mission with the **same files**.
- Track `zero_rater_rounds` in the state file. After **3 consecutive rounds**, transition
  to `done` with no result to avoid looping indefinitely.

---

## Conversation Management

**States:** `active` → `archived` (soft, reopenable) → `closed` (terminal).

- After mission completes or cancels: linked conversations auto-close. No action needed.
- Idle conversation (no reply after 3 follow-up messages): archive it —
  `close_conversation` with `action: "archive"`.
- Objective met: close it — `close_conversation` with `action: "close"`.
- To focus: list only `active` conversations.
- To resume: reopen with `action: "reopen"`.

**Re-watching on session resume:** On startup, call `watch_conversation` for every
`conversation_id` in `watched_conversations` in the state file before entering the loop.

**Message polling (no persistent MCP session):** Call
`GET /agent/conversations/:id/messages?since=<last_checked_at>` on the Fibonacci delay
schedule from the state file. See the [Fibonacci delay sequence](#fibonacci-delay-sequence)
table above.

---

## Rating Participants

Call `rate_participant` after the mission settles.

```json
{ "rating": 5, "comment": "Clear communication and delivered on time." }
```

Constraints: participant must be `qualified` or `rewarded`; mission must be in a
settled state (`completed`, `refundable`, or `refunded`); must be called within
**7 days** of `mission.completed_at`.

---

## Mission Status Reference

```
pending_funding → active → qualifying → completed
                                      ↘ refundable → refunded
                ↘ cancelled  (cancelTask or emergencyRefund)
                ↘ expired    (settlement_deadline passed, no action)
```

## Participant Status Reference

```
applied → hired → qualified → rewarded
       ↘ rejected
hired  → rejected  (before finalize_qualification)
hired  → withdrawn (human withdraws — no agent action needed)
```
