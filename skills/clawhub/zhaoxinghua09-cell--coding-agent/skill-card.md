## Description:

Delegates coding work to Codex, Claude Code, or OpenCode as background worker processes for large refactors, PR review, and similar coding tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to plan delegation of long-running coding tasks such as large refactors, automated PR review, and background feature work to coding agents while preserving an audit trail of agent, instruction, and change evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on generic coding-agent wording and gives limited operational safeguards for running background coding agents.

Mitigation: Review any separate agent commands or workflows before use, and require human review of delegated code changes before merge or deployment.

Risk: Background coding delegation can produce incorrect or misleading guidance or code changes if task scope and acceptance criteria are vague.

Mitigation: Provide bounded instructions, preserve audit evidence for agent actions and changes, and validate results with tests and code review.

## Reference(s):

- [coding-agent ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/coding-agent)
- [Publisher profile: zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with optional inline commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports multilingual responses in zh-CN, en, ja, ko, es, fr, de, and ar when requested.]

## Skill Version(s):

1.0.0 (source: frontmatter, manifest, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
