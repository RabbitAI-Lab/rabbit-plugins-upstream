## Description:

Helps e-commerce merchants, designers, and store operators create Vidu Q3 product marketing videos through Qinghu AI/qhkit, including model discovery, media upload, cost estimation, task polling, and result delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce teams use this skill to turn product images and selling points into short product, listing, and advertising videos with Vidu Q3 or the closest available qhkit video model. It guides setup, parameter selection, user confirmation before paid generation, status checks, and delivery of generated video links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require installing qhkit through npm or npx, which can affect the local execution environment.

Mitigation: Review the package source and install only in a trusted or isolated environment; prefer controlled package versions and avoid unpinned global installs when possible.

Risk: The skill asks for Qinghu API credentials and may persist them for qhkit use.

Mitigation: Use scoped secret storage or environment variables where available, and avoid pasting API keys into chat or logs.

Risk: Video generation uploads media to the provider and can consume paid credits.

Mitigation: Confirm model, duration, reference media, orientation, and estimated credits before submitting generation tasks, and avoid uploading sensitive media.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/linkpix-vidu-q3-sales)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)
- [Qinghu API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit task IDs, status summaries, video URLs, and credit estimates or charges.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
