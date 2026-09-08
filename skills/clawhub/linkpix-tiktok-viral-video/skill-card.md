## Description:

Helps agents guide TikTok Shop sellers, MCNs, and ad operators through LinkPix/qhkit workflows for generating short vertical product videos from prompts and image assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External commerce and marketing users use this skill to create TikTok-oriented product, seeding, and ad videos with model selection, cost estimation, generation, polling, and delivery guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may install mutable npm tooling or use alternate package registries.

Mitigation: Review the package source and install in an isolated environment when possible; prefer pinned or reviewed versions for controlled deployments.

Risk: The skill can upload local media to Qinghu/LinkPix services.

Mitigation: Use only assets the user is authorized to upload and avoid sensitive, confidential, or regulated media unless the service terms and data handling are approved.

Risk: A Qinghu API token may be stored locally or exposed during configuration.

Mitigation: Use a limited API key, prefer environment-variable configuration where practical, avoid sharing tokens in chat logs, and rotate any token that may have been exposed.

Risk: Video generation can consume credits and submitted tasks may not be cancellable.

Mitigation: Run estimates when supported and obtain explicit user confirmation of model, duration, inputs, language, orientation, and estimated cost before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-tiktok-viral-video)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model options, estimated credits, task IDs, status updates, and generated video URLs.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
