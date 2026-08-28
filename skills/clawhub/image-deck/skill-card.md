## Description:

image-deck guides an agent through creating full-image slide decks with Codex built-in image_gen (GPT Image 2), including planning, prompt review, sample approval, slide generation, QA, and optional PPTX/PDF assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tseng71](https://clawhub.ai/user/tseng71)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and presentation authors use this skill to have an agent design and generate presentation or carousel pages as complete raster slide images, then package them into deliverables such as PPTX or PDF when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt drafts, visual instructions, and generated slide text may be shown in chat and saved in local working files.

Mitigation: Avoid using sensitive or confidential material unless the working environment and file retention practices are appropriate.

Risk: Generated slide text is embedded inside raster images and may be inaccurate, unreadable, or hard to edit after generation.

Mitigation: Review the prompt package and generated sample before continuing, then regenerate any slide with missing, wrong, or unreadable text.

Risk: Some user-facing confirmation wording is hardcoded in Chinese, which may be unsuitable for English-only workflows.

Mitigation: Localize approval prompts and review wording for the target audience before using the skill in an English-only setting.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tseng71/skills/image-deck)
- [Prompt Patterns](references/prompt-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Files]

**Output Format:** [Markdown guidance and prompt groups with optional generated image, PPTX, PDF, and log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Codex built-in image_gen (GPT Image 2); generated slides are full-slide raster images with visible text rendered inside the image.]

## Skill Version(s):

0.1.26 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
