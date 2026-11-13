## Description:

Build & headless-verify Godot 4.7 OpenXR/VR apps — room-scale workflow, Pimax Crystal tested in-visor, controller-binding pitfalls covered.

This skill is ready for commercial/non-commercial use.

## Publisher:

[blueboyzx](https://clawhub.ai/user/blueboyzx)

### License/Terms of Use:

MIT-0

## Use Case:

Developers building Godot 4 OpenXR applications use this skill to scaffold VR projects, troubleshoot controller bindings, and verify scenes through headless runs and screenshots. It is especially useful for Godot 4.7 workflows and Pimax Crystal controller issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags a file replacement procedure that could delete existing project files without warning.

Mitigation: Back up the target project, review the paths to be replaced, and confirm existing files can be removed before following replacement steps.

Risk: The security scan was partial because some referenced paths were missing, so its evidence is incomplete.

Mitigation: Review the skill and resolve or inspect the missing referenced paths before relying on its instructions.

## Reference(s):

- [Godot 4.7.2 API forms](artifact/references/godot-47-api.md)
- [XR controller troubleshooting](artifact/references/xr-controller-troubleshooting.md)
- [Godot VR on ClawHub](https://clawhub.ai/blueboyzx/skills/godot-vr)

## Skill Output:

**Output Type(s):** [Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Godot project files with GDScript and project configuration, plus Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Build and runtime verification guidance includes headless checks and a non-headless screenshot; headset behavior requires an in-visor check.]

## Skill Version(s):

1.0.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
