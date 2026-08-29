## Description:

Image Enlarge uses the Flyelep AI Tool API to upscale one or more images and return enlarged image URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enlarge product or other images by 2x, 4x, or 8x through Flyelep's HTTP API. The workflow accepts public image URLs and can upload local image files before processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and the user's Flyelep API key are sent to Flyelep; local images may be uploaded to public permanent URLs.

Mitigation: Use runtime-provided API keys only, avoid storing credentials, and process private, regulated, or sensitive images only when public URL exposure is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-image-enlarge)
- [Flyelep control board](https://www.flyelep.cn/controlboard)
- [Flyelep image enlarge API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/enlarge)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with JSON payload examples, shell commands, and returned image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns enlarged image URLs and may first upload local files to public permanent URLs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
