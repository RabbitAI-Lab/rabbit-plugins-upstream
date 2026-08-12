## Description:

Turn community guidelines into an askable digital-human start-here course.

This skill is ready for commercial/non-commercial use.

## Publisher:

[personwiseai](https://clawhub.ai/user/personwiseai)

### License/Terms of Use:

MIT-0

## Use Case:

External community teams and creators use this skill to turn supplied community guidelines, welcome materials, and program documentation into a grounded onboarding course. The course is presented by a digital human and remains askable through learner voice questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update the PersonWise CLI before creating a course.

Mitigation: Require explicit user approval for install or update prompts and use only the bundled PersonWise bootstrap flow.

Risk: The workflow uses browser OAuth and uploads user-selected course materials to PersonWise.

Mitigation: Do not request secrets; use the browser OAuth flow and upload only files the user named, attached, or explicitly approved.

Risk: Course creation can consume existing course credits and may expose a course more broadly if link access or publication is requested.

Mitigation: Treat a create request as authorization only for the requested course count, never purchase credits automatically, and default access to private unless the user asks for broader access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/personwiseai/skills/personwise-community-onboarding)
- [PersonWise publisher profile](https://clawhub.ai/user/personwiseai)
- [PersonWise service](https://personwise.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Agent guidance with JSON inputs and CLI command workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a PersonWise interactive digital-human course through the PersonWise CLI; defaults course access to private unless the user requests broader access.]

## Skill Version(s):

2.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
