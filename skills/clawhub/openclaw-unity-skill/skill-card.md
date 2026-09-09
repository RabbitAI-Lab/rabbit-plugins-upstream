## Description:

Controls the Unity Editor through OpenClaw for scene inspection, GameObject and component changes, debugging, input simulation, Play mode control, package and asset operations, and explicitly gated C# execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tomleelive](https://clawhub.ai/user/tomleelive)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and engineers use this skill to inspect, automate, debug, and test Unity projects through OpenClaw-connected Unity Editor tooling. It is intended for trusted local Unity projects where read-only inspection is routine and project-changing actions require explicit operator opt-in and per-call confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-provided custom tools with read-like names may be treated as read-only even if they mutate a Unity project.

Mitigation: Use the skill only in trusted, version-controlled Unity projects and review project-registered custom tools before relying on their classification.

Risk: Unity Editor automation and C# execution can change scenes, assets, packages, settings, or project files.

Mitigation: Keep destructive operations disabled unless needed, review C# before execution, require user approval for project-changing calls, and use dryRun previews when available.

## Reference(s):

- [Openclaw Unity Skill on ClawHub](https://clawhub.ai/tomleelive/skills/openclaw-unity-skill)
- [Unity Plugin Tools Reference](references/tools.md)
- [OpenClaw Unity Plugin Repository](https://github.com/TomLeeLive/openclaw-unity-plugin)
- [OpenClaw Docs](https://docs.openclaw.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands, code snippets, configuration examples, and Unity tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations and confirmation requirements for project-changing Unity Editor actions.]

## Skill Version(s):

1.7.0 (source: release metadata, SKILL.md frontmatter, extension/package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
