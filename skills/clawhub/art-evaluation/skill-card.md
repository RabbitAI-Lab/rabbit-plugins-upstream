## Description:

对上传的艺术作品进行评估，提供点评、改进建议、模拟优化图，并列出该类作品的代表艺术家及代表作品

This skill is ready for commercial/non-commercial use.

## Publisher:

[nickliu54](https://clawhub.ai/user/nickliu54)

### License/Terms of Use:

MIT-0

## Use Case:

Artists, art educators, and developers can use this skill to evaluate uploaded artwork across categories such as sketch, comics, calligraphy, landscape, figure, and oil painting. It returns critique, improvement suggestions, optional optimized sample-image output, and representative artist references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Artwork may be processed by a local model or external image-generation service if the placeholder implementation is replaced.

Mitigation: Use only images suitable for that processing path and review any added model or API invocation code before deployment.

Risk: Generated sample images and critique may be subjective or misleading for professional assessment.

Mitigation: Have a qualified reviewer check the critique, suggestions, and generated image before relying on them for instruction, publication, or commercial decisions.

## Reference(s):

- [Evaluation Criteria](references/evaluation_criteria.md)
- [Representative Artists and Works](references/representative_artists.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Files, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON script output and optional image file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce critique text, improvement suggestions, criteria lists, and a generated or copied optimized image path.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
