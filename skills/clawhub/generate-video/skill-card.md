## Description:

Generates product or creative videos from text prompts through Flyelep's asynchronous video-generation API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to prepare Flyelep asynchronous video-generation API requests from text prompts and optional media references, then poll for the generated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Flyelep secretKey is required for API calls and could be exposed if stored in files, examples, or persistent configuration.

Mitigation: Collect the secretKey at runtime, pass it only in request headers, and do not save it in skill files, repositories, logs, or reusable payloads.

Risk: Uploaded media is sent to Flyelep and may be returned as a permanent public URL.

Mitigation: Upload only media the user is comfortable sharing with Flyelep and exposing through a persistent URL.

Risk: Video generation is asynchronous and can take long enough for premature timeouts or incomplete results.

Mitigation: Submit the task first, poll the result endpoint with the returned task ID, and allow an extended timeout before reporting failure.

Risk: Reference media has strict type, count, size, duration, and mode-combination limits.

Mitigation: Validate media inputs against the documented limits before upload or task submission, including the restriction against using first/last frame mode with reference media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/generate-video)
- [Flyelep video generation API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/generateVideo)
- [Flyelep task result API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown guidance with JSON request bodies, shell commands, and returned video URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Flyelep secretKey at runtime and may require polling for asynchronous task completion.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
