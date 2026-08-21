## Description:

一键提取图片中的印花图案，生成高清、平铺、可复用的图案素材，适用于 POD 定制及服装设计。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and design operators use this skill to guide an agent through extracting printable pattern artwork from clothing or product images for POD and apparel design workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected images to an external qinghu service through the qhkit CLI.

Mitigation: Use only images the user is comfortable uploading and configure the qhkit token through the documented secure configuration path.

Risk: Generation tasks consume credits and cannot be canceled after submission.

Mitigation: Run an estimate when available, show the selected parameters and expected credit cost, and wait for explicit user confirmation before submitting generation.

Risk: Generated pattern extraction may differ slightly from the source image and brand or IP artwork can carry rights risks.

Mitigation: Ask the user to review key visual elements after generation and flag obvious brand or IP patterns before reuse.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-pod-pattern-extract)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQingHu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with qhkit CLI commands and JSON parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation can return image URLs and credit usage after user confirmation; read-only options and estimates do not spend credits.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
