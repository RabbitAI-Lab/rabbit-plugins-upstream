## Description:

Guides course creators through planning and producing landscape lessons with a consistent digital lecturer, narrated slides, and selective avatar appearances using dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, educators, and training teams use this skill to turn lesson scripts and teaching materials into narrated course videos with a reusable digital lecturer and slide-first presentation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Model calls can consume paid dLazy credits, especially when generating longer avatar appearances or retrying failed outputs.

Mitigation: Estimate credit usage and check available balance before batches; preview requests where supported and limit avatar time.

Risk: Course files and selected media may be uploaded to dLazy services during production.

Mitigation: Upload only materials approved for third-party processing, and remove sensitive content before submission.

Risk: The workflow is written primarily in Chinese and may not fit other languages without adaptation.

Mitigation: Translate or adapt prompts and review narration, slides, and final video for the intended audience.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy homepage](https://dlazy.com)
- [Course production pipeline](artifact/pipeline.md)
- [Avatar and slide recipes](artifact/recipes.md)
- [Troubleshooting and compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers avatar images, narration, course slides, and video assembly; generating media requires separate tools and paid dLazy credits.]

## Skill Version(s):

1.0.15 (source: ClawHub release; skill frontmatter states 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
