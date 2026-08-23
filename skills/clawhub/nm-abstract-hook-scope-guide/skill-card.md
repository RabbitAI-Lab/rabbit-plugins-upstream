## Description:

Select hook scope (plugin, project, global) by audience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and plugin authors use this skill to decide whether Claude Code hooks belong in plugin, project, or global configuration based on audience, version-control expectations, and persistence needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sample logging hooks can capture raw tool input and expose sensitive project or user data.

Mitigation: Log only timestamps, tool names, or redacted summaries, and keep any local logs protected with appropriate file permissions.

Risk: Global hooks can affect every Claude Code session for the user.

Mitigation: Use global hooks only when cross-session behavior is intentional, and test them before relying on them broadly.

Risk: Adding a standard plugin hook file again through plugin configuration can create duplicate hook loading.

Mitigation: Let Claude Code auto-load the standard hooks/hooks.json file and reserve explicit hook configuration for additional hook files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-hook-scope-guide)
- [claude-night-market abstract plugin](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/settings)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, shell, and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.9.18 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
