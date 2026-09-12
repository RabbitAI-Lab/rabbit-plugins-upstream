## Description:

Generates a designed portfolio-resume image from resume content provided in conversation text, using optional style guidance and a fixed portfolio-resume layout prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert resume content and optional visual style direction into a tall portfolio-resume image for presentation or sharing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resume content can contain sensitive personal data and may be sent to configured text and image APIs.

Mitigation: Use the skill only in a private single-user environment with an explicit privacy notice and approved API configuration.

Risk: Intermediate resume text is written under predictable temporary paths without clear cleanup or access controls.

Mitigation: Require unpredictable temporary directories, restrictive file permissions, and immediate cleanup of intermediate files before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-image-resume)
- [Fixed portfolio-resume layout prompt](artifact/prompts/resume.md)

## Skill Output:

**Output Type(s):** [Image, Text, JSON]

**Output Format:** [PNG image with a short text summary; verbose mode may include the generation prompt and timing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default output uses a 9:16 aspect ratio and 2k image size; resume details may be condensed to fit the visual layout.]

## Skill Version(s):

2026.9.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
