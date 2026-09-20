## Description:

Use when someone wants an educational explainer with a host and characters — history or science shorts with dialogue, not voiceover-only B-roll.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, educators, and developers use this skill to plan and generate educational shorts that alternate narrator beats with on-camera expert or character dialogue. It provides phase-gated guidance for story structure, prompts, stills, TTS, video clips, and final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can call external paid media-generation services during still, audio, video, and assembly phases.

Mitigation: Follow the documented approval gates and do not start paid generation until the user has approved the relevant phase.

Risk: The workflow depends on installing and using multiple Pruna skills.

Mitigation: Review the Pruna skills being added and prefer pinned or vetted versions where available.

Risk: Generated educational media can contain inaccurate narration, misleading visuals, or inclusivity issues.

Mitigation: Review plans, stills, audio, and clips before final assembly, and revise prompts or scripts when quality or representation issues appear.

## Reference(s):

- [Educational explainer motion](references/interactive-explainer-motion.md)
- [Interactive explainer prompts](references/interactive-explainer-prompts.md)
- [Educational explainer scenes](references/interactive-explainer-scenes.md)
- [Educational explainer example prompt](example-prompt.md)
- [Explainer plan template](templates/explainer-plan.template.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON plan configuration and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Phase-gated workflow with approve plan, approve stills, and approve clips checkpoints; default plan settings are 720p, 24 fps, and 16:9.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
