## Description:

Uses Flyelep's asynchronous free-creation API to generate product or creative images with the Image-2 model from a prompt and optional reference image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect image-generation parameters, call Flyelep's async Image-2 creation API, poll for task results, and return generated image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference image URLs are sent to Flyelep's external image-generation API.

Mitigation: Use prompts and public image URLs that are appropriate to share with Flyelep; avoid sensitive, private, or internal-only content.

Risk: The skill requires a Flyelep secretKey for API authentication.

Mitigation: Provide the secretKey only at runtime and do not store it in skill files, examples, repositories, or persistent configuration.

Risk: Temporary payload files can contain prompts, reference image URLs, or task identifiers when the Windows/PowerShell flow is used.

Mitigation: Create temporary payload files only when needed, write them with UTF-8 encoding, and remove them after the API call completes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/async-free-creation)
- [Flyelep open platform](https://www.flyelep.cn/controlboard)
- [Flyelep async creation API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/allAroundCreationAsync)
- [Flyelep task result API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/queryTaskResult)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON and shell command examples plus generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a runtime secretKey, prompt text, image count, aspect ratio, and optional public reference image URLs.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
