## Description:

Rhino3D plugin and script development with the RhinoCommon SDK for .rhp plugins and commands, Grasshopper .gha components, Eto panels, dialogs and options pages, user data and document persistence, display conduits, render engine integration, Python scripting, and yak packaging.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhauga](https://clawhub.ai/user/jhauga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, debug, package, and maintain Rhino3D plugins, Grasshopper components, Rhino scripts, UI surfaces, persistence features, and yak releases. It is especially useful when work depends on RhinoCommon SDK conventions, Rhino version targeting, document state, or plugin loading behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated plugin code may run inside Rhino, including startup loading, document or user persistence, localhost viewers, and external dependency behavior.

Mitigation: Review generated code carefully and build-test it before loading it in Rhino, with extra attention to startup hooks, persistence paths, localhost surfaces, and dependency handling.

Risk: Yak publishing workflows can involve package publishing credentials.

Mitigation: Keep yak API keys out of prompts, source files, and logs; use scoped CI secrets and review publishing commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jhauga/skills/rhino3d-plugins)
- [Plugin project template](assets/plugin-project-template.md)
- [UI patterns](assets/ui-patterns.md)
- [Persistence and user data](scripts/persistence-and-userdata.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces documentation-grounded development guidance and proposed implementation artifacts; generated code should be reviewed before use in Rhino.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
