## Description:

Runs a fundamentals checklist for crypto projects covering token, liquidity, contract safety, team, and protocol health, returning PASS, WATCH, or FLAG research support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trdyqs6bsr-lksnf](https://clawhub.ai/user/trdyqs6bsr-lksnf)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to perform crypto project due diligence before investment decisions. It supports research workflows by collecting checklist-style risk signals and presenting uncertainty without giving buy, sell, or hold advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill operates in a high-risk financial context and may influence crypto investment decisions.

Mitigation: Treat PASS, WATCH, and FLAG outputs as research support only, and do not present them as financial advice or price predictions.

Risk: The skill promotes paid x402 calls, credit bundles, referrals, API-key use, and Telegram subscriptions.

Mitigation: Require explicit user approval before any wallet payment, credit purchase, referral action, API-key use, or digest subscription.

Risk: The skill depends on an external crypto API for project checks.

Mitigation: Review the API and skill before installation, and state uncertainty when data is stale, incomplete, or unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/trdyqs6bsr-lksnf/skills/crypto-research-checklist)
- [Crypto API homepage](https://crypto-api-blush.vercel.app)
- [Crypto API OpenAPI schema](https://crypto-api-blush.vercel.app/openapi.json)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with PASS, WATCH, or FLAG verdicts and checklist sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require curl and jq; paid API calls, x402 payments, credit purchases, referral actions, API-key use, and Telegram digest subscriptions should require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
