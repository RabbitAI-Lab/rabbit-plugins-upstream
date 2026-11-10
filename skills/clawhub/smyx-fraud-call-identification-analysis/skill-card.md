## Description:

Analyzes call recordings or transcripts for suspected scam patterns, assigns a risk level, and returns an anti-fraud report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and security teams can review call recordings or transcripts for suspected fraud, understand the assessed risk, and receive prevention suggestions and a report link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call or video content may be sent to a remote service for analysis.

Mitigation: Share only content you are authorized to provide, and review the service's privacy and retention terms before submitting recordings.

Risk: The scan flags account registration and token storage as considerations.

Mitigation: Review how account identity and tokens are handled, and avoid sharing credentials in prompts or reports.

Risk: Analysis may still run when `--export-env-only` is specified.

Mitigation: Do not rely on this option to prevent analysis; verify its behavior before using the skill with sensitive content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Structured JSON analysis with risk assessment, prevention suggestions, and report links; plain text is also supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a fraud classification, risk level, report details, prevention suggestions, and an export link; results can optionally be saved to a file.]

## Skill Version(s):

9.9.21 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
