## Description:

Guides an agent through LinkPix/qhkit workflows for generating e-commerce product videos, short selling videos, brand promos, advertising assets, AI scripts, storyboards, and multi-image video assembly for platforms such as TikTok, Douyin, Amazon, and Shopee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users, commerce teams, and developers use this skill to route product video requests to qhkit commands, choose current LinkPix models from live options, estimate credits when supported, confirm paid generation steps, and poll for completed video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can upload user-provided product images, videos, or audio to the qhkit/LinkPix service.

Mitigation: Use only media the user has chosen for upload and make the upload part of the generation parameters visible before submitting a job.

Risk: Generation can spend qhkit credits and submitted video tasks may not be cancellable.

Mitigation: Estimate credits when supported, summarize model, duration, orientation, reference assets, and expected cost, and wait for explicit user confirmation before running a generate command.

Risk: Live model catalogs, prices, and maintenance states can change.

Mitigation: Query qhkit options during the session and avoid treating artifact examples or dated snapshots as default model choices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/linkpix-ecom-video)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON command parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce task IDs, status summaries, video URLs, and credit estimates or actual credit usage when returned by qhkit.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
