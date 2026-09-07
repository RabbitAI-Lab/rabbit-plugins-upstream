## Description:

Plans the information Amazon main and secondary product images should communicate from product details and review friction; it does not generate image files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and product operators use this skill to inspect product details and review issues, quote and run ARI product-operations analysis, and produce guidance for what listing images should communicate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release appears broader than its image-planning label and can perform account-connected ARI review operations.

Mitigation: Use it only when a broad Amazon review and product-operations assistant is intended, and verify the connected ARI account, marketplace, credit balance, and export locations before use.

Risk: Paid or account-management actions may spend credits or alter monitoring behavior.

Mitigation: Review auto-confirm settings and disable auto-confirm when every paid action should require explicit approval.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/image-planner)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [User Guide](artifact/使用说明.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with ARI CLI command snippets, account-status summaries, report links, and image-planning guidance when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires ARI API key access and may reference ARI account state, credit usage, monitoring settings, exported files, and report URLs.]

## Skill Version(s):

1.4.7 (source: server release, SKILL.md frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
