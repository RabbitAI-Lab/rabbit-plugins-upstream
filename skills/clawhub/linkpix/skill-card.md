## Description:

LinkPix helps agents use the qhkit CLI to create ecommerce images, videos, scripts, storyboards, POD artwork, media edits, translations, and Qinghu workflow outputs with status tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use LinkPix to translate ecommerce media requests into qhkit commands for generating product imagery, ad videos, storyboards, translated or edited videos, POD assets, and Qinghu workflow results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install or upgrade qhkit and reuse an existing Qinghu/OpenClaw token.

Mitigation: Require explicit user approval before installing or upgrading software and before using stored credentials; keep token values out of outputs.

Risk: Selected local images, videos, audio, and workflow estimate inputs may be uploaded to Qinghu services.

Mitigation: Confirm the exact files and purpose with the user before estimates or generation, especially for private media.

Risk: Face replacement, de-watermarking, subtitle removal, and dubbing features can be misused on media without proper rights.

Mitigation: Use these features only for media the user owns or has permission to process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown]

**Output Format:** [Markdown instructions with qhkit command examples and JSON command parameters; generated runs may return media URLs, task IDs, scripts, text, files, or status JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected local media through qhkit; generation actions can consume credits and require user confirmation.]

## Skill Version(s):

0.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
