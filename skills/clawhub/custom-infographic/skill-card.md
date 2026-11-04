## Description:

Helps an agent turn articles, documents, URLs, or topics into infographic content and image-generation prompts, with optional image generation through OpenRouter.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content creators use the skill to turn source material into a structured visual summary, prepare an image-generation prompt, and, when configured, generate the infographic through an image model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source material may contain confidential information or personal data that should not be shared with OpenRouter or the selected model provider.

Mitigation: Use only material authorized for sharing with both providers, and review prompts for confidential information and personal data before generation.

Risk: Image generation can incur API charges, and local working files may remain after generation.

Mitigation: Check the selected model and expected API costs before generating, and manage local working files according to project policy.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/j3ffyang/skills/custom-infographic)
- [Related baoyu-infographic project listed in skill metadata](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)
- [Workflow example](references/workflow-example.md)

## Skill Output:

**Output Type(s):** [Images, Markdown, Image-generation prompts]

**Output Format:** [PNG infographic image plus Markdown source, analysis, structured content, and prompt files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Image generation requires an OpenRouter API key and an image-capable model; without them, the Markdown planning and prompt files can still be produced.]

## Skill Version(s):

1.56.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
