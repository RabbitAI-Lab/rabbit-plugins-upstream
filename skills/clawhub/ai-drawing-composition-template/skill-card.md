## Description:

Build high-consistency AI character prompts across five model syntax families using a weight and ratio precision-control workbench with character anchors, composition references, model-specific syntax guidance, negative-word support, and validation checklists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, artists, and content teams use this skill to assemble and validate AI character image prompts for illustrations, storyboards, character cards, and multi-image series that need consistent identity, composition, and model-specific syntax.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release packages reusable minor-character image prompt templates and body/proportion guidance without clear age-safety guardrails.

Mitigation: Review or modify the skill before installing; replace the under-18 example and body/proportion anchors with adult or age-neutral templates.

Risk: Prompt templates or reference-image packs could be used to preserve or regenerate sensitive visual material.

Mitigation: Add explicit rules forbidding sexualized, suggestive, or exploitative depictions of minors, and review reference-image packs and generation logs before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/ai-drawing-composition-template)
- [Project homepage](https://github.com/nohn3043-arch/ai-draw-cue-word-project)
- [Reference-First Workflow](references/ReferenceFirstWorkflow.md)
- [Production Pipeline](references/ProductionPipeline.md)
- [Character Anchors](references/CharacterAnchors.csv)
- [Composition and Shots](references/CompositionAndShots.csv)
- [Reference Image Capability Matrix](references/ReferenceImageCapabilityMatrix.csv)
- [Natural Language Prompt Template](references/NaturalLanguagePromptTemplate.csv)
- [Negative Word Bank](references/NegativeWordBank.csv)
- [Validation Checklist](references/Checklist.csv)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown prose, prompt templates, model-specific prompt snippets, and checklist-style guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model-specific syntax for natural-language image models, conversational image models, MJ/Niji, Stable Diffusion, and domestic API families.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata; artifact frontmatter states 2.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
