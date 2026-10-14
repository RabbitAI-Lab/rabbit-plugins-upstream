## Description:

Turns articles, documents, URLs, or topics into structured infographic prompts and, when image generation is available, finished infographic images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and other users turn source material into visual summaries using selectable layouts and styles. The skill can provide a reusable prompt and, with an image-generation API key, a finished infographic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated prompts may send sensitive source material to OpenRouter.

Mitigation: Review and remove confidential information before generating an image with your API key.

Risk: Generated image text or figures may differ from the source.

Mitigation: Check the final infographic against the source before sharing it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/j3ffyang/skills/custom-infographic)
- [Upstream project cited in skill metadata](https://github.com/JimLiu/baoyu-skills#baoyu-infographic)

## Skill Output:

**Output Type(s):** [Markdown, Image]

**Output Format:** [Markdown analysis, structured content, and image prompt; PNG infographic when generation succeeds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The image requires an OpenRouter API key and an image-capable model; Markdown preparation files remain available without image generation.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
