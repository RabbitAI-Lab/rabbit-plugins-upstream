## Description:

Yotta-skills is a YottaMeta skill-family orchestration router, inventory tool, and one-command installer for selecting, installing, updating, and cataloging yotta-* agent skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to route a task to suitable YottaMeta skill combinations, install or update those skills into an agent or directory, and inventory locally installed skills before use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide durable changes to agent memory or MCP configuration.

Mitigation: Review the exact target files and approve persistent writes only when that behavior is intended.

Risk: The installer can download and replace skills in an agent or directory.

Mitigation: Use dry-run or pinned installs where appropriate, confirm target directories, and scan skills before installing or updating them.

Risk: Routing output may list other installed skills as unscanned candidates.

Mitigation: Treat those candidates as advisory, scan them before use, and require user confirmation before invoking or installing skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-skills)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-skills)
- [orchestration.md](references/orchestration.md)
- [install-flow.md](references/install-flow.md)
- [skill-list.md](references/skill-list.md)
- [tutorial.md](references/tutorial.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce installation commands, routing recommendations, local inventory summaries, registry updates, and optional MCP configuration guidance.]

## Skill Version(s):

0.5.0 (source: frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
