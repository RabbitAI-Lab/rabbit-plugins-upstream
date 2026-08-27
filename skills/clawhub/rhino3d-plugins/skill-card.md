## Description:

Rhino3D plugin and script development with the RhinoCommon SDK — .rhp plugins and commands, Grasshopper .gha components, Eto panels, dialogs and options pages, user data and document persistence, display conduits, render engine integration, Python scripting, and yak packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhauga](https://clawhub.ai/user/jhauga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, debug, package, and document Rhino3D plugins, Grasshopper components, Eto UI surfaces, geometry workflows, and persistence features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated project settings, yak commands, startup-loaded plugins, and persistence code can affect a user's Rhino environment or saved files.

Mitigation: Review generated project settings and yak commands before running them, test in a disposable Rhino profile or sample model first, and keep backups of important .3dm files.

Risk: Placeholder GUIDs copied into plugin, UI, Grasshopper, render, or user-data code can cause identity collisions or orphan saved content.

Mitigation: Regenerate every placeholder GUID before building or shipping and keep released identifiers stable.

Risk: Publishing workflows may involve API keys or package ownership changes.

Mitigation: Use scoped secrets for CI publishing, avoid pasting credentials into generated files, and review package owner and push commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jhauga/skills/rhino3d-plugins)
- [Plugin Project Template](artifact/assets/plugin-project-template.md)
- [UI Patterns](artifact/assets/ui-patterns.md)
- [Persistence and User Data](artifact/scripts/persistence-and-userdata.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
