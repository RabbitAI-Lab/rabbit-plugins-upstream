## Description:

Detects potential employee phone use in workplace images or video and produces structured monitoring reports with counts, durations, warnings, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Workplace operations or compliance teams use this skill to review authorized office-area images or video for possible phone-use behavior and generate monitoring reports for internal management review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive workplace images or video for employee phone-use monitoring.

Mitigation: Use only with documented authority, employee notice or consent where required, defined retention limits, and review under applicable labor and privacy rules.

Risk: Security evidence flags unsafe network and identity defaults for a skill that handles employee media and report history.

Mitigation: Require HTTPS-only endpoints, disable debug HTTP tracing, and provide a way to reset or delete local identity tokens and report history before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-phone-usage-monitoring-analysis)
- [Workplace phone usage monitoring API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and optional saved output files.]

## Skill Version(s):

1.0.11 (source: server release metadata; SKILL.md frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
