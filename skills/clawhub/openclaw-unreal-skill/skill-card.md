## Description:

Controls Unreal Engine Editor via the OpenClaw Unreal Plugin for level and actor management, transforms, PIE control, debugging, input simulation, console commands, screenshots, and logs, with project-changing operations gated by operator opt-in and per-call confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and technical artists use this skill to inspect and control trusted local Unreal Engine Editor projects through OpenClaw, including level, actor, transform, editor state, debug, input, asset, console, and blueprint workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The legacy gateway compatibility path can expose an unauthenticated command broker for connected Unreal sessions.

Mitigation: Install only with a modern OpenClaw gateway that supports authenticated plugin routes and keep gateway access limited to trusted local components.

Risk: Project-changing Unreal operations can alter actors, levels, assets, console state, input, or Play In Editor state.

Mitigation: Leave destructive operations blocked by default; enable them only with the operator opt-in environment variable and require per-call confirm: true after user approval.

Risk: Screenshots, logs, and Unreal session details can expose sensitive project data, credentials, tokens, or local paths.

Mitigation: Treat screenshots and logs as sensitive and review them before sharing outside the trusted local environment.

## Reference(s):

- [OpenClaw Unreal Skill on ClawHub](https://clawhub.ai/tomleelive/skills/openclaw-unreal-skill)
- [OpenClaw Unreal Plugin](https://github.com/openclaw/openclaw-unreal-plugin)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [CHANGELOG.md](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dry-run previews, editor status guidance, and safety confirmation wording before project-changing Unreal operations.]

## Skill Version(s):

1.1.0 (source: SKILL.md frontmatter, CHANGELOG.md, extension/package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
