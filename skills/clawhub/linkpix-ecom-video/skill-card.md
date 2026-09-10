## Description:

Guides agents to generate e-commerce product, promotional, review, and spokesperson videos with LinkPix/qhkit, including prompt routing, script or storyboard preparation, one-click multi-image video generation, status polling, and delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn product prompts or selected local media into e-commerce videos for channels such as TikTok, Douyin, Amazon, and Shopee. The skill helps route broad video requests to qhkit commands for scripts, storyboards, cost estimates, generation, polling, and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or upgrade qhkit globally before use.

Mitigation: Require user confirmation before installation or upgrade, and prefer a pinned local qhkit install when possible.

Risk: Selected local images or videos may be uploaded to the LinkPix/qhkit service.

Mitigation: Confirm the exact files with the user before generation and avoid uploading sensitive or unintended media.

Risk: Video generation may consume service credits.

Mitigation: Run an available estimate command or clearly state when estimates are unavailable before submitting generation jobs.

Risk: Tool output may suggest upgrade commands during version gating.

Mitigation: Do not execute copied upgrade commands automatically; review and confirm the command source and package target first.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [iQinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected local media to the LinkPix/qhkit service, consume service credits, and return task IDs, status JSON, cost estimates, and generated video URLs.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
