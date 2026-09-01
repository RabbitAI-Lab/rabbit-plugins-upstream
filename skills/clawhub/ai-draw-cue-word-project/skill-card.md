## Description:

Build high-consistency AI character prompts across five model syntax families and multi-format outputs using a weight and ratio precision-control workbench.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate, refine, and validate character image prompts for consistent illustrations, storyboards, comic panels, videos, and 3D-oriented outputs across different image-generation model families.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reusable image-generation templates include an underage example character and could be adapted toward inappropriate sexualized minor imagery.

Mitigation: Use only for clearly age-appropriate, non-sexual character generation; revise examples to adult characters or add explicit minor-safety constraints before broad use.

Risk: Prompt templates may be reused across external image models with different safety filters and reference-image behavior.

Mitigation: Review generated prompts against the target model's content policy and avoid using consistency guidance to bypass safety controls.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/nohn3043-arch/skills/ai-drawing-composition-template)
- [Project Homepage](https://github.com/nohn3043-arch/ai-draw-cue-word-project)
- [CharacterAnchors.csv](references/CharacterAnchors.csv)
- [CompositionAndShots.csv](references/CompositionAndShots.csv)
- [NaturalLanguagePromptTemplate.csv](references/NaturalLanguagePromptTemplate.csv)
- [ReferenceImageCapabilityMatrix.csv](references/ReferenceImageCapabilityMatrix.csv)
- [ReferenceFirstWorkflow.md](references/ReferenceFirstWorkflow.md)
- [ProductionPipeline.md](references/ProductionPipeline.md)
- [Checklist.csv](references/Checklist.csv)
- [PanelLayoutRules.csv](references/PanelLayoutRules.csv)
- [SpeechBubblePositioning.csv](references/SpeechBubblePositioning.csv)
- [StoryboardSkeletonTemplate.csv](references/StoryboardSkeletonTemplate.csv)
- [TemporalConsistencyChecklist.csv](references/TemporalConsistencyChecklist.csv)
- [VideoGenerationPromptTemplate.csv](references/VideoGenerationPromptTemplate.csv)
- [ThreeDGenerationMatrix.csv](references/ThreeDGenerationMatrix.csv)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with prompt text, model-specific syntax, validation checklists, and configuration parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include image, storyboard, comic panel, video, and 3D prompt variants depending on the user's target model and workflow.]

## Skill Version(s):

2.8.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
