## Description:

voc-amazon helps an agent collect and analyze Amazon reviews through ARI, producing voice-of-customer insights such as pain points, buying motives, user profiles, scenarios, trends, competitor comparisons, and listing suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and analysts use this skill to turn Amazon ASIN review data into concise VOC summaries, deeper reports, trend checks, alerts, exports, and operational recommendations. It requires an ARI API key and may run paid ARI collection or analysis workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run paid ARI collection or analysis workflows, and documented auto-confirm behavior may spend credits without a fresh confirmation for each operation.

Mitigation: Use the skill only with an ARI account you intend to authorize; before routine use, request confirmation before every paid action or use quote-only language when pricing is needed without spending credits.

Risk: Reports and recommendations depend on ARI-collected Amazon review samples, which may not cover all reviews, variants, or time periods.

Mitigation: Read conclusions with the stated sample range and require the agent to call out small samples, limited windows, and trend uncertainty.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/voc-amazon)
- [README](artifact/README.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Account and API Keys](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and conversational text with inline shell commands; exported reports may be Markdown, HTML, or CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are based on ARI-collected Amazon review samples and should include sample range, evidence, cost or credit usage when relevant, and uncertainty for limited data.]

## Skill Version(s):

1.4.11 (source: server release metadata, SKILL.md frontmatter, _meta.json, and CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
