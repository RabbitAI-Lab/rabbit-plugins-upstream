## Description:

Assign an incident owner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Operations and incident-response teams use this skill to assign an incident owner from supplied severity routing guidance for the current alert.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Assignment guidance may include incident-routing details from the active service session.

Mitigation: Confirm that assignment_guidance contains only incident-routing information appropriate to share in the active session before use.

Risk: Incomplete or outdated routing guidance could produce an incorrect incident owner assignment.

Mitigation: Review the returned matched_rule, severity, and assignment against current operational routing guidance before acting on the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-workbench)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured object with alert_id, severity, assignment, and matched_rule]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-supplied assignment_guidance; no credentials, file access, or external access required.]

## Skill Version(s):

1.0.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
