## Description:

Uses the Flyelep hot-video recreation API to generate a product video that follows the style, pacing, and visual approach of a reference video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and e-commerce operators use this skill to collect required video-generation parameters, submit a Flyelep hot-video recreation task, poll for completion, and return the generated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends product video URLs, reference video URLs, prompts, task metadata, and the Flyelep API key to Flyelep.

Mitigation: Use it only when third-party processing by Flyelep is acceptable, and avoid private or regulated media unless that processing has been approved.

Risk: Temporary request payload files can retain media URLs, prompts, and task data on disk.

Mitigation: Delete payload_temp.json after use whenever a temporary request file is created.

Risk: The Flyelep API key could be exposed if it is stored in examples, repositories, or persistent configuration.

Mitigation: Provide the key at runtime in the request header and do not persist real credentials in skill files or shared examples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/gen-hot-video)
- [Flyelep API key console](https://www.flyelep.cn/controlboard)
- [Flyelep generateHotVideo endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/generateHotVideo)
- [Flyelep queryTaskResult endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, JSON, Configuration]

**Output Format:** [Markdown guidance with JSON request bodies and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns an asynchronous task ID first, then a generated video URL after polling succeeds.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
