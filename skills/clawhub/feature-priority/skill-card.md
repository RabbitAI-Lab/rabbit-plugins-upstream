## Description:

Ranks product improvement features using Amazon review frequency, experience impact, and product information; it is limited to feature prioritization and does not forecast sales, approve budgets, or execute purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External product teams, sellers, and operators use this skill to prioritize Amazon product feature improvements from review evidence after supplying an ASIN and marketplace. It helps compare likely customer impact while keeping paid analysis behind an explicit quote-and-confirm step.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the CLI can override the fixed feature-priority workflow and run other server-supported paid operations.

Mitigation: Review operations before confirmation, keep use scoped to the documented feature-priority workflow, and avoid workflow or focus overrides unless broader ARI capabilities are intentionally needed.

Risk: The skill requires an ARI API key and contacts ari.funewa.com for Amazon product review analysis.

Mitigation: Install only when ARI API access is acceptable, keep API keys managed by the documented setup or configuration flow, and do not proceed with paid runs until the quote is reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/feature-priority)
- [Amazon Feature Priority Operational Workflow](artifact/references/operation-workflow.md)
- [Amazon Feature Priority API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and CLI-backed analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and user confirmation before paid analysis runs.]

## Skill Version(s):

1.4.13 (source: server evidence, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
