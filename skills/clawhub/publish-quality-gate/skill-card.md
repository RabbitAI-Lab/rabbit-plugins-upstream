## Description:

Helps review release packages for sensitive information before publishing and guides a separate post-release TRACE self-check.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and release owners use the skill to check selected folders or archives for sensitive information before sharing and to guide a manual post-release TRACE review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan results may expose sensitive values found in selected files.

Mitigation: Keep results private and redact sensitive values before sharing reports or logs.

Risk: A clean local scan does not establish complete release safety or finish a post-release TRACE review.

Mitigation: Manually inspect release materials and perform separate security and TRACE checks before relying on the result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Plain-text scan results and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Four-layer findings and exit status; TRACE self-check requires separate human review.]

## Skill Version(s):

1.0.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
