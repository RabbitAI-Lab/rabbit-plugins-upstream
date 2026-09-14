## Description:

Use when crafting still-image prompts for any generative model, including composition, identity sheets, edits, try-on, and photoreal personas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to draft and review still-image prompts for photo generation, image edits, character continuity sheets, virtual try-on, upscaling, and photoreal persona plates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Install examples use unpinned npx commands.

Mitigation: Review the skill before installation and prefer pinned, reviewed versions of npx skills add commands.

Risk: Example API calls may send prompts, media references, scripts, or API keys to external Pruna or Replicate services.

Mitigation: Do not send confidential prompts, private image URLs, real-person likenesses, voice scripts, or production API keys unless that external processing is intended.

## Reference(s):

- [Prompt Golden Rules](references/prompt-golden-rules.md)
- [Character Turnaround Sheet](references/character-turnaround-sheet.md)
- [p-image-edit Prompting](references/p-image-edit-prompting.md)
- [p-image-try-on Prompting](references/p-image-try-on-prompting.md)
- [p-image-upscale Guidance](references/p-image-upscale-guidance.md)
- [p-image Quality Checklist](references/p-image-quality-checklist.md)
- [p-image-edit Quality Checklist](references/p-image-edit-quality-checklist.md)
- [p-image-try-on Quality Checklist](references/p-image-try-on-quality-checklist.md)
- [p-image-upscale Quality Checklist](references/p-image-upscale-quality-checklist.md)
- [Dynamic Persona and Scenario Showcase](references/realistic-persona-showcase.md)
- [Dynamic Persona Example Prompts](references/realistic-persona-example-prompt.md)
- [Pruna Predictions API Endpoint](https://api.pruna.ai/v1/predictions)
- [Replicate p-image Model Page](https://replicate.com/prunaai/p-image)
- [Replicate p-image-try-on Model Page](https://replicate.com/prunaai/p-image-try-on)
- [Replicate p-video-avatar Model Page](https://replicate.com/prunaai/p-video-avatar)
- [Square-Zero-Labs video-prompting-skill Source Pattern](https://github.com/Square-Zero-Labs/video-prompting-skill)
- [smixs visual-skills Source Pattern](https://github.com/smixs/visual-skills)
- [higgsfield-ai skills Source Pattern](https://github.com/higgsfield-ai/skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with prompt templates, checklists, and inline bash/JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API request examples that require a PRUNA_API_KEY and externally hosted media URLs.]

## Skill Version(s):

1.0.12 (source: server release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
