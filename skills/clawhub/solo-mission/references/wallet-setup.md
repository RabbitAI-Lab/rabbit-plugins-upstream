# SOLO Mission Platform — Wallet Setup (On-Chain Missions)

> ⚠️ **This is the Base wallet path — Base is closed to new mission creation.**
> For any new on-chain mission, set up a Solana wallet instead: see
> `references/solana-wallet.md`. This document remains accurate only for resuming
> or managing a Base mission created before the closure.

On-chain missions require a Sponsor wallet — an Ethereum EOA that signs `createTask()`,
`cancelTask()`, `emergencyRefund()`, and `claimRefund()` on EscrowVault. All four
functions must be called from the **same address**.

---

## Skip this if you already have a funding tool

If your environment provides a signing/funding tool (e.g. a managed wallet service,
an existing KMS-backed key, a hardware wallet CLI, or a platform that handles
transaction signing for you), use it directly. You only need two things from it:

- `WALLET_ADDRESS` — the Ethereum address that will act as Sponsor
- A way to call `cast send` or submit signed transactions on Base Sepolia

Set `WALLET_ADDRESS` and proceed to `references/onchain.md`. No new wallet needed.

---

## Creating a new wallet (owner action — not the agent)

> ⚠️ **Wallet creation must be performed by the owner on a local trusted machine,
> not by the agent and not on a remote server.**

### Prerequisites

- Foundry installed. `curl -L https://foundry.paradigm.xyz | bash` fetches only the
  small `foundryup` bootstrap script — read it before running (`curl -L
  https://foundry.paradigm.xyz -o foundryup-installer.sh && less
  foundryup-installer.sh`) rather than piping blind. Then install a **pinned**
  version rather than implicit latest, so this doesn't silently install a different
  toolchain next time it's run:
  ```bash
  foundryup -i v1.7.1   # check https://github.com/foundry-rs/foundry/releases for current
  ```
  `foundryup` verifies binary checksums by default for the actual toolchain download —
  only pass `--force` if you specifically need to skip that, and don't by default.
- Verify: `cast --version`

### Generate the keypair

Run on your **local machine**:

```bash
cast wallet new
# Output:
#   Address:     0xYourWalletAddress
#   Private key: 0xYourPrivateKey
```

### Critical security warnings

> 🔴 **NEVER share your private key with the agent or paste it into any AI chat.**
>
> 🔴 **LLM SIDE-CHANNEL RISK: If you paste your private key into any AI chat interface
> (including this one), the key may be logged or stored. Treat it as a secret that
> must never enter an AI conversation.**
>
> 🔴 **NEVER store the private key in plaintext on disk or in a `.env` file on a server.**
>
> ✅ After copying the key, clear your terminal history:
> ```bash
> history -c && > ~/.bash_history   # bash
> fc -p && > ~/.zsh_history          # zsh
> ```

---

## Securing the private key

Encrypt the key so it never exists as plaintext on the server, then convert it into
a Foundry keystore **once** — after that, no `cast send` call ever needs the raw key
again. This matters beyond the initial storage: `references/onchain.md`'s call
sequence runs `cast send ... --private-key $PRIVATE_KEY` at every step (`approve`,
`createTask`, `cancelTask`, `claimRefund`, `emergencyRefund`) over the life of a
mission, and each of those invocations puts the raw key on that process's command
line — visible to anything that can list processes on the box (`ps`, other users,
monitoring agents). A keystore removes the key from that path entirely: only an
encrypted file and a separate passphrase are ever referenced at call time, and
`references/onchain.md` and the on-chain section of `SKILL.md` both assume this
setup (`$KEYSTORE_PATH` / `$KEYSTORE_PASSWORD_FILE`, not `$PRIVATE_KEY`).

### Option A — OpenSSL (works everywhere, no cloud required)

On your **local machine**:

```bash
openssl enc -aes-256-cbc -pbkdf2 \
  -in <(echo -n "YOUR_PRIVATE_KEY_HEX") \
  -out wallet.enc
```

