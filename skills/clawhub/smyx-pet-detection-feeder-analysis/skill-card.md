## Description:

Analyzes feeder or IPC camera images and videos to detect cats and dogs, recognize individual pets, enroll pet identities, and retrieve past detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-feeder developers use the skill to identify cats and dogs in feeder-camera media, register individual pets, and review detection history for multi-pet feeding workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Camera images, videos, and report history are processed through a cloud service.

Mitigation: Use only with footage and report data you are comfortable sharing with the lifeemergence service.

Risk: The skill can silently create or reuse an identity and persist account tokens locally.

Mitigation: Review the identity and local token-storage behavior before use, especially in shared workspaces.

Risk: Requests for historical reports can automatically query cloud-stored history.

Mitigation: Check that cloud report access is appropriate before requesting or sharing historical reports.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured text or JSON results; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or save results to a file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
