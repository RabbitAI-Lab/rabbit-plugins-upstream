## Description:

Helps brand teams, ecommerce designers, and media buyers use Qinghu AI/LinkPix Seedance 2.5 through qhkit to generate product promotion, beauty review, and ecommerce ad videos from prompts and reference media.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce and brand teams use this skill to prepare short-form product videos, product-page media, and paid ad creatives with Seedance 2.5 via Qinghu AI/LinkPix. The agent checks available models, estimates credit usage when supported, confirms paid generation parameters, submits qhkit jobs, polls task status, and returns generated video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads user-selected product images, videos, or audio to Qinghu/AutoAGC for video generation.

Mitigation: Use only media approved for Qinghu/LinkPix processing and avoid submitting confidential or unlicensed assets.

Risk: Video generation can spend credits after a task is submitted.

Mitigation: Run the supported estimate command and require explicit user approval of model, duration, orientation, reference media, and expected credits before generation.

Risk: The workflow may install or update the qhkit CLI before use.

Mitigation: Install qhkit only when the user intends to use Qinghu/LinkPix and follow the documented package manager or checksum verification steps for prerequisites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-seedance-25-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return task IDs, credit estimates, status JSON, and generated video URLs after user-confirmed paid generation.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