Transfer to server:

```bash
scp wallet.enc user@your-server:/path/to/wallet.enc
chmod 600 /path/to/wallet.enc
```

At runtime, decrypt into memory and **immediately import into a keystore** — this is
the one and only time the raw key exists outside `wallet.enc`:

```bash
PRIVATE_KEY=$(openssl enc -d -aes-256-cbc -pbkdf2 -in wallet.enc)
cast wallet import solo-sponsor --private-key "$PRIVATE_KEY" \
  --keystore-dir ~/.foundry/keystores   # prompts for a NEW keystore passphrase
unset PRIVATE_KEY
```

Store both passphrases (the OpenSSL one for `wallet.enc`, and the new keystore one)
in a password manager. **Never store either on the same server as the file it
protects.**

### Option B — Cloud KMS (passphrase-free at the encryption layer)

The cloud VM authenticates automatically via its IAM role — no OpenSSL passphrase
needed to decrypt `wallet.enc`. You still set a keystore passphrase in the import
step below; that one is inherent to the keystore format, not something KMS replaces.

| Environment | KMS option |
|---|---|
| GCP Compute Engine | GCP KMS |
| AWS EC2 | AWS KMS |
| Azure VM | Azure Key Vault |
| Other | Use OpenSSL above |

At runtime:

```bash
# GCP example
PRIVATE_KEY=$(gcloud kms decrypt \
  --ciphertext-file=wallet.enc \
  --plaintext-file=- \
  --key=my-key --keyring=my-keyring --location=global)
cast wallet import solo-sponsor --private-key "$PRIVATE_KEY" \
  --keystore-dir ~/.foundry/keystores
unset PRIVATE_KEY
```

### Storing the keystore passphrase for unattended (agent-driven) signing

An agent running the on-chain lifecycle end-to-end can't sit at an interactive
password prompt for every `cast send`. Put the keystore passphrase — not the private
key — in a file only the owner can read, the same way `wallet.enc`'s own passphrase
would be handled if it had to live on the box:

```bash
echo -n "your-keystore-passphrase" > ~/.foundry/keystore.pass
chmod 600 ~/.foundry/keystore.pass
```

This is a strictly smaller blast radius than the key itself: anyone who reads this
file still needs the keystore file (`~/.foundry/keystores/solo-sponsor`) to sign
anything, and anyone who copies the keystore file still needs this passphrase.
Neither alone moves funds — unlike a leaked `$PRIVATE_KEY`, which does.

---

## Fund the wallet

The Sponsor wallet needs ETH for gas and USDC for the mission budget before calling
`create_mission`.

| Asset | Purpose | Source |
|---|---|---|
| Base Sepolia ETH | Gas for every on-chain call | [Base Sepolia faucet](https://docs.base.org/docs/tools/network-faucets) |
| Test USDC | Mission budget (`amount_raw`) | [Circle USDC faucet](https://faucet.circle.com) — select Base Sepolia |

Check USDC balance before creating a mission:

```bash
cast call 0x036CbD53842c5426634e7929541eC2318f3dCF7e \
  "balanceOf(address)(uint256)" $WALLET_ADDRESS \
  --rpc-url https://sepolia.base.org
# Divide result by 1e6 for USDC amount — must be ≥ funding_params.amount_raw
```

---

## Set environment variables

```bash
export WALLET_ADDRESS=0xYourWalletAddress
export KEYSTORE_PATH=~/.foundry/keystores/solo-sponsor
export KEYSTORE_PASSWORD_FILE=~/.foundry/keystore.pass
```

No `PRIVATE_KEY` variable — the keystore import step above is the last time the raw
key exists anywhere outside `wallet.enc`. These three values are what
`references/onchain.md` and the on-chain section of `SKILL.md` actually reference for
every `cast send` call (`--keystore $KEYSTORE_PATH --password-file
$KEYSTORE_PASSWORD_FILE` in place of `--private-key`).
