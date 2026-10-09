## Description:

Guides agents to write diverse, explicit generative-media prompts and check outputs before paid API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan varied image, video, and audio prompts, clarify creative requirements, and review generated assets before continuing paid workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid media generation may incur unwanted charges or produce outputs that miss the brief.

Mitigation: Keep approval gates enabled, review prompts before API calls, and inspect outputs before advancing to paid steps.

Risk: Example gender or voice choices may override a user's explicit preferences.

Mitigation: Preserve the user's stated identity and voice requirements when selecting prompt variations.

Risk: Installing related skills introduces publisher and installer supply-chain exposure.

Mitigation: Install only when the publisher and skill installer are trusted.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/pruna-ai/skills/generation-diversity)
- [Clarification intake](references/clarification-intake.md)
- [Generation diversity guidance](references/generation-diversity.md)
- [Still-image prompt flow](references/still-image-prompt-flow.md)
- [Generation quality checklists](references/generation-quality-checklists.md)
- [Workflow feedback gates](references/workflow-feedback-gates.md)
- [String Seed of Thought](https://pub.sakana.ai/ssot/)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands]

**Output Format:** [Markdown prompts, planning notes, and review checklists; optional API command drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompts preserve user-specified constraints and include varied scenario choices and approval checkpoints.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
