## Description:

Organizes Amazon review pain points, product fields, and usage context into verifiable product requirements and acceptance questions; it does not support delivery commitments, procurement, or sales forecasts and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and product teams use this skill to turn Amazon review evidence into product requirement drafts and acceptance questions after checking available data and cost. It is intended for requirements organization only, not engineering schedules, procurement actions, sales forecasts, inventory claims, advertising claims, or profit predictions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires the agent to hold an ARI API key.

Mitigation: Install only in environments where the agent is allowed to access that ARI credential, and remove or rotate the key when access is no longer needed.

Risk: The skill can trigger credit-spending ARI jobs.

Mitigation: Check the quote and requestId before running paid operations, and proceed only after explicit user confirmation.

Risk: Custom workflow or focus values can move execution outside the narrow product requirements workflow.

Mitigation: Use the documented product/requirements defaults unless a non-default ARI workflow is intentionally requested and reviewed.

## Reference(s):

- [Amazon Product Requirements Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Product Requirements API Reference](artifact/references/reference.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/product-requirements)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence summaries, acceptance questions, and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before credit-spending operations.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact changelog, artifact metadata, and CLI version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
