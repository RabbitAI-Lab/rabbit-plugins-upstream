## Description:

Use when writing any generative prompt — ritual seed, explicit structure, scenario axes, and quality gates before paid API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this agent skill to make image, video, audio, and other generative prompts more varied, explicit, and reviewable before paid generation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Implicit identity, voice, or demographic defaults may not match user intent.

Mitigation: Ask the user to make people, voice, and representation preferences explicit before generation.

Risk: Skipping review gates can spend paid generation steps on weak or unwanted outputs.

Mitigation: Use clarification intake, quality checklists, and approval gates before paid image, video, or audio calls.

## Reference(s):

- [Generation diversity](references/generation-diversity.md)
- [Still-image prompt flow](references/still-image-prompt-flow.md)
- [Generation quality checklist hub](references/generation-quality-checklists.md)
- [Workflow feedback gates](references/workflow-feedback-gates.md)
- [Clarification intake](references/clarification-intake.md)
- [String Seed of Thought](https://pub.sakana.ai/ssot/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt text, checklists, install commands, and phase-gate instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include ritual seeds, scenario axes, prompt drafts, QA pass/fail notes, and approval gates.]

## Skill Version(s):

1.0.10 (source: artifact frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
