## Description:

Generates image-prompt guidance for low-budget Chinese 3D animation artwork, including rough early-2000s CGI styling, negative prompts, and style validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to transform creative image ideas into prompts that mimic low-budget Chinese 3D animation from the early 2000s. It is intended for style-directed image generation workflows that need prompt, negative prompt, and style-score guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests near adjacent styles, such as polished low-poly art, retro CGI, Pixar-style 3D, anime, or photorealistic rendering, may need precise routing to avoid unwanted activation.

Mitigation: Review trigger wording and keep the supplied positive, negative, and orthogonal evaluation cases in the release test set.

Risk: The skill's final prompt output is designed around English image-generation prompts, which may not match users who need non-English or bilingual output.

Mitigation: Ask explicitly for non-English or bilingual final prompts when that output format is required.

Risk: The skill intentionally degrades visual polish and steers outputs toward rough, awkward, low-budget aesthetics.

Mitigation: Use it only for requests where that aesthetic is desired, and route polished, cinematic, photorealistic, anime, or premium CG requests to another skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qomob/skills/low-budget-3d)
- [Publisher profile](https://clawhub.ai/user/qomob)
- [Server-resolved source repository](https://github.com/qomob/low-budget-3d)
- [Style Constitution](references/style-constitution.md)
- [Subject Rebuilder](references/subject-rebuilder.md)
- [Character Director](references/character-director.md)
- [World Builder](references/world-builder.md)
- [Production and Render](references/production-and-render.md)
- [Prompt Compiler](references/prompt-compiler.md)
- [Style Validator](references/style-validator.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown-style response with an English image prompt, a negative prompt, generation YAML, and style-score YAML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill strongly steers eligible image-prompt requests toward rough low-budget Chinese 3D animation aesthetics.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
