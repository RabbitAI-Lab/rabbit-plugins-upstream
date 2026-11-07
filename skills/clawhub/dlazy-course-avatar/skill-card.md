## Description:

Guides agents in creating digital-human lecturers and slide-first videos for paid courses, training modules, and knowledge-sharing lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External course creators and training teams use this skill to plan consistent digital-human lecturer assets and produce slide-first course videos with voiceover and selected on-screen lecturer segments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Course materials sent to cloud services may contain confidential content or hidden document notes.

Mitigation: Use materials approved for cloud processing and remove confidential content and hidden notes before upload.

Risk: Portrait generation or avatar use may involve personal likenesses.

Mitigation: Use synthetic portraits or portraits with consent.

Risk: Upload commands may match unintended files, API credentials may be exposed, and model calls may incur costs.

Mitigation: Review the files matched by upload commands, protect the API key, and preview costs with --dry-run.

Risk: The external CLI package and hosted execution are outside the inspected artifacts.

Mitigation: Review the CLI package and hosted service before relying on them for sensitive course content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-course-avatar)
- [Dlazy homepage](https://dlazy.com)
- [Dlazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples and JSON payload/configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides production workflows and cost estimates; final video assembly uses a separate template or tool.]

## Skill Version(s):

1.0.29 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
