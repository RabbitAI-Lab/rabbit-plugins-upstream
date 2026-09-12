## Description:

Tool Call Guard helps agents classify proposed tool calls by side-effect risk and return allow, confirm, or block guidance before execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to add a pre-execution review step for file, network, database, messaging, and payment tool calls. It is intended to flag higher-risk actions such as writes, sends, deletes, and payments for human confirmation instead of silent execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled classifier may be treated as a reliable enforcement gate even though the security evidence describes it as advisory.

Mitigation: Review classifications before execution and keep independent approval controls for delete, send, payment, and other irreversible tools.

Risk: Broad global installation from an unpinned source could influence future agent behavior.

Mitigation: Install from a reviewed local copy or a trusted pinned version, and verify the exact source before global installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/tool-call-guard)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [LGD theory](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with optional plain text or JSON command output from the bundled classifier]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The classifier is zero-dependency and returns a risk level, decision, reason, and matched keywords.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; packaged SKILL.md frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
