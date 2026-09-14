## Description:

Use when someone wants an educational explainer with a host and characters, such as history or science shorts with dialogue rather than voiceover-only B-roll.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and agent operators use this skill to plan and generate educational short videos that combine host narration, character dialogue, still generation, TTS, video generation, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags unpinned remote skill installation during setup.

Mitigation: Install reviewed or pinned versions, inspect added skills before loading them, and remove automatic confirmation from install commands when reviewing interactively.

Risk: The security summary flags an overbroad instruction that affects every reply.

Mitigation: Activate the workflow only for relevant explainer-generation tasks and review generated plans before proceeding to media generation.

Risk: The security guidance notes that reference media may be uploaded and media outputs may be overwritten.

Mitigation: Run generation in an isolated workspace and use only reference media that is acceptable to upload for the selected service.

## Reference(s):

- [Interactive explainer scenes](artifact/references/interactive-explainer-scenes.md)
- [Interactive explainer motion](artifact/references/interactive-explainer-motion.md)
- [Interactive explainer prompts](artifact/references/interactive-explainer-prompts.md)
- [Explainer plan template](artifact/templates/explainer-plan.template.json)
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/interactive-explainer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON plans, shell commands, and media-generation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides phase-gated production of stills, narration audio, video clips, optional background music, and assembled explainer videos.]

## Skill Version(s):

1.0.12 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
