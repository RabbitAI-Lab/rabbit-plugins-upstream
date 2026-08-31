## Description:

元阁 yotta-skills routes agent tasks to YottaMeta skill combinations, inventories installed skills, and provides a one-command installer and updater for the yotta-* skill family.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to choose appropriate YottaMeta skill combinations for a task, install or update selected yotta-* skills into a target agent or directory, and keep a local skill registry current.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer can download npm packages and replace skill directories in a chosen target.

Mitigation: Use dry-run first, pin versions when reproducibility matters, confirm the target directory, and scan packages before installation.

Risk: The skill asks agents to persist future orchestration behavior in memory files.

Mitigation: Allow edits to AGENTS.md, CLAUDE.md, or similar persistent files only when you explicitly want future sessions to follow those rules.

Risk: Routing output can be mistaken for permission to install or auto-apply skills.

Mitigation: Treat routing as a recommendation, require user confirmation for installs and application-mode changes, and review high-risk workflows before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [YottaMeta Publisher Profile](https://clawhub.ai/user/yottameta)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [Orchestration Reference](references/orchestration.md)
- [Install Flow](references/install-flow.md)
- [Skill List](references/skill-list.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, and shell command suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Route outputs may include candidate combinations, call order, roles, confidence, rationale, installed or missing status, and install commands; installer outputs summarize success, skipped, and failed items.]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
