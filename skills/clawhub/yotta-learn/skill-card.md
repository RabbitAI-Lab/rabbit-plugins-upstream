## Description:

Yuanxi yotta-learn captures mistakes, corrections, feature requests, and practical insights as reusable project-local .learnings/ entries for later agent sessions and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to record lessons from command failures, user corrections, stale knowledge, missing capabilities, and external-interface issues, then review, promote, or extract those entries into future guidance or skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent learning logs can capture tokens, keys, private data, full source files, or sensitive incident details if users include them in entries.

Mitigation: Record only summaries or deliberately redacted details unless the user explicitly approves storing sensitive content.

Risk: The optional UserPromptSubmit hook templates run review broadly and can affect every prompt submission when enabled.

Mitigation: Review and narrow hook configuration before enabling automatic review behavior.

Risk: Unpinned npm installation can reduce supply-chain repeatability.

Mitigation: Use a pinned npm package version when reproducible installation is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [README](README.md)
- [Chinese README](README.zh-CN.md)
- [Learning entry examples](references/examples.md)
- [Hook setup](references/hooks-setup.md)
- [Hook guide](hooks/README.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-learn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown learning-log entries, command guidance, generated skill skeleton files, and optional hook configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local .learnings/ files and may update AGENTS.md or CLAUDE.md only when the user runs promote.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
