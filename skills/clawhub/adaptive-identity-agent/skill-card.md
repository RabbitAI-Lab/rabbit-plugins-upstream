## Description:

A conversational agent skill that adapts and stacks expert-style identities across 12 dimensions, supports @ identity invocation, and maintains memory threads for multi-domain task handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangjiaocheng](https://clawhub.ai/user/wangjiaocheng)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this conversational skill to switch or combine task-relevant expert perspectives for cross-domain analysis, creative transformation, and structured response planning. The skill is suited to sessions that require explicit persona boundaries, @-invoked identities, or continuity across related task threads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests Bash, Write, and Edit permissions even though its primary behavior is conversational and mostly read-only.

Mitigation: Restrict tool permissions before installation unless local command execution or file edits are specifically required for the deployment.

Risk: Adaptive expert personas can make generated guidance sound more authoritative than the underlying evidence supports.

Mitigation: Keep identities framed as perspectives, require uncertainty labels for unverifiable claims, and preserve the artifact's rule against claiming real credentials or institutional roles.

## Reference(s):

- [Character Data](references/character-data.md)
- [Character Requirements](references/character-requirements.md)
- [Dialogue Examples](references/dialogue.md)
- [Identity Matrix](references/identity-matrix.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style conversational responses with identity-stack labels and structured sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include role labels, uncertainty notes, source prompts, diagrams or scripts as task-appropriate text.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
