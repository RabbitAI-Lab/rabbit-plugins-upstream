## Description:

Generates professional infographics from articles, documents, URLs, or topics using the baoyu 21-layout by 21-style system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn source content into high-density infographic assets by analyzing content, structuring it into Markdown, assembling image prompts, and generating an image when an OpenRouter key and image-capable model are available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill writes source-derived files and generated outputs into the workspace.

Mitigation: Review the target output folder before running, and avoid using confidential or proprietary content unless local file creation is acceptable.

Risk: When image generation is used, prompt content can be sent to OpenRouter or another image service.

Mitigation: Redact confidential, personal, credential, and proprietary content before generating prompts or images.

Risk: Image generation depends on model availability and supported aspect ratios.

Mitigation: Use the prompt-only workflow when image generation fails and map unsupported aspect ratios to supported presets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/baoyu-infographic)
- [Upstream metadata link](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Infographic Content Analysis Framework](references/analysis-framework.md)
- [Structured Content Template](references/structured-content-template.md)
- [Base Prompt Template](references/base-prompt.md)
- [Workflow Example](references/workflow-example.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files, images]

**Output Format:** [Markdown files and an optional PNG image; responses include concise guidance and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates an infographic/{topic-slug}/ workspace folder; image generation requires OPENROUTER_API_KEY and may send prompt content to OpenRouter.]

## Skill Version(s):

1.0.0 (source: server release metadata; upstream artifact metadata version 1.56.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
