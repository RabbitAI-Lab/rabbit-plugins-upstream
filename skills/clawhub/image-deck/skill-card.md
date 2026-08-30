## Description:

image-deck helps agents create full-image slide decks, single slides, PPT-style presentations, and carousel pages with GPT Image 2, using explicit design and sample-style approvals before generating the complete deck.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tseng71](https://clawhub.ai/user/tseng71)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to guide Codex through creating presentation decks whose pages are complete generated raster images, then optionally packaging those images as PPTX or PDF.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive source documents may be transformed into prompts, research notes, logs, and image-generation requests.

Mitigation: Use this workflow only when that processing is acceptable; choose an ordinary editable PPT workflow for sensitive material that should not enter image-generation prompts.

Risk: Generated slide pages are raster images, so text, exact charts, and precise tables are not directly editable and may require regeneration if inaccurate.

Mitigation: Use an editable presentation workflow when exact text, tables, or charts are required; otherwise inspect generated slides and regenerate pages with errors.

## Reference(s):

- [Prompt Patterns](references/prompt-patterns.md)
- [ClawHub skill page](https://clawhub.ai/tseng71/skills/image-deck)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with image-generation prompts, optional shell commands, and generated slide image/PPTX/PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Codex built-in image_gen (GPT Image 2); visible slide text is generated inside raster images and is not directly editable.]

## Skill Version(s):

0.1.27 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
