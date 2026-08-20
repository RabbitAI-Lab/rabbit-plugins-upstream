# MagicPay Setup

<!-- magicpay-continuation-contract:v1 -->

## Contents

- [Setup Instructions](#setup-instructions)
- [First-Time Landing Setup](#first-time-landing-setup)
- [UI Connect Setup](#ui-connect-setup)

## Setup Instructions

Most MagicPay work is normal operating mode: the user has already connected
MagicPay locally, and the agent uses this skill for approved login, identity,
checkout, donation, subscription, payment, Memory fill, CAPTCHA recovery, and
browser-bound workflows.

There are two setup exceptions. Treat them as mutually exclusive.

If the current user prompt says to read/install `skill.md`, comes from the
MagicPay landing bootstrap flow, or asks to continue setup after installation,
that prompt is a setup request. Installing the skill and CLI is not completion.
After `magicpay --help` includes `setup next`, continue in the same task by
running `magicpay setup next`, then follow its returned `instructions` until
setup needs user input, completes, or returns a real blocker. A skill-manager
recommendation to start a fresh agent session affects only future skill-catalog
activation; it does not block the installed CLI and is not a reason to stop at
an installation report or ask the user to repeat the setup prompt. Ask for an
email, OTP, API key, or other setup input only when the returned instructions
request it. The only exception is an authenticated MagicPay UI prompt that
includes a setup token; that path uses UI Connect Setup.

For read-only account questions such as "what is my card balance?", do not ask
for an email first. Run `magicpay status`. If status is healthy, answer with
`magicpay card-balance` or the matching read-only account command. If status
shows missing or invalid local setup, run `magicpay setup next` and follow its
returned `instructions`. Ask for the user's email only when those instructions
ask for it.

### First-Time Landing Setup

Use this mode only when the user asks to set up MagicPay, log in to MagicPay,
connect MagicPay, or top up MagicPay after installing this skill. Also use
this mode when the current prompt explicitly says it came from the MagicPay
landing bootstrap flow or asks you to follow the setup instructions in this
skill.

1. Make sure the MagicPay CLI is available and has the setup command this
   skill needs:

   ```bash
   magicpay --version
   magicpay --help
   ```

   The help output must include `setup next`. If the `magicpay` command is
   missing or `setup next` is missing, install or repair the CLI before
   continuing. Do not stop after only reporting that `magicpay` is not on
   `PATH`.

   If the current setup request installed this skill from
   `http://localhost:4321`, `http://localhost:4321/skill.md`, or an AgentPay
   local generated dist path (`./packages/agent-skills/dist/...`), prefer the
   local CLI tarballs so the CLI and skill capabilities match:

   ```bash
   npm i -g http://localhost:4321/dev-packages/magicbrowse-local.tgz http://localhost:4321/dev-packages/magicbrowse-cli-local.tgz http://localhost:4321/dev-packages/captcha-solver-local.tgz http://localhost:4321/dev-packages/magicsearch-local.tgz http://localhost:4321/dev-packages/magicpay-sdk-local.tgz http://localhost:4321/dev-packages/magicpay-home-local.tgz http://localhost:4321/dev-packages/magicsearch-cli-local.tgz http://localhost:4321/dev-packages/magicpay-cli-local.tgz
   magicpay --version
   magicpay --help
   magicsearch --help
   magicbrowse --help
   ```

   If the localhost tarballs are unavailable but the AgentPay checkout is
   available, use the local files:

   ```bash
   npm i -g ./apps/landing/public/dev-packages/.lifecycle/magicbrowse-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicbrowse-cli-local.tgz ./apps/landing/public/dev-packages/.lifecycle/captcha-solver-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicsearch-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicpay-sdk-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicpay-home-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicsearch-cli-local.tgz ./apps/landing/public/dev-packages/.lifecycle/magicpay-cli-local.tgz
   magicpay --version
   magicpay --help
   magicsearch --help
   magicbrowse --help
   ```

   If the local tarballs are missing, run this from the AgentPay repo root and
   then retry one of the local install commands above:

   ```bash
   pnpm --filter @agentpay/landing prepare:local-packages
   ```

   In production or when the prompt did not use a local AgentPay skill source,
   install the public CLI and verify again:

   ```bash
   npm i -g @nuanu-ai/magicbrowse-cli@latest @nuanu-ai/magicsearch-cli@latest @nuanu-ai/magicpay-cli@latest
   magicpay --version
   magicpay --help
   magicsearch --help
   magicbrowse --help
   ```

   If `setup next` is still missing after repair, stop and report the CLI
   version and install source instead of guessing an alternate command.

2. Ask `magicpay setup next` what to do next. Use the default production
   gateway unless the current setup prompt or served `skill.md` explicitly
   gives a branch API URL or local hosted-link origin:

   ```bash
   magicpay setup next --intent landing --platform <runtime> --agent-name "<runtime> Agent"
   ```

   For local development only, use the complete profile command supplied by
   the setup prompt. Do not omit `--env`, invent, reuse, or hardcode a preview
   branch URL:

   ```bash
   magicpay setup next --intent landing --platform <runtime> --agent-name "<runtime> Agent" --api-url <branch-api-url> --env local
   ```

3. Read the returned JSON and follow the `instructions` text exactly. Treat the
   `instructions` field as the agent-facing setup plan. Its English copy is a
   semantic and formatting recommendation: render the user-facing message
   naturally in the language the user is currently using. In mixed-language
   conversations, follow the latest clear user request; fall back to English
   only when no preference can be inferred. Do not ask the user to choose a
   language. Keep `MagicPay`, `x402`, `USDT`, `USDC`, amounts, currencies, and
   URLs unchanged. Do not maintain your own mapping from `state` or
   `nextAction` to user prompts.
4. If the instructions ask for an email, ask the user for the email, run the
   provided `magicpay setup start ...` command, then ask for the one-time code.
   <!-- magicpay-continuation:v1 id=setup-run-next-command action=run-exact-returned field=nextCommand -->
   Run exactly the returned `nextCommand`.
   <!-- /magicpay-continuation:v1 -->
   Supply the OTP requested by that setup command. If setup verify succeeds,
   continue with the common balance-driven completion flow in the remaining
   `instructions` text. Do not guess, invent, repeat, log, or summarize OTP
   digits.
5. If the instructions say an existing connection was found, ask whether to
   reuse it or set up MagicPay with another email. Reuse only after the user
   chooses reuse.
6. Use one common completion flow after OTP verification or approved reuse,
   regardless of whether setup reports `account.status: "created"`,
   `account.status: "existing"`, or the backwards-compatible `unknown` status:
   run `magicpay card-balance` first and follow the exact numeric branches in
   the returned setup instructions. A positive balance gets the funded
   handoff without a top-up link. An exactly zero numeric `balance` gets one
   `magicpay top-up-link` call and the exact returned hosted URL. A failed or
   malformed balance is not proof of zero and must not create a top-up link.
   If the confirmed balance is zero but link creation fails, report only that
   the link is temporarily unavailable; never expose the raw failure.
7. For a successful install or setup handoff, return only the concise localized
   user-facing message recommended by the instructions. Do not add package
   versions, installer response fields, gateway health, agent status,
   settled/held breakdowns, config paths, browser or curl fallback details,
   commands, or an internal verification checklist. For the zero-balance branch,
   say: “Top up your MagicPay balance through this link: {exact hosted top-up
   URL}. Crypto top-ups can take a few minutes to arrive. MagicPay will notify
   you when the funds are available.” Localize naturally, render the returned
   URL as the link target, and do not append a payment approval reminder.

Do not start this flow merely because the MagicPay skill exists in the runtime
during unrelated work. Do start it when the current user prompt asked to
read/install MagicPay `skill.md`, asks for MagicPay setup/top-up, or a read-only
MagicPay account command discovers missing local setup. If the prompt came from
the MagicPay UI and includes a setup token, use UI Connect Setup instead.

### UI Connect Setup

Use this mode when the current prompt came from the authenticated MagicPay UI
after the user clicked Create agent or Copy prompt. In that path, MagicPay has
already created the account, the external agent, and a setup token for this
agent.

1. Do not ask for the user's email.
2. Do not run `magicpay setup start` or `magicpay setup verify`.
3. Do not ask for an OTP.
4. Ensure the MagicPay skill and owner CLI are installed for the current
   runtime. If they are already installed, skip reinstallation unless the
   prompt asks for an update or the runtime cannot see the skill.
5. Initialize the local gateway config with the setup token from the UI prompt:

   ```bash
   magicpay init "<setup-token>"
   ```

6. Run `magicpay status`.
7. Report that the agent is connected and ready for normal MagicPay workflows.

If `magicpay status` fails after `init`, run `magicpay doctor` and report the
safe error. Do not fall back to the First-Time Landing Setup unless the user
explicitly says this is not a UI-created agent.
