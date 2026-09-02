## Description:

Qinghu AI image upscaling skill uses a tiled upscaling workflow to enlarge and clarify a single image while preserving the original content, texture, and style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to upscale, sharpen, and restore detail in one authorized image at a time for product, portrait, scenery, print, or old-photo workflows. It is for enlargement and detail repair, not style transfer or content alteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected image is uploaded to Qinghu AI through qhkit for processing.

Mitigation: Use only images the user owns or is authorized to process, avoid sensitive images unless appropriate, and explain that the workflow sends the image to Qinghu AI.

Risk: The workflow uses an API key and paid Qinghu credits.

Mitigation: Store credentials in a managed secret or temporary API key, run an estimate before generation, and wait for explicit user confirmation before submitting any paid job.

Risk: The skill depends on local qhkit and Node setup.

Mitigation: Install qhkit only from the declared npm package, keep the CLI updated, and surface installation or configuration errors to the user instead of retrying blindly.

Risk: Images larger than the supported limit can fail or require local compression.

Mitigation: Resize oversized images to within the documented limit before retrying, and do not repeatedly resubmit the same failing file.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-image-upscale-detail)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON qhkit parameters; completed workflow results are returned as image URLs in qhkit status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One input image per generation; the agent checks options, estimates credits, obtains user confirmation, submits the workflow, polls status, and reports actual credit usage.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
