## Description:

青虎AI 电商工作流应用通过 qhkit workflow 帮助 agents 选择、报价、提交并轮询青虎工作台的电商视频、图片处理和数据追踪工作流。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route ecommerce creative and data-tracking requests to Qinghu AI workflows, including video imitation, TVC ad generation, model image editing, super-resolution, watermark removal, and short-video or creator data tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install and use the external qhkit CLI service.

Mitigation: Install only when the user intends to use Qinghu cloud workflows and understands the external service dependency.

Risk: Workflow generation may require a Qinghu API key, uploaded media, and paid credit usage.

Mitigation: Confirm selected workflow, input media, parameters, and estimated credits with the user before submitting generation jobs.

Risk: User-provided media may be uploaded to Qinghu services for processing.

Mitigation: Use only media the user owns or is authorized to process, and clarify upload implications before generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-workflow-apps)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI](https://www.iqinghu.com)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON request or status payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce workflow selection advice, parameter summaries, credit estimates, log IDs, status updates, and generated media URLs from the Qinghu service.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
