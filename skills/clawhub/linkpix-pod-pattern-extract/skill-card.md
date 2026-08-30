## Description:

一键提取图片中的印花图案，生成高清、平铺、可复用的图案素材，适用于 POD 定制及服装设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, POD sellers, and design operators use this skill to turn product or worn-garment images into reusable flat bitmap pattern drafts. Agents use it to guide qhkit setup, collect user approval for generation parameters and credit cost, run the image workflow, and return generated pattern outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install or upgrade qhkit and supporting runtime tools.

Mitigation: Confirm the user is comfortable with installing qhkit and related tooling before setup.

Risk: Selected input images are uploaded to the provider for generation.

Mitigation: Ask the user to approve the exact images and generation parameters before running a generate command.

Risk: Generation requires an API key and may consume credits.

Mitigation: Use the documented estimate and approval step before generation, and avoid exposing the API key in responses or logs.

Risk: Generated pattern details may differ slightly from the source image.

Mitigation: Tell the user to review key visual elements, colors, and design details before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [LinkPix workspace](https://www.iqinghu.com)
- [LinkPix API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown, Image URLs]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow may return generated image URLs and credit usage after user approval.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
