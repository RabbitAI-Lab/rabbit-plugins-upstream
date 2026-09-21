## Description:

Builds an evidence-based action plan for a single Amazon ASIN by using ARI product detail and review data to rank operational priorities and checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to turn product detail and review evidence for one ASIN into prioritized operating actions. It excludes PPC, live inventory, replenishment, profit, tax, cash-flow, and unsupported store-data decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ARI operations require a local ARI API key and use ari.funewa.com for product and review analysis.

Mitigation: Install only when comfortable using the ARI service, store the API key locally, and keep API/authentication traffic on the documented ari.funewa.com endpoint.

Risk: Confirmed collection or analysis operations can spend ARI credits.

Mitigation: Review the quote and request ID first, then run credit-spending operations only after explicit user confirmation.

Risk: The generated action plan may be misleading if product details or review samples are incomplete.

Mitigation: Treat conclusions as evidence-limited, identify missing data, and avoid using the skill for PPC, live inventory, replenishment, profit, tax, or cash-flow decisions.

Risk: Documentation and CLI messages are primarily Chinese-language.

Mitigation: Use the skill with users who can review the Chinese-language prompts, warnings, and outputs or provide translation before acting on results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/seller-action-plan)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [Amazon Seller Action Plan API reference](artifact/references/reference.md)
- [Amazon Seller Action Plan operation workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with optional inline shell commands and ARI status details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and user confirmation before credit-spending collection or analysis runs.]

## Skill Version(s):

1.4.13 (source: server evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
