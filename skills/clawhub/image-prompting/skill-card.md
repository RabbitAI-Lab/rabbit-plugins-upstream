## Description: <br>
Use when crafting still-image prompts for any generative model - composition, identity sheets, edits, try-on, and photoreal personas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to craft text-to-image, image-editing, virtual try-on, upscaling, character sheet, and photoreal persona prompts for still-image generation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Copied install or API examples may run package installation commands or send prompts, images, or generated media references to Pruna or related services. <br>
Mitigation: Review npx and API commands before execution, confirm the intended service interaction, and use only an API key the user has authorized for that workflow. <br>
Risk: Image editing, try-on, and persona workflows can involve user-provided likenesses, garments, or media references. <br>
Mitigation: Avoid sensitive or unauthorized media, confirm consent and rights for source images, and review generated outputs before downstream use. <br>


## Reference(s): <br>
- [Prompt golden rules](references/prompt-golden-rules.md) <br>
- [Character turnaround sheet](references/character-turnaround-sheet.md) <br>
- [p-image-edit prompting](references/p-image-edit-prompting.md) <br>
- [p-image-try-on prompting](references/p-image-try-on-prompting.md) <br>
- [p-image-upscale guidance](references/p-image-upscale-guidance.md) <br>
- [p-image quality checklist](references/p-image-quality-checklist.md) <br>
- [p-image-edit quality checklist](references/p-image-edit-quality-checklist.md) <br>
- [p-image-try-on quality checklist](references/p-image-try-on-quality-checklist.md) <br>
- [p-image-upscale quality checklist](references/p-image-upscale-quality-checklist.md) <br>
- [Dynamic persona and scenario showcase](references/realistic-persona-showcase.md) <br>
- [Dynamic persona example prompts](references/realistic-persona-example-prompt.md) <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/image-prompting) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with prompt templates, checklists, and inline shell or API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include review steps for generated images, prompt parameters to keep outside prompt text, and API examples that require a user-provided Pruna API key.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
