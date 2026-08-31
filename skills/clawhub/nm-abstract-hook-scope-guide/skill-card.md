## Description:

Select hook scope (plugin, project, global) by audience.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose whether Claude Code hooks belong in plugin, project, or global scope based on audience, version control, and persistence needs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Overbroad global hooks can affect every Claude Code session.

Mitigation: Choose the narrowest hook scope that fits the audience and persistence need before applying a hook pattern.

Risk: Logging tool input in hook examples can expose sensitive data.

Mitigation: Avoid logging sensitive tool input or redact it before writing logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-hook-scope-guide)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/abstract)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/settings)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration]

**Output Format:** [Markdown guidance with JSON and Python configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only guidance; it does not install or run hooks.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
