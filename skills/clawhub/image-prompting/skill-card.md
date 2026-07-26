## Description: <br>
Use when crafting still-image prompts for any generative model — composition, identity sheets, edits, try-on, and photoreal personas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to craft and validate prompts for still-image generation, edits, character identity sheets, virtual try-on, upscaling, and photoreal or stylized persona plates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompt examples and related Pruna or Replicate workflows may send prompts, image URLs, uploaded media, or scripts to third-party services. <br>
Mitigation: Review the provider's media and script handling before use, and avoid sending confidential assets, internal URLs, or unapproved real-person images. <br>
Risk: Example API calls use credential-bearing workflows. <br>
Mitigation: Keep API keys in environment variables or a secrets manager, and do not paste secrets into prompts, shared logs, or generated artifacts. <br>
Risk: Persona, avatar, and try-on examples can involve realistic depictions of people. <br>
Mitigation: Use only images and voices with appropriate permission, and visually review generated outputs before publication or downstream reuse. <br>


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


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with prompt templates, checklists, and example shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-specific prompt structure, API input guidance, and visual quality review checklists.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence and skill frontmatter metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
