## Description:

Uses the Flyelep Image-2 asynchronous free-creation API to generate product or creative images from prompts and optional reference images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare authenticated Flyelep API requests, optionally upload local reference images, submit asynchronous Image-2 generation tasks, poll for task completion, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Flyelep secret key is required for API access and could be exposed if written into files, examples, logs, or persistent configuration.

Mitigation: Request the secret key at runtime, send it only in the request header, and avoid storing real credentials in skill files or durable configuration.

Risk: Reference images may be uploaded to Flyelep and converted into public URLs.

Mitigation: Upload only images the user is allowed to share with Flyelep, and treat returned upload URLs as publicly accessible.

Risk: Asynchronous generation tasks may remain pending or fail.

Mitigation: Poll the task result endpoint at reasonable intervals, surface failed task items to the user, and avoid assuming image URLs exist until the service reports success.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/async-free-creation)
- [Flyelep control board](https://www.flyelep.cn/controlboard)
- [Flyelep asynchronous creation endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/allAroundCreationAsync)
- [Flyelep task result endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep file upload endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns task identifiers, task status summaries, and generated image URLs when the external service completes successfully.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
