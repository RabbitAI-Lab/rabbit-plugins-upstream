## Description:

Creates code-built 3D explainer videos with sourced fact sheets, staged models, and rendering and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to build sourced, code-generated 3D explainers for scientific or technical subjects, then render and review the video and its on-screen text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports a potential directory traversal exposure.

Mitigation: Review file paths and output locations before running the scripts, and run them within the intended project directory.

Risk: The security review reports a weakness in the fact-checking gate, so automated checks may not catch every inaccurate claim.

Mitigation: Verify claims against their cited sources and review the completed fact sheet and video text independently.

Risk: The security review was partial, with some components not fully analyzed.

Mitigation: Inspect the remaining source files before installing or running the skill.

## Reference(s):

- [Fact sheet guidance](artifact/references/fact-sheet.md)
- [Critic review prompt](artifact/references/critic-prompt.md)
- [Building subjects and camera movement](artifact/references/build-and-camera.md)
- [Rendering guide](artifact/references/render.md)
- [Label and text checks](artifact/references/labels.md)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/code-3d-explainer)
- [Example animal-cell film](https://s3.varg.ai/files/4325c578-378d-4c43-ae53-3cc3218df1ea/file_b6dc1bd5642f.mp4)

## Skill Output:

**Output Type(s):** [Code, Markdown, Shell commands, Files]

**Output Format:** [Three.js project files, a sourced fact sheet, QA reports, and a rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes scripts and guidance for rendering, labels, and fact checks.]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
