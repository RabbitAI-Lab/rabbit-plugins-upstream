## Description:

Knowledge-course / online-teaching avatar lecturer — 16 landscape base-portrait recipes plus the slide-first pipeline that keeps a 20-minute lesson under 3000 credits. Use when the user wants a digital human to teach a paid course, a training module or a knowledge-sharing video on platforms like Xiaoetong, Tencent Classroom, Bilibili, YouTube or an internal LMS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Course creators, instructors, and training teams use this skill to turn course materials into videos with a consistent digital lecturer, narration, and slide-focused scenes. It provides portrait prompts, segmentation and production guidance, and CLI examples for course video workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The publisher's CLI documentation says uploaded local media are replaced with public URLs, which may expose confidential or identifying course assets.

Mitigation: Use only materials approved for external processing; omit confidential or identifying assets unless that handling is acceptable.

Risk: Video generation uses credits and the CLI stores an API key in its configuration file.

Mitigation: Review estimated costs with --dry-run and protect the saved API key.

## Reference(s):

- [dLazy CLI documentation on local files and data URLs](https://github.com/dlazy-ai/cli#local-files--data-urls)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes portrait prompts, video workflow steps, and cost and segmentation guidance.]

## Skill Version(s):

1.0.26 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
