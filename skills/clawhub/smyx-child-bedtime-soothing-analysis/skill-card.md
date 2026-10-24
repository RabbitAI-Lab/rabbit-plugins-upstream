## Description:

Analyzes child-bedroom audio and video through a cloud service and returns reports on bedtime distress and nighttime awakenings, but does not itself activate soothing devices or alert caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents or caregivers can submit consented child-bedroom recordings or media URLs to request an analysis report and review cloud-stored report history. This is not a real-time monitoring, medical diagnosis, or caregiver-alert system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive child-bedroom audio or video, including media URLs, may be sent to the configured cloud service.

Mitigation: Use only in a consented single-user setting; verify the service's privacy, access, and retention practices before submitting child media.

Risk: Silent identity and token persistence can mix users' data in shared workspaces.

Mitigation: Avoid shared workspaces unless identity isolation and token storage are fixed and verified.

Risk: Claimed automatic soothing and parent alerts are not implemented by the inspected code.

Mitigation: Do not rely on this skill for real-time soothing, parent alerts, or safety escalation without separately implemented and verified controls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-child-bedtime-soothing-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis text or JSON, with Markdown history links when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the returned report to a user-specified file; cloud report history can be queried.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled frontmatter says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
