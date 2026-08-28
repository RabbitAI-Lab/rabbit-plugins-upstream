## Description:

Yuanxi is a cross-agent learning-loop skill that captures mistakes, corrections, feature requests, and reusable insights as project-local .learnings/ entries for later review, promotion, statistics, and skill improvement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent users, and multi-agent teams use this skill to record command failures, user corrections, stale knowledge, external-interface failures, and better practices so later sessions can review, aggregate, and reuse them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists project learning notes that may accidentally include secrets, full source, environment values, or other sensitive information.

Mitigation: Follow the documented boundary and scanner guidance: do not log secrets or full source; use summaries or redacted snippets unless the user explicitly requests otherwise.

Risk: Broad installation or hook enablement can add persistent behavior across multiple agent environments.

Mitigation: Prefer scoped installation with --agent or --dir, and review hook templates before merging them into Claude Code, Codex, or OpenClaw settings.

Risk: Promoting unreviewed learning entries into AGENTS.md or CLAUDE.md-style instruction files can turn local observations into durable agent instructions.

Mitigation: Promote only trusted, reviewed entries and keep sensitive or uncertain observations in local .learnings/ files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-learn)
- [GitHub repository](https://github.com/YottaMeta/yotta-learn)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-learn)
- [agentskills.io](https://agentskills.io/)
- [examples.md](references/examples.md)
- [hooks-setup.md](references/hooks-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown entries, command-line output, shell commands, and generated skill skeleton files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes project-local .learnings/ files; optional hook templates can be installed into agent settings; optional yotta-memory sync degrades without blocking local records.]

## Skill Version(s):

0.1.3 (source: SKILL.md frontmatter, package.json, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
