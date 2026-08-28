## Description:

A general-purpose anti-shallow AI output rules engine that prompts agents to analyze first, execute after, and self-check on complex or rigor-sensitive tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, writers, and other agent users use this skill to reduce shallow answers on tasks that need correctness, root-cause analysis, verification, or careful execution. It guides the agent toward structured analysis, confidence labeling, user confirmation for complex work, and final self-checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can broadly change an agent's response style by adding analysis, confirmation checkpoints, confidence labels, and self-checks.

Mitigation: Install it only where that posture is desired, and prefer scoped installation with --agent or --dir instead of -g for broad multi-agent rollout.

Risk: The rules can add process overhead for complex tasks and may affect workflows where the user expects a short direct answer.

Mitigation: Use the documented closing and explicit-instruction paths for simple or results-only work, while retaining the baseline requirement to state uncertainty and avoid unverified completion claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-anti-shallow)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-anti-shallow)
- [README](README.md)
- [Chinese README](README.zh-CN.md)
- [Changelog](CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Natural-language and Markdown responses, with code or shell command blocks when the user's task requires them.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May add analysis, confidence labels, confirmation checkpoints, and self-check summaries depending on task complexity.]

## Skill Version(s):

1.3.3 (source: frontmatter, CHANGELOG, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
