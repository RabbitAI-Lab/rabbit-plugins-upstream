## Description:

Token-efficient assistant discipline for concise answers and task execution; includes optional file and Windows encoding utilities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phoenixlucky](https://clawhub.ai/user/phoenixlucky)

### License/Terms of Use:

GPL-3.0

## Use Case:

Developers and agent users use ZeroToken to guide AI assistants toward concise planning, targeted context gathering, minimal tool use, and short actionable outputs. It also provides optional utilities for environment detection and text encoding repair.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence tool choice and guide local file reads, writes, recursive scans, or encoding conversions.

Mitigation: Review proposed file operations before execution and require an explicit user request before recursive rewrites or environment-cache use.

Risk: Publishing and git workflows can affect public releases or repository history.

Mitigation: Require an explicit user request before any publish, git push, or commit-oriented workflow.

Risk: Environment detection caches host metadata locally.

Mitigation: Use cached environment metadata only for requested environment-aware command execution and avoid sharing host details unnecessarily.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/phoenixlucky/skills/zerotoken-skill)
- [Unicode encoding specification](docs/unicode-encoding-spec.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown text with optional code blocks and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise by default; may include local file edits or encoding reports when explicitly requested.]

## Skill Version(s):

1.13.2 (source: SKILL.md frontmatter, package.json, CHANGELOG released 2026-08-28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
