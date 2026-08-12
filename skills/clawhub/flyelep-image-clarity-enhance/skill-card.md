## Description:

Enhances one or more image URLs through the Flyelep AI Tool API and returns new URLs for clearer images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit public image URLs to Flyelep for light, standard, or strong clarity enhancement, including batch processing. The agent gathers the required image URL and enhancement-strength inputs, calls the HTTP API, and presents the returned enhanced image URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image URLs and the Flyelep secretKey are sent to Flyelep's API during use.

Mitigation: Use only image links appropriate for third-party processing, provide the API key at runtime, and avoid storing real keys in shared prompts, files, repositories, or persistent configuration.

Risk: Unsupported image formats, inaccessible URLs, oversized files, or invalid enhancement-strength values can cause API failures.

Mitigation: Confirm that source images are public direct links in JPG, PNG, or BMP format, meet the documented size and dimension limits, and use one of light, standard, or strong for enhancement strength.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-image-clarity-enhance)
- [Flyelep image clarity API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/imageClarityEnhance)
- [Flyelep Open Platform control board](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP request examples and returned image URL text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned image URLs may be comma-separated for batch requests; the skill instructs the agent to split and present them individually.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
