## Description: <br>
Pre-flight checks for Polymarket trading via the TickTape API (ticktape.cc). Use BEFORE sending a Polymarket order (slippage/depth/fee verdict), BEFORE copy-trading a wallet (copyability verdict), or when choosing whom to copy (leaderboard, red list). Trigger words: Polymarket order, preflight, slippage check, safe size, copy trade, copy this wallet, whale leaderboard, who to copy, red list, is this wallet worth copying, will this order move the market. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[padak](https://clawhub.ai/user/padak) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External agents and developers use this skill before Polymarket trades or copy-trading decisions to request TickTape risk checks, wallet copyability ratings, leaderboards, and red-list results. It is intended for pre-flight analysis only and does not provide custody or trade execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live use can spend real USDC through x402 payments or prepaid credits. <br>
Mitigation: Use sandbox or probe mode first, verify payment terms and recipient before signing, and enforce client-side per-call and per-session spend caps. <br>
Risk: The returned verdicts may influence trading or copy-trading decisions. <br>
Mitigation: Treat results as pre-flight risk checks rather than investment advice, and keep a human review step before placing trades. <br>
Risk: Prepaid credit tokens grant access to paid credits if exposed. <br>
Mitigation: Store tk_ tokens only in secret storage or environment variables, avoid logging them, and rotate by purchasing a new token if exposed. <br>
Risk: Retrying credit-purchase POST requests with fresh payment authorization can create duplicate charges. <br>
Mitigation: Do not auto-retry POST /api/credits with newly signed authorizations; reuse the same signed authorization for idempotent retry behavior. <br>
Risk: Paid leaderboard, red-list, and copy-profile data may not change until the next refresh timestamp. <br>
Mitigation: Respect next_refresh_at and cache paid responses until the service indicates fresh data is available. <br>


## Reference(s): <br>
- [TickTape homepage](https://ticktape.cc) <br>
- [TickTape authentication and payment details](https://ticktape.cc/auth.md) <br>
- [TickTape agent metadata](https://ticktape.cc/agent.json) <br>
- [TickTape verification runbook](https://ticktape.cc/why.md) <br>
- [TickTape OpenAPI specification](https://ticktape.cc/openapi.json) <br>
- [ClawHub skill page](https://clawhub.ai/padak/skills/polymarket-preflight) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, API calls, shell commands, configuration] <br>
**Output Format:** [Markdown with HTTP examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns and interprets JSON verdicts from external TickTape endpoints; sandbox and probe modes are available before paid calls.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
