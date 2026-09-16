# SOLO Mission Platform — Solana Wallet (On-Chain Missions)

Solana missions escrow into the `solo_escrow` Anchor program. The Sponsor is a Solana keypair that
signs `create_task`, and later `cancel_task` / `emergency_refund` / `claim_refund`. All of them must
be signed by the **same address**.

You do not hand-assemble any of them: `fund_solana_mission` and `refund_solana_mission` build,
verify and submit each one. That matters because there is no `cast send` equivalent on Solana (see
*Tooling* below), so an earlier version of this document described a capability that had no tooling
behind it.

If you have already read `wallet-setup.md` for Base, three things differ and each one has bitten
someone:

1. **You need SOL as well as USDC.** On Base you needed ETH for gas and USDC for the budget. Solana
   adds *rent* — a deposit for the accounts your mission creates. It has no EVM analogue.
2. **You do not build the transaction.** The backend builds it and you sign it. That means you must
   **verify what you are signing**, because you have no wallet UI to decode it for you.
3. **There is no `cast`.** The capabilities `cast` gives you are split across three binaries. See
   *Tooling* below.

---

## Skip this if you already have a signing tool

If your environment provides a managed wallet, a KMS-backed key, or anything that can sign a
Solana transaction, use it. You need exactly two things from it:

- the **base58 address** that will act as Sponsor
- a way to sign a serialised transaction and hand back the signed bytes

Set `SOLO_SOLANA_KEYPAIR_PATH` (or use your tool directly) and go to *Funding a mission*.

---

## What the money is actually for

Read this before deciding an amount. The rent line is the one that surprises people.

| Item | SOL | ≈USD | Comes back? |
|---|---|---|---|
| Task account rent | 0.00374 | $0.374 | partly — $0.139 on `close_task` |
| TaskVault token account | 0.00204 | $0.204 | **in full** on `close_task` |
| `create_task` + `confirm_funding` fees | 0.00004 | $0.004 | no |
| **Locked during the mission** | 0.00582 | **$0.58** | |
| **Permanent cost per mission** | 0.00239 | **$0.24** | no — kept on purpose |

**Rent is a refundable deposit, not a fee.** The lamports sit in accounts you control and come back
when they close. The ~$0.24 that does not return buys the on-chain record that makes your escrow and
your frozen participant list checkable by anyone, forever. On a $10 mission that is 2.4%; on a
$1,000 mission, 0.024%.

Budget **0.02 SOL per concurrent mission** and you will not think about it again.

---

## Creating a wallet (owner action — not the agent)

> ⚠️ **Do this on a local trusted machine.** Not on a remote server, and not by asking the agent to
> generate a key it then holds.

```bash
# Install the Solana CLI
sh -c "$(curl -sSfL https://release.anza.xyz/stable/install)"
solana --version

# Generate the keypair — writes a JSON byte array
solana-keygen new --outfile ~/.config/solana/solo-sponsor.json

# The address to fund
solana address -k ~/.config/solana/solo-sponsor.json
```

Fund it with SOL and with the payout token. On devnet:

```bash
solana airdrop 1 <ADDRESS> --url devnet
```

> The devnet faucet is aggressively IP-rate-limited and will often refuse outright. If it does, use
> https://faucet.solana.com (GitHub login) rather than retrying in a loop. Getting 4 SOL this way
> once took 30 attempts over 12 minutes.

The payout token is decided by the platform, not by you — call `get_solana_config` to see which
mints are whitelisted on the current cluster. On devnet the platform currently funds new missions
in **`USDC`** — Circle's real devnet USDC — not the `TEST_USDC` mint also listed there (that one
exists for the platform's own internal/automated funding and is not what your mission will use
unless you were told otherwise). Get some from https://faucet.circle.com (select **Solana Devnet**),
not `solana airdrop`, which only dispenses SOL.

Then point the MCP server at it:

```bash
export SOLO_SOLANA_KEYPAIR_PATH=~/.config/solana/solo-sponsor.json
# or inline, for a containerised agent:
export SOLO_SOLANA_KEYPAIR="$(cat ~/.config/solana/solo-sponsor.json)"
```

**The key stays in your process.** It is never sent to the SOLO API. The backend builds transactions
and submits them, but only you can authorise one — which is why a compromised backend cannot move
your funds.

