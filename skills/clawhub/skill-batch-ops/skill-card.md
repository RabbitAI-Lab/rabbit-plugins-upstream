## Description:

Skill Batch Operations guides agents through batch inventory, patching, publishing, version alignment, and verification across three or more agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to coordinate batch operations over three or more skills, including inventory, version selection, platform publishing, GitHub sync, and per-item verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch changes can apply incorrect versions or publish unintended skill changes across multiple skills.

Mitigation: Prepare an explicit target list, review each batch change before publishing, and verify each installed skill against the published source.

Risk: GitHub synchronization may require token handling.

Mitigation: Use a least-privilege GitHub token stored outside logs and shell history, and rotate it if exposure is suspected.

Risk: Platform rate limits or occupied versions can cause partial or inconsistent publishes.

Mitigation: Query latest platform versions before choosing targets, use explicit publish parameters, respect publish spacing, and record item-level failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/skill-batch-ops)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and concise operational guidance with inline commands or code when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes per-skill status, failures, and unified version information.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
