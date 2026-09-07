## Description:

Organizes Amazon review pain points, product fields, and use cases into verifiable product requirements and acceptance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT

## Use Case:

Amazon marketplace operators and product teams use this skill to turn review evidence and product context into requirements-oriented analysis for listing and product improvement decisions. It is not intended for development schedule commitments, procurement execution, or sales forecasting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use and store an ARI API key and access ARI account, report, alert, and Amazon review data.

Mitigation: Install only after reviewing the skill, keep the API key out of chat and reports, and revoke or rotate the key from the ARI account page if access is no longer needed.

Risk: Some analysis, collection, leaderboard, advice, and monitoring workflows can spend credits or create ongoing collection costs.

Mitigation: Set autoconfirm to ask every time when explicit approval is required, use quote-only flows for pricing, and authorize schedule, watch, or competitor changes only after reviewing the returned cost and scope.

Risk: The security review flags broad ARI account, monitoring, export, and paid-analysis capabilities under a narrow product-requirements label.

Mitigation: Use the skill for requirements-focused Amazon review analysis only, and review requested operations before allowing account changes, exports, recurring monitoring, or paid analysis.

## Reference(s):

- [Operation Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)
- [Usage Guide](使用说明.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/product-requirements)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and conversational text, with shell commands only for setup, confirmation, or troubleshooting when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses ARI account data and Amazon review samples; paid analysis and recurring monitoring require the confirmation behavior described by the skill and service.]

## Skill Version(s):

1.4.7 (source: frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
