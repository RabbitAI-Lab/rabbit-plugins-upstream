## Description:

Uses main-ASIN and authorized competitor product fields, images, and review evidence to identify verifiable Amazon product differentiation directions and open validation questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators, product teams, and developers use this skill to compare a main Amazon ASIN with authorized competitor ASIN evidence and produce differentiated product-positioning directions. It is for discussion and validation planning, not market sizing, sales forecasting, advertising, inventory, order, or profit decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags that broader server-approved operation workflows may be accepted than the advertised fixed product-differentiation workflow.

Mitigation: Review the package before installing and avoid workflow or focus overrides unless a future package documents and constrains them clearly.

Risk: Using the skill sends product identifiers and analysis requests to ari.funewa.com and requires saving an ARI API key locally.

Mitigation: Use it only when the publisher and ARI service are trusted, keep the ARI API key protected, and avoid submitting sensitive product data beyond the intended ASIN analysis context.

Risk: Paid collection or analysis can consume credits after confirmation.

Mitigation: Check the quote first and run paid actions only after explicit user confirmation with the returned requestId.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/differentiation)
- [Amazon 产品差异化机会 API 参考](references/reference.md)
- [Amazon 产品差异化机会 专属运营工作流](references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence gaps, and inline shell commands when advanced CLI use is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are grounded in collected product and review samples; paid analysis requires quote review and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release metadata, CHANGELOG, _meta.json, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
