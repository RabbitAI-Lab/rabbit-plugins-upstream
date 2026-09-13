## Description:

Use when writing any generative prompt: ritual seed, explicit structure, scenario axes, and quality gates before paid API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and external agents use this skill to draft varied image, video, and audio generation prompts, decide when to ask clarifying questions, and apply quality and approval gates before paid generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Related-skill installation commands are unpinned and auto-confirmed.

Mitigation: Review each install command before execution and prefer pinned versions or a controlled installer.

Risk: Downstream workflows may involve paid API calls, uploads, or changes to the installed skill suite.

Mitigation: Require explicit user approval before paid API calls, uploads, or skill-suite changes.

Risk: Gender and identity defaults can affect face, voice, or avatar outputs.

Mitigation: Review identity-related defaults and keep user-specified identity, voice, and continuity constraints locked.

## Reference(s):

- [Generation Diversity](artifact/references/generation-diversity.md)
- [Still-image Prompt Flow](artifact/references/still-image-prompt-flow.md)
- [Generation Quality Checklist Hub](artifact/references/generation-quality-checklists.md)
- [Workflow Feedback Gates](artifact/references/workflow-feedback-gates.md)
- [Clarification Intake](artifact/references/clarification-intake.md)
- [String Seed of Thought](https://pub.sakana.ai/ssot/)
- [ClawHub Skill Page](https://clawhub.ai/pruna-ai/skills/generation-diversity)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, checklists, command snippets, and JSON manifest examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes human approval gates before paid generation and logs ritual_seed, axes, and prediction identifiers for traceability.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
