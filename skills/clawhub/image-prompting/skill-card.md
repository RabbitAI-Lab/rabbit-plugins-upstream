## Description:

Use when crafting still-image prompts for any generative model - composition, identity sheets, edits, try-on, and photoreal personas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent builders use this skill to draft and check still-image prompts for photo generation, character identity sheets, image edits, virtual try-on, upscaling, and persona plates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install commands and API examples can execute third-party tooling or send prompts, images, scripts, and metadata to Pruna or Replicate.

Mitigation: Review commands before running them, pin trusted package versions where appropriate, and upload only content and likenesses the user is authorized to use.

Risk: Generated image prompts and quality checks can still produce misleading, low-quality, or rights-sensitive image outputs.

Mitigation: Visually review generated outputs against the included quality checklists before reuse, publication, or downstream model calls.

## Reference(s):

- [Image prompt golden rules](references/prompt-golden-rules.md)
- [Character turnaround sheet](references/character-turnaround-sheet.md)
- [p-image-edit prompting](references/p-image-edit-prompting.md)
- [p-image-try-on prompting](references/p-image-try-on-prompting.md)
- [p-image-upscale guidance](references/p-image-upscale-guidance.md)
- [p-image quality checklist](references/p-image-quality-checklist.md)
- [p-image-edit quality checklist](references/p-image-edit-quality-checklist.md)
- [p-image-try-on quality checklist](references/p-image-try-on-quality-checklist.md)
- [p-image-upscale quality checklist](references/p-image-upscale-quality-checklist.md)
- [Dynamic persona and scenario showcase](references/realistic-persona-showcase.md)
- [Dynamic persona example prompts](references/realistic-persona-example-prompt.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance with prompt text, checklists, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompt drafts, visual quality checks, model-selection guidance, and API example commands.]

## Skill Version(s):

1.0.11 (source: server evidence and skill frontmatter metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
