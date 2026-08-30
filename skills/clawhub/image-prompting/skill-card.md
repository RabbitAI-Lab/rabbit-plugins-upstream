## Description:

Use when crafting still-image prompts for any generative model: composition, identity sheets, edits, try-on, and photoreal personas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pruna-ai](https://clawhub.ai/user/pruna-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agent operators use this skill to plan high-quality still-image generation and editing prompts, including identity continuity sheets, surgical edits, virtual try-on prompts, upscaling decisions, and visual quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive prompts, private images, or real-person likenesses may be processed by external generative-image services when users follow API examples.

Mitigation: Use only inputs you are authorized to process, obtain consent for likenesses, avoid sensitive private material, and keep API keys in environment variables or a secret manager.

Risk: Generated, edited, try-on, or upscaled images can drift identity, alter garments, introduce artifacts, or preserve unsuitable source-image flaws.

Mitigation: Apply the included prompt discipline and matching visual quality checklist before reuse, downstream video generation, ecommerce handoff, or publication.

Risk: Complex try-on prompts or multi-reference edits can miss requested items, merge details, or change protected regions such as face, hair, pose, background, or product geometry.

Mitigation: Use explicit image indexing and change/keep clauses, choose normal mode for hard preservation tasks, and visually verify outputs against the preservation checklist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/image-prompting)
- [Prompt golden rules](references/prompt-golden-rules.md)
- [Character turnaround sheet](references/character-turnaround-sheet.md)
- [p-image edit prompting](references/p-image-edit-prompting.md)
- [p-image try-on prompting](references/p-image-try-on-prompting.md)
- [p-image upscale guidance](references/p-image-upscale-guidance.md)
- [p-image quality checklist](references/p-image-quality-checklist.md)
- [p-image edit quality checklist](references/p-image-edit-quality-checklist.md)
- [p-image try-on quality checklist](references/p-image-try-on-quality-checklist.md)
- [p-image upscale quality checklist](references/p-image-upscale-quality-checklist.md)
- [Dynamic persona and scenario showcase](references/realistic-persona-showcase.md)
- [Dynamic persona example prompts](references/realistic-persona-example-prompt.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with prompt templates, checklists, JSON snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory and should be visually reviewed before downstream image, video, try-on, or production use.]

## Skill Version(s):

1.0.10 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
