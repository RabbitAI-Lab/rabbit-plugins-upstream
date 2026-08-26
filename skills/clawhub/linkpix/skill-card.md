## Description:

LinkPix guides an agent to use qhkit for Qinghu/LinkPix ecommerce media workflows, including product images, ad creatives, short videos, video translation, watermark and subtitle removal, storyboards, POD assets, and workflow task status checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to translate ecommerce creative requests into qhkit commands for Qinghu/LinkPix media generation and editing. It covers selecting live options, estimating credit cost, confirming paid submissions, uploading chosen media, and returning generated image, video, text, or task-status results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can submit paid Qinghu/LinkPix media-generation jobs that consume credits and may not be cancellable after submission.

Mitigation: Run estimate where supported, present model or template, count or duration, quality, language, referenced media, and expected credits, then wait for explicit user confirmation before any generate or storyboard script action.

Risk: The skill uploads user-selected images, videos, or audio files to Qinghu/LinkPix services for processing.

Mitigation: Upload only the files the user selected for the task, avoid broad file globs, and confirm sensitive or private media before sending it to the service.

Risk: The skill installs and uses the qhkit command-line package and may install Node when it is missing.

Mitigation: Prefer the npm official source for qhkit, verify Node downloads with the official SHA256 sums before unpacking, and fall back to mirrors only for network access as described by the artifact.

Risk: Live model and template catalogs can change, so stale model names, prices, or capability assumptions may produce incorrect commands.

Mitigation: Use qhkit options to fetch the current catalog before selecting models or templates, and use estimate rather than static documentation values when reporting credit cost.

Risk: The skill requires an API token for Qinghu/LinkPix access.

Mitigation: Configure the token through qhkit config or QHKIT_TOKEN, keep it out of public outputs, and show only masked configuration during self-checks.

## Reference(s):

- [ClawHub LinkPix Skill Page](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu Workbench](https://www.iqinghu.com)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text, Markdown, Code]

**Output Format:** [Markdown guidance with inline qhkit shell commands and JSON parameters; generated service results are returned as URLs, text fields, task IDs, or status JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires qhkit and a Qinghu API token; paid generate/script actions require estimate and explicit user confirmation before submission.]

## Skill Version(s):

0.1.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
