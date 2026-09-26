## Description:

Analyzes bathroom doorway or silhouette-only video to estimate an older adult's bathroom occupancy and flag stays exceeding a default 30-minute threshold.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care providers use bathroom entry and exit footage to identify unusually long stays and review alerts or historical reports. Alerts support, but do not replace, an in-person safety check.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bathroom footage and report history are sent to a cloud service.

Mitigation: Obtain informed consent from the monitored person or authorized caregiver; prefer doorway footage or pre-blurred, silhouette-only video over raw in-bathroom footage.

Risk: The skill automatically creates or reuses a local identity and token state for cloud requests.

Mitigation: Review the configured service and local identity handling before installation or use, and limit access to stored identity and reports.

Risk: An occupancy alert may not establish why a person has remained in the bathroom.

Mitigation: Have a caregiver promptly verify urgent alerts by phone or in person; do not treat the output as a medical diagnosis.

## Reference(s):

- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Text]

**Output Format:** [JSON or Markdown, including report tables and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional saved report file and cloud-hosted report links.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; packaged SKILL.md says 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
