## Description:

Analyzes pet ear images or videos for visible redness, discharge, and earwax, then returns observation alerts and suggestions for veterinary follow-up without providing a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding centers, and veterinary clinics can use the skill to review pet ear images or videos for visible redness, discharge, or wax buildup and receive a structured observation report to help decide whether to seek veterinary care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious with high confidence, citing credential and account handling, broad credentialed web requests, and behavior that does not consistently match the stated analysis purpose.

Mitigation: Follow the scanner guidance and resolve these concerns before installation; review the required credentials, permissions, and request destinations.

Risk: The workflow accepts pet images and videos and sends them for remote analysis, which can expose sensitive media.

Mitigation: Use only media you are authorized to share, and confirm the analysis service and its data handling are acceptable before submitting it.

Risk: Visual findings may be incomplete and are not a veterinary diagnosis.

Mitigation: Treat results as observations only and consult a veterinarian about concerning symptoms or suspected illness.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Structured observations and alerts in Markdown or JSON, with suggestions and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual observations only; the report does not provide a medical diagnosis.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
