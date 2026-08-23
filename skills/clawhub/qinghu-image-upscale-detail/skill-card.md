## Description:

This skill helps agents use Qinghu AI to upscale and sharpen one image at a time while preserving the source image content and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route product, portrait, landscape, print, or restoration images through Qinghu AI image upscaling. It is intended for one-image-at-a-time enhancement workflows where the agent checks options, estimates cost, obtains confirmation before paid generation, polls status, and returns the completed image output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads the selected image to Qinghu/AutoAGC for processing.

Mitigation: Use it only for images the user is comfortable uploading and has the right to process.

Risk: Generation can consume Qinghu credits.

Mitigation: Run an estimate first and require explicit user confirmation before invoking paid generation.

Risk: The workflow depends on the qhkit CLI and a Qinghu API key.

Mitigation: Install qhkit from the documented npm package and configure credentials only when the user accepts that dependency.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Image URLs]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated image URLs after qhkit workflow completion; paid generation requires an estimate and explicit user confirmation.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
