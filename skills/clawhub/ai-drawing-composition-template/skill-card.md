## Description:

Helps agents build consistent AI character prompts across image, storyboard, comic, video, and 3D workflows using structured anchors, composition rules, model-specific syntax, and validation checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

External users, artists, and prompt engineers use this skill to generate or refine character prompts when visual consistency across models, image series, storyboards, comic panels, video, or 3D outputs matters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes reusable under-18 character and body prompt templates without clear safety guardrails.

Mitigation: Review before installation, remove or rewrite under-18 character templates and loli or teen body baselines, and add explicit image-generation safety safeguards before use.

Risk: Prompt workbooks can preserve unsafe or unsuitable character anchors across repeated outputs.

Mitigation: Require human review of character anchors, negative prompts, and validation checklists before using generated prompts in production image workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/ai-drawing-composition-template)
- [Project homepage from clawdis metadata](https://github.com/nohn3043-arch/ai-draw-cue-word-project)
- [CharacterAnchors.csv](references/CharacterAnchors.csv)
- [CompositionAndShots.csv](references/CompositionAndShots.csv)
- [NaturalLanguagePromptTemplate.csv](references/NaturalLanguagePromptTemplate.csv)
- [ReferenceImageCapabilityMatrix.csv](references/ReferenceImageCapabilityMatrix.csv)
- [Reference-First Workflow](references/ReferenceFirstWorkflow.md)
- [Production Pipeline](references/ProductionPipeline.md)
- [Checklist.csv](references/Checklist.csv)
- [StoryboardSkeletonTemplate.csv](references/StoryboardSkeletonTemplate.csv)
- [PanelLayoutRules.csv](references/PanelLayoutRules.csv)
- [VideoGenerationPromptTemplate.csv](references/VideoGenerationPromptTemplate.csv)
- [ThreeDGenerationMatrix.csv](references/ThreeDGenerationMatrix.csv)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text prompt guidance with model-specific prompt blocks and checklist results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include image prompt text, negative prompt guidance, storyboard or panel planning text, reference-pack recommendations, and validation notes.]

## Skill Version(s):

2.6.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
