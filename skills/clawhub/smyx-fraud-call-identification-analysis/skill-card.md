## Description:

Analyzes call recordings, audio URLs, or transcripts for possible fraud and provides risk assessments and an anti-fraud report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing suspicious calls and developers building anti-fraud workflows can analyze call audio or transcripts, assess potential scam indicators, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call recordings, transcripts, or supplied URLs are sent to lifeemergence.com services for analysis.

Mitigation: Disclose remote processing and obtain appropriate consent before submitting sensitive call content.

Risk: Report history can be queried from cloud storage and linked to a locally created or reused identity with tokens stored in a workspace SQLite database.

Mitigation: Limit access to report history and the local workspace, and review stored identity and token handling before installation.

Risk: The broader cloud media-analysis and authentication behavior is not fully explained by the fraud-call description.

Mitigation: Review the skill and its remote-service behavior before enabling it for users.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Fraud analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Markdown reports or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk assessments, fraud indicators, recommendations, report links, or requested report history.]

## Skill Version(s):

9.9.18 (source: ClawHub release; packaged frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
