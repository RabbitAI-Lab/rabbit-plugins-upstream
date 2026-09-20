## Description:

Use when crafting still-image prompts for any generative model - composition, identity sheets, edits, try-on, and photoreal personas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent operators use this skill to draft and review still-image generation prompts, image edit prompts, character sheets, virtual try-on prompts, upscale parameters, and visual quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional install commands fetch remote skill packages that are not pinned in the examples.

Mitigation: Install only from trusted PrunaAI sources, and pin or review remote npx skill targets before running them in stricter environments.

Risk: API examples can send prompts, referenced media URLs, voice text, and API keys to Pruna services.

Mitigation: Use approved accounts and data, avoid sensitive inputs unless permitted, and keep API keys in environment variables or approved secret storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/image-prompting)
- [Prompt golden rules](references/prompt-golden-rules.md)
- [Character turnaround sheet](references/character-turnaround-sheet.md)
- [p-image-edit prompting](references/p-image-edit-prompting.md)
- [p-image-try-on prompting](references/p-image-try-on-prompting.md)
- [p-image-upscale guidance](references/p-image-upscale-guidance.md)
- [p-image quality checklist](references/p-image-quality-checklist.md)
- [p-image-edit quality checklist](references/p-image-edit-quality-checklist.md)
- [p-image-try-on quality checklist](references/p-image-try-on-quality-checklist.md)
- [p-image-upscale quality checklist](references/p-image-upscale-quality-checklist.md)
- [Dynamic persona showcase](references/realistic-persona-showcase.md)
- [Dynamic persona example prompts](references/realistic-persona-example-prompt.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt templates, checklists, and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model parameter guidance, API request examples, and visual review criteria for generated or edited images.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
