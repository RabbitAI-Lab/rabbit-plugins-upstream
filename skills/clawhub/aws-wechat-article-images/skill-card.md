## Description:

Generates WeChat public account cover images and in-article illustrations from article titles and content, using reusable style presets and a user-configured image-generation endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aiworkskills](https://clawhub.ai/user/aiworkskills)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and brand teams use this skill to plan and generate WeChat article cover images and supporting illustrations that match an article's topic, structure, and visual style. Developers or agent operators can also use it as the image-generation step inside the broader aws-wechat-article workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send API keys and article-derived prompts to a user-configured image endpoint, and the security evidence notes that HTTPS is not enforced.

Mitigation: Use only a trusted HTTPS image_model.base_url, use a dedicated low-privilege API key with billing limits, and rotate any key that may have been used with an HTTP endpoint.

Risk: Prompts may include unpublished article titles, summaries, or section content that an external image provider or relay can receive.

Mitigation: Avoid sending confidential or unpublished article content unless the provider is trusted, and review prompts before generation for sensitive details.

Risk: Generated covers and illustrations can contain incorrect text, irrelevant imagery, or low-quality rendering.

Mitigation: Review generated images before publication, checking title text, layout, relevance, dimensions, and whether image references still point to existing files after regeneration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/aiworkskills/skills/aws-wechat-article-images)
- [Publisher profile](https://clawhub.ai/user/aiworkskills)
- [Declared homepage](https://aiworkskills.cn)
- [Cover method](references/cover-method.md)
- [Article image method](references/image-method.md)
- [Image specifications](references/specs.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, image files]

**Output Format:** [Markdown guidance, prompt files, shell commands, and generated JPG/PNG/WebP image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and IMAGE_MODEL_API_KEY when using the configured external image-generation endpoint.]

## Skill Version(s):

1.0.24 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
