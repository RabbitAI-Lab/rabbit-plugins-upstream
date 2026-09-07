## Description:

Plans Amazon A+ content modules, information hierarchy, and buyer-question responses from Amazon product details and review evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon operators and content teams use this skill to plan A+ content from product details and review evidence. It focuses on listing/A+ planning and excludes ad bidding, image production, and automatic page publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill label suggests A+ content planning, while the security review notes broader ARI account, billing, monitoring, export, and advertising-related capabilities.

Mitigation: Install only when a broad ARI account assistant is intended, and keep the user-facing task scoped to the requested A+ content planning workflow.

Risk: Some workflows can consume credits, change confirmation settings, or enable ongoing monitoring and collection.

Mitigation: Review billing and autoconfirm settings before use, require clear user confirmation for paid actions, and avoid enabling recurring collection or watches casually.

Risk: Exports and workbench/status changes may affect account data or local files.

Mitigation: Treat export, workbench, and status-changing actions as account-affecting operations and confirm intent before executing them.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/aplus-writer)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [README](README.md)
- [Amazon A+ Dedicated Operations Workflow](references/operation-workflow.md)
- [ARI CLI and API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional inline shell commands and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ASIN/site scope, evidence summaries, cost/confirmation status, report links, and account-safe next steps.]

## Skill Version(s):

1.4.7 (source: frontmatter, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
