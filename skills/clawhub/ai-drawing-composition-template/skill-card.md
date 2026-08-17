## Description:

Build high-consistency AI character prompts across five model syntax families using a weight and ratio precision-control workbench with character anchors, composition references, reference-image guidance, negative-word banks, and P0/P1/P2 validation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nohn3043-arch](https://clawhub.ai/user/nohn3043-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and production teams use this skill to generate and refine consistent character image prompts across natural-language, conversational, Midjourney/Niji, Stable Diffusion, and domestic API model families. It helps plan anchors, composition, reference-image strategy, negative prompts, and validation for one-off illustrations, storyboards, character cards, and series work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using private or sensitive reference images with third-party image models may expose those images under the model provider's terms.

Mitigation: Review the target model provider's privacy and retention terms before uploading reference images, and avoid private or sensitive images unless approved for that service.

Risk: Model-specific prompt syntax and reference-image support vary, so a prompt assembled for one model family may perform poorly or mislead users when reused elsewhere.

Mitigation: Select the target model first, follow the matching syntax and reference-image method, and run the included P0/P1/P2 validation checklist before scaling production runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nohn3043-arch/skills/ai-drawing-composition-template)
- [Project homepage](https://github.com/nohn3043-arch/ai-draw-cue-word-project)
- [Reference-first workflow](references/ReferenceFirstWorkflow.md)
- [Production pipeline](references/ProductionPipeline.md)
- [Natural language prompt template](references/NaturalLanguagePromptTemplate.csv)
- [Reference image capability matrix](references/ReferenceImageCapabilityMatrix.csv)
- [Validation checklist](references/Checklist.csv)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown prose and model-specific prompt templates with reference-table guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces image-prompt guidance and validation checklists; does not include executable code.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; artifact frontmatter lists 2.5.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
