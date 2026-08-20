## Description:

Generates a designed portfolio-resume image from resume content provided in conversation text by extracting optional style instructions, converting the resume into a fixed portfolio-resume layout prompt, and generating the final image through sn-image-base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to turn user-provided resume text and optional visual style directions into a portfolio-style resume image. It is intended for visual resume or resume poster generation, not ATS resume authoring or uploaded-document parsing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume details may contain sensitive personal data and are written temporarily to local /tmp storage and sent through the configured SenseNova/sn-image-base text and image services.

Mitigation: Provide only necessary resume content, confirm API configuration and data handling expectations, and delete the generated task directory after generation on shared systems.

Risk: The generated visual resume may compress or omit long text because the skill targets a designed portfolio-resume layout rather than a conventional text resume.

Mitigation: Review the generated image against the source resume before using it and regenerate with shorter content or clearer priorities when important details are missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-image-resume)
- [SKILL.md](artifact/SKILL.md)
- [Fixed portfolio-resume layout prompt](artifact/prompts/resume.md)

## Skill Output:

**Output Type(s):** [Text, Files, JSON]

**Output Format:** [Text summary plus a generated PNG image file; verbose mode may also include the generated prompt and timing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default aspect ratio is 9:16 and default image size is 2k; generated files are stored under a task directory in /tmp.]

## Skill Version(s):

2026.8.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
