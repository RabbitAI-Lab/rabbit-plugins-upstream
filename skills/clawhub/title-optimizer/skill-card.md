## Description:

Diagnoses gaps in Amazon product titles using product-detail and review evidence, then suggests title improvements without writing full listings, managing ads, or publishing changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill to review an ASIN's title against available product fields and review evidence, then receive concise title optimization guidance. It is intended for title diagnosis and recommendations, not full listing copywriting, advertising decisions, or automatic Amazon page changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports that the code can override the promised title-only workflow and run broader billable ARI operations.

Mitigation: Before confirming any paid run, verify the command uses the intended listing/title workflow and that the requestId matches the reviewed quote; do not pass custom workflow or focus values unless broader ARI operations are intended.

Risk: The skill requires a locally stored ARI API key and depends on the external ARI service.

Mitigation: Install only when the publisher and ARI service are trusted, and manage the API key according to local secret-handling practices.

## Reference(s):

- [Amazon Title Optimization Workflow](references/operation-workflow.md)
- [Amazon Title Optimization API Reference](references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/title-optimizer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence notes, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ASIN and site context plus an ARI API key; paid runs require quote review and explicit confirmation.]

## Skill Version(s):

1.4.13 (source: server release metadata, artifact _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
