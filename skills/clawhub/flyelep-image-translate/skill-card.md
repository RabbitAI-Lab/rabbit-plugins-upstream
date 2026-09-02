## Description:

Recognizes and translates text in images through the Flyelep AI Tool API and returns URLs for the translated images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to translate visible text in posters, product images, and other image assets into a supported target language. It is intended for workflows where the user can provide a public image URL or allow local images to be uploaded before translation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image uploads can create permanent public URLs for source images.

Mitigation: Warn users before uploading local files and proceed only with images they are comfortable making externally reachable.

Risk: Images sent for translation are processed by a third-party service.

Mitigation: Avoid confidential, personal, regulated, or unreleased business images unless the provider's retention and deletion controls are acceptable.

Risk: The skill requires a Flyelep API key at runtime.

Mitigation: Request the key only when needed and do not store it in skill files, repositories, or persistent configuration.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/flyelepai/skills/flyelep-image-translate)
- [Flyelep API Key Dashboard](https://www.flyelep.cn/controlboard)
- [Flyelep Image Translation API](https://www.flyelep.cn/prod-api/poster-design/api/v1/poster/aiTool/translate)
- [Flyelep File Upload API](https://www.flyelep.cn/prod-api/poster-design/api/v1/file/upload)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request bodies and curl commands; runtime output is translated image URL text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return one or more translated image URLs as a comma-separated list in the same order as the input images.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
