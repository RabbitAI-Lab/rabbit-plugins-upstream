## Description:

Analyzes cat scratch-post videos to summarize scratching frequency, duration and estimated intensity, with observational stress and claw-health indicators rather than diagnoses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to analyze scratch-post video, monitor scratching patterns and review past reports. Its stress and claw-health observations are not veterinary diagnoses or behavior-correction advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet video may be uploaded to external analysis services without clear media retention terms.

Mitigation: Confirm the destination and media retention and deletion controls before sending videos; share only media you are authorized to upload.

Risk: The skill may silently create or reuse a service identity and store account tokens in a local workspace database.

Mitigation: Review identity and token handling before installation; limit access to the workspace database and establish token deletion procedures.

Risk: History-related phrases can automatically retrieve account-linked cloud reports.

Mitigation: Require user confirmation before retrieving history and verify the correct account is in use.

Risk: An unsafe import-path pattern warrants manual review before execution.

Mitigation: Review the packaged scripts and prefer a release that removes the unsafe import-path manipulation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-scratch-frequency-intensity-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured JSON analysis or Markdown report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Observations may include scratching frequency, session duration, relative intensity, stress and claw-health indicators, and report links.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
