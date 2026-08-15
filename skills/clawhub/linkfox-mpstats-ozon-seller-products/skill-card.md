## Description:

Returns seller-scoped MPSTATS Ozon Russia product metrics, including per-SKU sales, revenue, price, ratings, inventory, turnover, lost sales, filters, sorting, and currency conversion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts, ecommerce operators, and developers use this skill to audit an Ozon seller's SKU portfolio, identify top products, compare competitor stores, and inspect stockout or turnover metrics from a numeric seller ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the skill suspicious because it includes Ozon analytics plus login, API-key, billing, feedback, and credential-handling flows.

Mitigation: Install only if LinkFox is trusted for those workflows, and prefer completing login and payment directly on official LinkFox pages.

Risk: API keys or onboarding credentials may appear in script output or local session files during setup.

Mitigation: Treat generated API keys as secrets and avoid sharing logs or saved onboarding output that contain credentials.

Risk: LINKFOX_* endpoint override environment variables can redirect requests away from default LinkFox services.

Mitigation: Avoid custom endpoint overrides unless they point to infrastructure you control.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-seller-products)
- [MPSTATS Ozon seller products API reference](references/api.md)
- [Authentication and billing onboarding guide](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses saved to local files; small responses may be printed inline and large responses summarized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses authenticated LinkFox gateway calls, numeric Ozon seller IDs, optional filters, sorting, currency parameters, and a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
