## Description:

Analyzes surveillance images and video to identify signs of negative emotions in children and can provide soothing reminders and caregiver notifications.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and childcare providers use it to review emotion analysis from children's surveillance images or videos and access reports for follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Report histories may cross account boundaries, and the export-only option may not prevent children's footage from being processed.

Mitigation: Wait for fixes before using real children's footage; confirm where uploads are stored and how to delete them.

Risk: Authenticated requests may expose credentials if sent to an untrusted or insecure destination.

Mitigation: Restrict authenticated requests to trusted HTTPS destinations.

Risk: Caregivers may rely on automated alerts as a substitute for supervision.

Mitigation: Keep adult supervision in place and treat alerts as supplementary.

## Reference(s):

- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Report links]

**Output Format:** [Structured analysis reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Emotion findings, suggestions, caregiver alerts, and report links may be included.]

## Skill Version(s):

1.0.33 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
