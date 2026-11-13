## Description:

Guides an agent to create sourced, fact-checked 3D explainer videos with procedural three.js scenes, deterministic rendering, and visual quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and educators use this skill to build short 3D explainers of scientific or technical subjects. It structures the work around sourced facts, a part-by-part scene, readable labels, deterministic rendering, and visual QA.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthenticated render server may expose files and allow traversal into sibling directories.

Mitigation: Run it only in a dedicated project directory where it cannot access sensitive files.

Risk: The security scan was partial: 16 of 23 components were fully inspected, 7 were partial, and binary fonts were outside analyzer scope.

Mitigation: Review the remaining files and binaries before installation; treat the suspicious verdict as a review warning, not an attribution of malicious intent.

Risk: Optional narration may be shared with an external speech service.

Mitigation: Use narration only for content you are comfortable sharing with that service.

Risk: The security guidance flags an unpinned installer as a trust consideration.

Mitigation: Review the installer and pin its source and version before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vargai/skills/code-3d-explainer)
- [Fact sheet guide](artifact/references/fact-sheet.md)
- [Accuracy critic prompts](artifact/references/critic-prompt.md)
- [Build and camera guide](artifact/references/build-and-camera.md)
- [Labels and readability guide](artifact/references/labels.md)
- [Rendering guide](artifact/references/render.md)
- [Subject-specific guidance](artifact/references/subjects.md)
- [Optional narration guide](artifact/references/narration.md)
- [varg.ai skill guide](https://varg.ai/how-to/skills/code-3d-explainer)

## Skill Output:

**Output Type(s):** [Code, Configuration, Markdown, Shell commands, MP4 video]

**Output Format:** [A project containing JavaScript or TypeScript, HTML, JSON, Markdown, and a rendered MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a sourced fact sheet, label and fact checks, and contact sheets; rendering targets 1920×1080.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