---

## Check you can actually pay before you create anything

```
get_solana_wallet
```

```json
{
  "configured": true,
  "address": "SNWf…7X1Z",
  "sol": 1.5,
  "token_account": "…",
  "token_account_exists": true,
  "token_balance": "5000",
  "can_pay_fees": true
}
```

Two fields worth understanding:

- **`token_account_exists: false`** means you hold no balance of that mint yet. An SPL token account
  is created when tokens first arrive, and `create_task` reads yours — so funding fails without one.
  The on-chain error names the *account*, not the missing balance, which sends people looking in the
  wrong place.
- **`sol: 0`** produces `Attempt to debit an account but found no record of a prior credit`. That
  message never mentions SOL. If you see it, this is why.

---

## Funding a mission

```
create_mission        { chain: "solana", budget: 10, max_humans: 2, base_reward: 5, … }
fund_solana_mission   { mission_id: "…", expected_budget: 10 }
```

`fund_solana_mission` does four things in one call: asks the backend to build the transaction,
**decodes and verifies it**, signs it locally, and submits it.

### Why verification is not optional

On Base you built `createTask()` yourself from published parameters, so you could check every field
against the API response before signing. On Solana the backend builds the transaction and hands you
base64. That removes a whole class of integration breakage — the instruction layout is no longer a
published contract you have to track — but it hands you bytes you cannot read.

A human signing in Phantom gets that decoded for free by their wallet. **You have no wallet UI.**

So `fund_solana_mission` decodes the transaction and checks it. Pass `expected_budget` as **what you
intended**, not what the API told you — comparing the API's answer to itself proves nothing. It
refuses to sign, and returns the discrepancies, if:

- the budget, deadlines, lottery parameters or mint differ from what you expected
- the transaction contains **more than one instruction** (an appended transfer would be authorised
  by your signature too)
- the program is not the escrow program
- you are not the only signer, or not the fee payer
- the escrow vault is not a program-derived address, i.e. **someone holds its private key**
- the vault equals your own token account, i.e. the budget never actually leaves your control
- the parameters the backend *described* disagree with the bytes it *built*

That last one is the strongest check. Everything else compares the backend's description against
your expectations — and a dishonest backend controls that description. Comparing the description
against the instruction data catches a backend that quotes correct numbers and encodes different
ones.

Use `dry_run: true` to see exactly what would be signed without signing or paying anything.

If verification fails: **do not retry blindly.** Nothing was escrowed and no fee was paid. The
discrepancy is either a bug worth reporting or an attempt to have you authorise something else.

### Lottery and non-lottery both work

`create_mission` takes the same lottery parameters on either chain:

```
create_mission { chain: "solana", budget: 20, max_humans: 10,
                 base_reward: 1, lottery_winner_count: 2, lottery_prize_per_winner: 5 }
```

`budget` must cover `base_reward × max_humans + lottery_prize_per_winner × lottery_winner_count`
plus the platform fee, exactly as on Base.

**Where the randomness comes from is different, and worth understanding if you are asked to justify
a draw.** At `finalize_qualification` the program commits a slot number on chain and will accept no
other one at settle. The randomness is that slot's blockhash — which did not exist when the cohort
froze, cannot be chosen by the platform because the slot is already committed, and can be fetched by
anyone who wants to recompute the winners. The final value is `keccak(seed_reveal ‖ blockhash)`, so
neither the platform (holding the seed) nor a validator (influencing the blockhash) decides the
outcome alone.

That is the same trust model as the Base deployment, which uses `blockhash(taskEntropyBlock)`.

> When there are at least as many prizes as qualified participants the outcome is predetermined, and
> the program consumes no randomness at all. Nothing to verify, and nothing to wait for.

### The task id race

The response includes a `task_id`. It is valid only while the program's internal counter has not
moved — if another mission is funded in between, your transaction fails on a seeds constraint.
That is the safe direction: a stale id cannot fund the wrong task, it simply does not execute.
Request a fresh transaction and sign again.

Blockhashes also expire in **60–90 seconds**. If signing takes longer, request a fresh transaction
rather than submitting a stale one.

---

## Tooling: there is no `cast`

Foundry's `cast` has no single-binary equivalent. The capabilities are split:

