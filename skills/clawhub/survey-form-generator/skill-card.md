## Description:

Generates a structured survey questionnaire from a user's research goal and renders it as a local HTML form for preview, trial completion, copying, printing, or PDF export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zenobiazizi](https://clawhub.ai/user/zenobiazizi)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to turn survey goals for customer satisfaction, NPS, market research, product feedback, employee surveys, and training evaluation into usable questionnaire files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Survey goals, audience, and intended use may be sent to Dify's cloud service during questionnaire generation.

Mitigation: Avoid entering confidential customer lists, HR details, unreleased strategy, or sensitive business context unless approved; use the local fallback path when cloud submission is not acceptable.

Risk: The server security review reports an embedded service token and a suspicious verdict.

Mitigation: Review the skill before deployment, confirm the token handling is acceptable for the intended environment, and rotate or remove exposed credentials where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zenobiazizi/skills/survey-form-generator)
- [README](artifact/README.md)
- [CHANGELOG](artifact/CHANGELOG.md)
- [Dify API endpoint](https://api.dify.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown guidance with generated JSON survey structure and an HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated HTML responses remain local in browser memory; the file is intended for preview, trial completion, copying questions into survey platforms, printing, or PDF export.]

## Skill Version(s):

1.0.1 (source: server release metadata and CHANGELOG, released 2026-08-24)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
