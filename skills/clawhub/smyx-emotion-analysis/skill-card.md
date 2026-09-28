## Description:

Analyzes facial videos or video URLs for micro-expressions and returns emotion reports and cloud report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People analyzing facial videos can request emotion reports and retrieve past reports. Treat the findings as tentative rather than proof of a person's feelings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive face videos or URLs are sent to lifeemergence.com services, and report history is queried in the cloud.

Mitigation: Review the service's data handling and obtain consent before submitting face media or querying reports.

Risk: The skill silently creates or reuses persistent service identity and tokens in a local workspace database.

Mitigation: Use a controlled workspace, restrict access to stored credentials, and review or remove them when no longer needed.

Risk: Facial-expression reports can misrepresent a person's actual emotions.

Mitigation: Do not treat reports as definitive proof of emotions or use them for consequential decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured emotion reports, JSON results, and Markdown tables of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links; results can optionally be saved to a file.]

## Skill Version(s):

1.0.16 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
