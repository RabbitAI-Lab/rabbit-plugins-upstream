## Description:

Generates realistic lifestyle photos of people holding a user's product by analyzing product and inspiration images, creating structured photo prompts, and producing image outputs with role consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce sellers, and marketing teams use this skill to turn product photos and optional style references into realistic product lifestyle images for listings, ads, or campaign assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload local product or reference images and make them publicly accessible through OSS URLs.

Mitigation: Use only files that are approved for public access, avoid private local files, and confirm user intent before upload.

Risk: The skill uses credentialed external network calls through LinkFox gateway and API-key environment variables.

Mitigation: Install only in environments where LINKFOX_TOOL_GATEWAY and API-key variables are controlled by trusted administrators.

Risk: The artifact includes external onboarding installation guidance and self-extension behavior for creating or modifying skills.

Mitigation: Disable this behavior or require explicit administrator approval before installing external onboarding packages or changing skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-realistic-photo-generation)
- [AI image generation API reference](artifact/skills/linkfox-aigc-imagegen/references/api.md)
- [AI text generation API reference](artifact/skills/linkfox-aigc-textgen/references/api.md)
- [File upload API reference](artifact/skills/linkfox-file-upload/references/api.md)
- [Web search API reference](artifact/skills/linkfox-tsearch-search/references/api.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown responses with generated image links, structured JSON prompt excerpts, and local file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external LinkFox services, upload local images to public URLs, and create local media and data files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
