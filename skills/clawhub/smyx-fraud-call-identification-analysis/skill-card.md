## Description:

Helps analyze call recordings or text for suspected fraud and presents risk assessments, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

People and security teams can submit call recordings or transcripts for suspected-scam analysis, review risk guidance, and request earlier cloud reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call media or URLs are sent to an external cloud service.

Mitigation: Obtain permission before submitting sensitive calls and confirm the service's data-handling terms.

Risk: The workflow can create and store local account tokens and retrieve cloud history linked to an internally managed identity.

Mitigation: Review token storage and history-access behavior before installation; restrict local access and use only with an approved account.

Risk: The fraud-call description differs from the broader, video-oriented packaged implementation.

Mitigation: Test the intended call inputs and verify the reports before relying on fraud classifications.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Fraud analysis API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON]

**Output Format:** [Markdown report or history table, with optional JSON details and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fraud risk level and prevention suggestions when available]

## Skill Version(s):

9.9.19 (source: ClawHub release; bundled SKILL.md declares 1.0.21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
