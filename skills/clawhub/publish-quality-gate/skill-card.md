## Description:

Checks skill, expert-pack, document, and tool release packages before publication for sensitive information and supports post-release TRACE self-assessment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this agent skill to run local release-quality checks before sharing or publishing an artifact, then use TRACE dimensions for post-release self-assessment. It is an auxiliary quality gate and does not replace human review for compliance or regulated decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A passing scanner result may not prove every release artifact was inspected, especially unsupported files, nested archives, images, PDFs, Office documents, or unreadable targets.

Mitigation: Manually verify unsupported and nested content before publishing, and treat the scan as one release check rather than complete assurance.

Risk: Install guidance includes a mutable global npx command path.

Mitigation: Use a trusted, pinned installer source or manually inspect and install the release artifact before use.

Risk: The authoritative license is inconsistent across server metadata and artifact files.

Mitigation: Confirm whether MIT-0 or MIT governs this release before public distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/publish-quality-gate)
- [Publisher profile](https://clawhub.ai/user/zhaoxinghua09-cell)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and human-readable scan results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Exit codes indicate pass, finding, or usage/environment error when the bundled scanner is run directly.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
