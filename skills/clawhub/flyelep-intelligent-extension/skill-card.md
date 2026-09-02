## Description:

This skill helps agents use the Flyelep AI Tool API to intelligently extend one or more images to a requested aspect ratio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send image URLs, or uploaded local images, to Flyelep for outpainting and aspect-ratio adaptation such as 16:9, 1:1, or 9:16.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a Flyelep API key at runtime.

Mitigation: Provide the key only at runtime, avoid storing it in skill files or persistent configuration, and rotate it if exposure is suspected.

Risk: Selected local images may be uploaded to Flyelep and converted into permanent public URLs.

Mitigation: Avoid uploading private, regulated, or sensitive images unless the user has approved that external processing and public URL exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/flyelep-intelligent-extension)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)
- [Flyelep intelligent extension API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/intelligentExtension)
- [Flyelep file upload API endpoint](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns generated image URLs in the same order as the input image URL list.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
