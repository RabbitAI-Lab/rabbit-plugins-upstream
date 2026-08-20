## Description:

青虎AI 爆款视频模仿（女装） helps an agent guide users through uploading a reference video and model image, estimating cost, submitting a Qinghu workflow, polling for completion, and returning the generated women's fashion motion-transfer video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create women's fashion short videos by transferring motion from an authorized reference video onto a supplied model image through Qinghu AI's paid workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads user-provided reference videos and model images to Qinghu AI.

Mitigation: Use only media and likenesses the user owns or is authorized to process, and make the upload requirement clear before submission.

Risk: The workflow is paid and charges by video duration.

Mitigation: Run the estimate step with the same parameters before generation, report the returned credits, and wait for user confirmation before submitting.

Risk: Generated video jobs are asynchronous and may take significant time.

Mitigation: Return the logId after submission and poll status until completion before presenting generated media URLs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-womens)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs and a final Qinghu credit-consumption line after workflow completion.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
