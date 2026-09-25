## Description:

Knowledge-course / online-teaching avatar lecturer with landscape base-portrait recipes and a slide-first pipeline for creating paid-course, training, or knowledge-sharing videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, trainers, and internal enablement teams use this skill to plan and generate cost-aware digital-human course videos from PPTs, documents, scripts, and media. It focuses avatar generation on opening, transition, and closing segments while keeping the main lesson slide-first.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Course documents, images, audio, and other media may be uploaded to dLazy services or model APIs when users run the generated commands.

Mitigation: Avoid sending confidential training materials unless they are approved for dLazy handling, and review file arguments before execution.

Risk: Batch image, TTS, and avatar-driving calls can consume paid external model credits.

Mitigation: Use the skill's dry-run and cost-check guidance before running batches, and verify resolution, duration, and input limits first.

Risk: Authentication may be stored in the normal dLazy config location or supplied through an environment variable.

Mitigation: Handle API keys as secrets, avoid committing config files or environment dumps, and rotate keys if exposed.

Risk: Generated digital-human course content can imply credentials, endorsements, training outcomes, or AI-human identity claims that require review.

Mitigation: Review course scripts and generated visuals for education-advertising claims, invented credentials or endorsements, and platform AI-content labeling requirements before publication.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [dLazy Homepage](https://dlazy.com)
- [Pipeline Guide](artifact/pipeline.md)
- [Recipe Library](artifact/recipes.md)
- [Troubleshooting and Compliance](artifact/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend dLazy CLI calls that upload provided course files or media and consume paid external model credits.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