| What you want | Base (`cast`) | Solana |
|---|---|---|
| Read an account, typed | `cast call` | **`anchor account solo_escrow.Task <addr> --provider.cluster devnet`** — deserialises using the IDL |
| Read raw account bytes | `cast storage` | `solana account <addr>` |
| **Send a typed instruction** | `cast send` | **no CLI equivalent** — build it in TS/Rust, or use `fund_solana_mission` |
| Balance | `cast balance` | `solana balance <addr>` |
| Transaction receipt | `cast tx` | `solana confirm -v <signature>` |
| Decode a transaction | `cast 4byte-decode` | `solana decode-transaction` |
| Token operations | `cast send` on the ERC20 | `spl-token` CLI |
| Local chain | `anvil` | `solana-test-validator` |
| Interactive REPL | `cast` + `chisel` | `anchor shell` |

`anchor account` is the closest thing to `cast call` and genuinely useful for checking your own
escrow:

```bash
anchor account solo_escrow.Task <TASK_PDA> --provider.cluster devnet
# {"budget": 10000000, "status": {"funded": {}}, "qualified_count": 0, …}
```

It needs the IDL present at `target/idl/solo_escrow.json` in the workspace you run it from.

**The gap that matters:** there is no `cast send` for arbitrary program instructions. This is why the
funding flow is a tool rather than a documented CLI incantation — an agent cannot reasonably be
asked to hand-assemble borsh instruction data.

> ⚠️ `anchor` shells out to the Solana toolchain. If `solana` is not on your `PATH`, `anchor --help`
> will try to *install* a specific Solana version and then fail. Put
> `~/.local/share/solana/install/active_release/bin` on your `PATH` first.

---

## Verifying escrow independently

You should not have to trust the SOLO API that your money is locked. Every on-chain mission exposes
its escrow account, and you can read it from any RPC node:

```bash
# The task account, deserialised
anchor account solo_escrow.Task <TASK_PDA> --provider.cluster devnet

# The vault's actual token balance — this is the escrow
spl-token balance --address <VAULT_PDA> --url devnet
```

The vault is a program-derived address whose authority is the task itself, so **no key can move it**
— not yours, not ours. That is the guarantee, and it is checkable rather than promised.

---

## Getting the money back

Three routes, and which one is legal depends on the mission's state. **`refund_solana_mission` with
no `action` tells you which** rather than making you guess:

```
refund_solana_mission { mission_id: "…" }
→ { available_actions: ["emergency_refund"], why_not_claim_refund: "…" }
```

| Action | Legal when | Returns |
|---|---|---|
| `cancel` | funded, and hiring has not closed yet | the whole budget |
| `emergency_refund` | funded or qualified, and the settlement deadline has passed | the whole budget |
| `claim_refund` | the mission settled `refundable` | the unspent remainder |

Then run it for real:

```
refund_solana_mission { mission_id: "…", action: "emergency_refund" }
```

Same shape as funding: the backend builds, the tool **verifies and signs locally**, the backend
submits. Use `dry_run: true` to see what would be signed without moving anything.

A refund moves the *entire* escrow, so the verifier is stricter than for funding — it refuses to
sign unless the transaction targets the escrow program, contains exactly one instruction, has you as
the only signer, sends the tokens to **your** token account, and carries exactly the 8-byte
discriminator. None of the three instructions takes arguments, so anything longer means something
was appended.

> **If nothing is available yet, that is the program's rule, not a bug.** Once hiring closes,
> `cancel` is gone — participants may already have done the work — and `emergency_refund` only
> opens once the settlement deadline passes. A mission mid-flight has no refund route by design.

### Rent is separate from the budget

A refund returns the USDC. The ~$0.24 of permanent per-mission rent is not part of it, and the
recoverable ~$0.20 comes back through `close_task`, which is permissionless and batched by the
backend — you do not need to call it.

## What differs after funding

Nothing else, from your side. `hire_participant`, `finalize_qualification` and `settle_mission` behave
identically on both chains — the platform signs those, not you.

The one participant-facing difference worth knowing: a Solana participant funds their own token
account (~$0.21, refundable) at their **first** collection, and needs no SOL before that. So a
participant can bind a wallet, apply, be hired, do the work and see their rewards with an empty
wallet. What they cannot do with zero SOL is take delivery.
