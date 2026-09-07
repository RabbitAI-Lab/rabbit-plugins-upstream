## Description:

Builds high-consistency AI character prompts across natural-language, conversational, MJ/Niji, Stable Diffusion, and domestic API syntax families for image, storyboard, comic panel, video, and 3D workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and production teams use this skill to assemble and validate model-specific character prompts while preserving identity, composition, reference-image strategy, and cross-scene consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images may include material the user is not allowed to upload or reuse.

Mitigation: Use only reference images the user has rights to use, as directed by the server security guidance.

Risk: Prompt outputs could be misused for sexualized, minor-like, or otherwise policy-violating character content.

Mitigation: Follow the skill's adult-only, non-sexual character-design rules and reject prompts that reintroduce minors, minor-coded traits, or sexualized content.

Risk: External image, video, or 3D generation tools may apply reference images and negative prompts inconsistently across model families.

Mitigation: Use the reference-image capability matrix, P0/P1/P2 checklist, and production pre-flight checks before scaling a prompt series.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/ai-draw-cue-word-project)
- [Project homepage](https://github.com/nohn3043-arch/ai-draw-cue-word-project)
- [SKILL.md](SKILL.md)
- [ReferenceFirstWorkflow.md](references/ReferenceFirstWorkflow.md)
- [ProductionPipeline.md](references/ProductionPipeline.md)
- [NOTES.md](references/NOTES.md)
- [CharacterAnchors.csv](references/CharacterAnchors.csv)
- [CompositionAndShots.csv](references/CompositionAndShots.csv)
- [ReferenceImageCapabilityMatrix.csv](references/ReferenceImageCapabilityMatrix.csv)
- [NaturalLanguagePromptTemplate.csv](references/NaturalLanguagePromptTemplate.csv)
- [Checklist.csv](references/Checklist.csv)
- [VideoGenerationPromptTemplate.csv](references/VideoGenerationPromptTemplate.csv)
- [ThreeDGenerationMatrix.csv](references/ThreeDGenerationMatrix.csv)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown prompt guidance, model-specific prompt text, and CSV-backed configuration choices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; outputs guide external image, video, and 3D generation tools.]

## Skill Version(s):

2.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
