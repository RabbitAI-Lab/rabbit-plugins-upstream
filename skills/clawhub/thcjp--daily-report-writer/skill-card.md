## Description:

Generates structured Markdown daily report drafts from user-provided work content and writes them to a reports directory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, team leads, and workflow builders use this skill to turn daily work notes, dates, and style preferences into editable Markdown daily report drafts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad command execution and file access for a task that primarily writes Markdown reports.

Mitigation: Run it in a constrained workspace, review any proposed commands before execution, and grant write access only to the intended reports directory when possible.

Risk: Daily report inputs and generated outputs may contain sensitive work data.

Mitigation: Avoid providing secrets, credentials, customer data, or confidential business details unless the environment and publisher controls are acceptable for that data.

Risk: API-related authority is mentioned without a narrow requirement for local report drafting.

Mitigation: Do not provide API keys unless the publisher narrows the API behavior and documents why external access is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/daily-report-writer)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown daily report draft written as a local file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for Chinese-language daily report writing; output should be reviewed before sharing or publication.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
