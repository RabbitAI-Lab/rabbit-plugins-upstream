## Description:

Generate a professional infographic from an article, document, URL, or topic, using the baoyu layout x style system with 21 layouts and 21 styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content creators, and developers use this skill to turn articles, documents, URLs, or topics into infographic planning files, prompts, and optionally a generated image. It supports layout and style selection for visual summaries, information graphics, and high-density information posters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts may contain source-derived text that is sent to OpenRouter or another image provider selected by the user.

Mitigation: Review and redact confidential or sensitive content before image generation, or use the prompt-only outputs when provider transmission is not acceptable.

Risk: Image generation depends on a configured API key and a provider model that can produce images.

Mitigation: Set OPENROUTER_API_KEY before generation and keep the generated Markdown analysis, structured content, and prompt files as fallback outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/baoyu-infographic)
- [Upstream baoyu-infographic metadata link](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Structured content template](references/structured-content-template.md)
- [Base prompt template](references/base-prompt.md)
- [Workflow example](references/workflow-example.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown planning files, image-generation prompt text, shell command guidance, and optional PNG image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires an OpenRouter API key and an image-capable model; when unavailable, the skill still produces analysis, structured content, and prompt files.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
