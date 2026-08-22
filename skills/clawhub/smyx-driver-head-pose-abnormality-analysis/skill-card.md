## Description:

Analyzes in-cabin DMS camera images or video to estimate driver head pose and report head-down, side-view, or roll-abnormality distraction events with alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and fleet-safety integrators use this skill to submit driver-facing DMS images, videos, or URLs for cloud analysis, then retrieve structured distraction warnings and historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver or passenger video, video URLs, identity-linked metadata, and report queries may be sent to a third-party backend.

Mitigation: Use only with clear consent, approved media sources, and documented retention, deletion, and privacy handling for fleet or workplace deployments.

Risk: The skill silently creates or reuses local identity records and stores authentication tokens locally.

Mitigation: Run in a controlled workspace, review token storage before deployment, rotate or clear stored credentials as needed, and avoid shared local environments.

Risk: Packaged configuration includes development or private HTTP endpoint settings.

Mitigation: Verify the active endpoint configuration before use and require production-approved HTTPS endpoints for operational deployments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-driver-head-pose-abnormality-analysis)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands]

**Output Format:** [Markdown text with JSON-formatted analysis content and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export URLs and historical report lists.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
