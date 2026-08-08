## Description:

Uses the Flyelep asynchronous video generation API to create product or creative videos from text prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect video generation requirements, call Flyelep's asynchronous API, poll for task completion, and return the generated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends video prompts, referenced media URLs, and a Flyelep API key to Flyelep.

Mitigation: Use the skill only when that data sharing is acceptable, provide the API key at runtime, and avoid storing the key in files or logs.

Risk: Temporary payload files can contain request details or credentials when used for Windows or PowerShell execution.

Mitigation: Delete temporary payload files after the API call and avoid persisting generated request bodies beyond the active task.

Risk: Video generation is asynchronous and may return only a task ID before the final video is ready.

Mitigation: Poll the task result endpoint until a successful completion status is returned, and treat failures or timeouts as incomplete generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/generate-video)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [Flyelep generateVideo endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/generateVideo)
- [Flyelep queryTaskResult endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an asynchronous task ID first, then a generated video URL after polling succeeds.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
