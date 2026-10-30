## Description:

Analyzes call recordings, URLs, or transcripts for scam patterns, estimates risk, and produces an anti-fraud report with recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and security teams use this skill to review call recordings or transcripts, identify possible scam patterns, and receive a risk assessment and prevention suggestions. It can also retrieve prior analysis reports from the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Files may be submitted even when export-only mode is selected; the skill may also enroll a cloud account and store authentication tokens locally.

Mitigation: Before use, verify export-only behavior, get clear consent for uploads and account enrollment, and confirm the service's privacy, retention, charging, and token-removal terms. Avoid sensitive recordings.

Risk: The --api-url option may not change the request destination.

Mitigation: Verify the service destination independently and do not rely on --api-url to protect sensitive input.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis reports, with risk assessment and recommendations; Markdown tables for report listings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include links to reports when available. Results are for anti-fraud reference and are not an official determination.]

## Skill Version(s):

9.9.20 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
