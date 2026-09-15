## Description:

Generates a user-confirmed Amazon single-ASIN weekly operations brief that summarizes recent product changes, review signals, and action items for one subscribed product.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and developers use this skill to prepare a weekly operational brief for a subscribed Amazon ASIN, including product-change context, review evidence, and next actions. The workflow checks ARI capabilities, profile data, and quote details before any confirmed paid run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can request product-operation workflows beyond the fixed weekly/asin path if those options are supplied.

Mitigation: Review before installation when strict single-purpose behavior is required, and operate it only through the documented weekly/asin workflow with the ops_weekly output template.

Risk: The skill contacts ARI, stores or reads an ARI API key, checks account and credit status, and can charge credits.

Mitigation: Use the quote step first and proceed with paid collection or analysis only after explicit user confirmation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/weekly-operator)
- [Amazon single-ASIN operations workflow](artifact/references/operation-workflow.md)
- [Amazon single-ASIN operations API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and ARI quote, status, and report output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection and analysis actions require a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
