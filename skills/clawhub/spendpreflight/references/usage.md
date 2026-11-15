# Setup, scope and one offline example

The skill's default has no network, signer, credentials, payment client or account requirement. The companion helper needs Node.js 20+ and the exact published SDK `spendpreflight@0.4.0`. After the operator authorizes dependency installation, run from this skill folder:

```sh
npm install --ignore-scripts --omit=dev --legacy-peer-deps --no-audit --no-fund
node examples/offline.mjs
```

The example uses fictional local data and prints two **hold** results with `payment_authorized: false`, `signer: null` and `network_requests: 0`. It neither looks up the example address nor requests its URL. No environment variables are read or needed.

For supplied public data, pipe a JSON object to `node scripts/offline.mjs`. Its only top-level fields are `tool`, `input` and `policy`:

- `preflight_payment`: input contains an actual x402 v2 `challenge` and the exact `selected_requirement` from its `accepts` array.
- `check_payee`: input contains one or more public `address`, `domain`, `name` strings.
- `policy`: SDK 0.4.0 JSON Spend Policy, with explicit amount limits, merchant allow/block lists and exact allowed network/native-USDC pairs. See the example for its shape. Do not treat the example limits or allowlist as approval for a real payment.

Malformed inputs and local policy blocks return block. Valid offline checks return hold. The helper cannot be switched online by a JSON field, approval flag, environment variable or command-line option. Its offline invocation does not reserve a durable payment budget. The SDK's configured online controllers use in-process UTC-day reservations, not a wallet-wide or restart-persistent ledger; this helper does not create such a controller.

## Optional existing MCP connection

An online tool call is separate from this offline helper. Use only an operator-configured SpendPreflight MCP connection at `https://api.spendpreflight.com/mcp`, exposing `preflight_payment` and `check_payee`. Use its actual current schema, quote and payment requirements rather than guessed prices or manually constructed payment headers. No runtime connection, x402 wallet integration, trial, authentication or payment setup is installed by this skill.

SpendPreflight is the skill publisher's **paid external service**. A human must approve each potentially paid screening call and its current quote/cap before a configured transport can spend. Target merchant payments require separate approval. Tool annotations such as read-only describe the screening operation and do not make a paid API call free. A returned allow, a local allowlist or a prior approval is not permission to sign. Missing remote evidence, authorization or an enforceable fee cap means hold.

The skill artifact is MIT-0. The dependency's MIT license and our API pricing/service terms are separate and unchanged.

References: [SDK 0.4.0](https://www.npmjs.com/package/spendpreflight/v/0.4.0), [SpendPreflight MCP and Spend Policy](https://docs.spendpreflight.com/mcp/), [OpenClaw skill format](https://docs.openclaw.ai/clawhub/skill-format).
