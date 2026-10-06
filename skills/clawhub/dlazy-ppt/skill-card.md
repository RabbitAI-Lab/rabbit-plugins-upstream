## Description:

Generate visually unified image-based PPT/PPTX decks from articles, reports, papers, notes, or outlines, using dLazy for every slide image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating presentations from articles, reports, research papers, notes, or outlines use this skill to plan and produce visually consistent image-based PowerPoint decks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared local runtime stores a dLazy API key.

Mitigation: Install only if local key storage is acceptable; protect the key and rotate or revoke it when needed.

Risk: Slide prompts and required source images are sent to dLazy for image generation.

Mitigation: Use only material permitted to leave your machine; avoid highly sensitive source content.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-ppt)
- [Project homepage listed in skill metadata](https://github.com/dlazy-ai/ai-ppt-slides)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)
- [Image model configuration](docs/image-model-configuration.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Files]

**Output Format:** [Markdown guidance and image-based PPTX with slide images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Slides are full-page images, not separately editable text or shapes.]

## Skill Version(s):

1.0.16 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
