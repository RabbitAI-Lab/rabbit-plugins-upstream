## Description:

Creates animated vertical infographic reels from a topic, article URL, YouTube URL, or prepared script using Higgsfield for image and video generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[formula100k](https://clawhub.ai/user/formula100k)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content teams use this skill to turn educational or explanatory inputs into publish-ready 9:16 infographic reels. It helps an agent classify the concept, build a brief, generate image and video prompts, request approval before costly media generation, and deliver output paths plus caption guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creative inputs, URLs, extracted article or YouTube content, and prompts may be processed by external tools.

Mitigation: Avoid private URLs, confidential business ideas, tokens in query strings, and sensitive personal data before using the skill.

Risk: Image and video generation can incur external tool costs.

Mitigation: Review the cost prompt and require approval before media generation, especially before the video step.

Risk: Educational or health-oriented reels can become misleading if claims are not verified.

Mitigation: Use the configured research or web extraction tools for verifiable claims and review the generated copy before publishing.

Risk: Generated files are written under entregables/infografias/<slug> and may be shared through the agent workflow.

Mitigation: Inspect the output directory and generated media before distributing the PNG, MP4, captions, or prompts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/formula100k/skills/infografia-reel-formula100k)
- [Animation Presets](references/animation-presets.md)
- [Los 7 Arquetipos Visuales](references/arquetipos.md)
- [Brandkit](references/brandkit.md)
- [Clasificador de Arquetipo](references/clasificador.md)
- [Input Pipeline](references/input-pipeline.md)
- [Prompt Builder](references/prompt-builder.md)
- [Word Substitution](references/word-substitution.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance, files]

**Output Format:** [Markdown guidance with YAML brief content, prompt text, and generated PNG/MP4 file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected files are saved under entregables/infografias/<slug>; the normal deliverables include a base image, animated reel, brief, prompts, caption, hashtags, and CTA.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
