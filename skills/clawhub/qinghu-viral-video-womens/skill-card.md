## Description:

青虎AI 爆款视频模仿（女装） helps an agent upload a reference video and model image, estimate cost, submit a paid QinghuAI workflow, and poll for an AI-generated womenswear video that transfers the source video's motion to the supplied model image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create womenswear short-form commerce videos by applying the motion from an authorized reference video to a supplied model image. The skill guides setup, quoting, paid submission, status polling, and delivery through QinghuAI qhkit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-provided reference video and model image to QinghuAI/qhkit.

Mitigation: Confirm the user is comfortable sending those media files to the service before installation or generation.

Risk: The workflow uses a QinghuAI API key and submits paid generation jobs.

Mitigation: Use qhkit configuration or environment variables for credentials, run an estimate first, and submit generation only after explicit user confirmation.

Risk: Broad requests such as generic womenswear ads may not identify the exact authorized source media or desired workflow.

Mitigation: Clarify the requested source video, model image, and workflow before estimating or submitting generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [QinghuAI login](https://www.iqinghu.com/workbench/login?urlCode=agentch)
- [QinghuAI API keys](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [QinghuAI API key guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include qhkit command output summaries, cost confirmation prompts, generated media URLs, and final credit consumption when a workflow completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
