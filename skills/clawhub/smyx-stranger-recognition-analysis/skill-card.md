## Description:

Identifies unfamiliar people in surveillance images and videos by comparing faces against a known-person database and returns recognition reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security administrators and operators use the skill to compare faces in submitted surveillance images or videos against a known-person database, review recognition reports and alerts, and query report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the no-analysis option is ignored and credential forwarding has no destination restrictions.

Mitigation: Request fixes for both behaviors before using private footage, and confirm destination restrictions before forwarding credentials.

Risk: Face enrollment adds people to a cloud reference database shared under the selected identity.

Mitigation: Confirm the service's retention and deletion policies, use separate workspaces or accounts for different users, and scope enrollment to the intended identity.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured JSON or human-readable text and Markdown reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include recognition results, alerts, and report links; history listings are formatted as Markdown tables.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
