## Description:

Analyzes multi-day bedroom and dining video for changes in time spent in bed and eating behavior, then produces a behavioral-change report for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family members, community care teams, and developers use the skill to review behavior changes observed in continuous bedroom and dining video and to obtain a report for follow-up. The output is an observational aid, not a depression diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags possible cross-user access to private reports.

Mitigation: Require sender-specific account isolation and verify report access controls before use.

Risk: The client may upload complete bedroom video even when a no-analysis option is advertised; this footage contains highly sensitive personal information.

Mitigation: Obtain explicit consent for cloud processing, confirm the no-analysis option works, and verify retention and deletion controls before uploading private footage.

Risk: Credential destinations require review before sending private data through the service.

Mitigation: Restrict credential destinations to approved services and confirm the upload destination before processing footage.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured behavior report in JSON or a Markdown summary, with report links when returned]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include bed-time and eating indicators, baseline comparisons, behavior-change alerts, and caregiver follow-up reminders; not a medical diagnosis.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
