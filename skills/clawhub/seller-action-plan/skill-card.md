## Description:

Helps Amazon sellers use ARI product-detail and review data for a single ASIN to prioritize evidence-supported operational next steps and checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to generate a prioritized action plan for one ASIN from product-detail fields and review evidence. It is intended for operational planning, not advertising, inventory, profit, tax, or cash-flow decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an authenticated ARI API key stored locally.

Mitigation: Install it only when ARI product-review analysis is intended, protect the local API key, and remove or rotate the key if the environment is shared or no longer trusted.

Risk: Analysis and collection commands can consume ARI credits.

Mitigation: Review the returned quote and request ID before confirming any paid run or collection command.

Risk: The security review notes that the CLI may support behavior beyond the advertised single-ASIN action-plan workflow.

Mitigation: Use the documented operations flow for one ASIN and avoid workflow, focus, or competitor options unless broader analysis is deliberately intended.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/seller-action-plan)
- [Amazon seller action plan API reference](references/reference.md)
- [Amazon seller action plan workflow](references/operation-workflow.md)
- [ARI service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline shell commands and evidence-based action-plan guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before credit-consuming analysis or collection commands.]

## Skill Version(s):

1.4.11 (source: server release metadata, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
