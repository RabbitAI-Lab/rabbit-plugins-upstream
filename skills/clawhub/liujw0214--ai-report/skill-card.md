## Description:

Generates structured daily, weekly, and monthly AI assistant work reports from recent work activity, discussion topics, decisions, follow-up items, and plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liujw0214](https://clawhub.ai/user/liujw0214)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to turn AI assistant activity into concise daily, weekly, or monthly status reports for work summaries and handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read dated agent memory and save generated reports that may contain private, confidential, or credential-like information.

Mitigation: Use explicit review before saving or sharing reports, and enable automatic generation only when local retention and redaction expectations are acceptable.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Structured Markdown reports, with optional PDF or HTML export when pandoc is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be saved under ~/.openclaw/reports/ by reporting period.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
