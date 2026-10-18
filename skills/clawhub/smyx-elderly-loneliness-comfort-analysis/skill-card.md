## Description:

Analyzes fixed-camera video of an older adult living alone for behaviors associated with loneliness and provides a behavioral summary and suggested companionship actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and elder-care teams use video from a fixed camera in a home or care room to review loneliness-related behavior, receive companionship suggestions, and consult historical reports. The results are behavioral observations, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private elder-monitoring video or optional audio is uploaded to cloud services.

Mitigation: Obtain explicit consent from the monitored adult and authorized caregivers; review provider access controls, retention, deletion, and local legal requirements before deployment.

Risk: Automatic identity creation and local token storage can expose sensitive report access if the workspace is shared.

Mitigation: Restrict workspace and report access, and review how locally stored tokens and cloud reports are protected and removed.

Risk: Behavior-based loneliness scores may be mistaken for a mental-health diagnosis.

Mitigation: Treat scores as observations only; have caregivers review the context and refer suspected mental-health concerns to qualified professionals.

## Reference(s):

- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Text or Markdown reports with behavioral observations, a loneliness index, suggested actions, and report links; JSON output is also supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a cloud-hosted historical report list or a saved result file.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
