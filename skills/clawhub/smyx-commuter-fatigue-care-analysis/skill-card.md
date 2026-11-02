## Description:

Analyzes living-room footage from the first 30 minutes after arrival home for fatigue indicators and returns a report with supportive care suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Smart-home users and integrators use the skill to review potential after-work fatigue signals from living-room footage and receive supportive, non-diagnostic suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private household footage may leave the device for analysis.

Mitigation: Before use, clarify who receives the footage and how it is retained and deleted; start with consented test footage.

Risk: Remote accounts and saved login tokens have unclear user controls, and the export-only option still permits analysis.

Mitigation: Clarify how remote accounts and saved tokens can be removed, and require the export-only behavior to be fixed before relying on it.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Markdown or JSON analysis report, depending on the selected detail level]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue indicators, supportive suggestions, and report links; it is not a medical diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved release evidence; artifact frontmatter lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
