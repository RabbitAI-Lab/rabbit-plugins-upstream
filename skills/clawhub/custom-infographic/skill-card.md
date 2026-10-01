## Description:

Turns articles, documents, URLs, or topics into structured infographic content, visual prompts, and an optional generated image using selectable layouts and styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and teams use this skill to turn source material into an infographic with a chosen layout, visual style, aspect ratio, and language. It produces planning files and a generation prompt even when image generation is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source text and generated prompts are sent to OpenRouter during image generation.

Mitigation: Review and redact confidential material and secrets before generating images.

Risk: Image generation uses the OPENROUTER_API_KEY credential.

Mitigation: Use a key limited to the intended image-generation account.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/custom-infographic)
- [Upstream project listed in skill metadata (not verified import provenance)](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Analysis framework](references/analysis-framework.md)
- [Structured content template](references/structured-content-template.md)
- [Base infographic prompt](references/base-prompt.md)

## Skill Output:

**Output Type(s):** [Markdown, Image files]

**Output Format:** [Markdown planning files and prompt; PNG image when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [An API key and an image-capable model are needed for image generation; otherwise, the planning files and prompt remain usable.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
