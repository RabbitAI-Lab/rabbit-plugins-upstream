## Description:

Generate textual descriptions of one or more images when the current session model has no image input by delegating selected image files to a vision-capable model through `opencode run`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j3ffyang](https://clawhub.ai/user/j3ffyang)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content workflows use this skill to get factual image descriptions, captions, or ordered image notes when the active agent cannot inspect images directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are sent to OpenRouter-backed vision models for processing.

Mitigation: Avoid sensitive photos, private documents, or images with confidential metadata unless the user has reviewed the files and accepted external processing.

Risk: Image descriptions may contain factual mistakes because the main agent cannot independently verify image content.

Mitigation: Treat generated descriptions as draft observations and have the user spot-check important details before downstream use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j3ffyang/skills/read-image)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with optional labeled lists and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Descriptions are AI-generated from selected image files and should be reviewed for factual accuracy before reuse.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
