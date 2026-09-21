## Description:

Generates a user-confirmed weekly operations brief for a subscribed Amazon ASIN, summarizing recent product changes, review signals, and prioritized follow-up tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and ecommerce teams use this skill to request a weekly Amazon ASIN operations report after authorizing ARI access and confirming any quoted credit spend. The skill is intended for single-product weekly review, not shop-level inventory, order, ad, or profit reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the CLI can run broader paid operation workflows than the fixed single-ASIN weekly flow described by the skill.

Mitigation: Review command use before installation and keep agent usage constrained to the documented weekly/asin workflow, quote, explicit confirmation, and status recovery path.

Risk: The skill stores an ARI API key locally and sends ASIN/report requests to ari.funewa.com.

Mitigation: Use a dedicated ARI key, keep it in the documented local user configuration or ARI_API_KEY environment variable, and rotate it if the local environment is shared or compromised.

Risk: Paid collection or analysis can spend ARI credits.

Mitigation: Run profile and quote first, then execute paid commands only after the user explicitly approves the quoted requestId.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/weekly-operator)
- [Amazon weekly ASIN operation workflow](references/operation-workflow.md)
- [Amazon weekly ASIN API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence notes, action priorities, and optional CLI command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis or collection.]

## Skill Version(s):

1.4.13 (source: release metadata, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
