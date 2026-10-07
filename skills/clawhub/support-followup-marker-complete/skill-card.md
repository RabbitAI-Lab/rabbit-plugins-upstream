## Description:

Turns a support intake message into a case digest and follow-up comment, saves a local case record, and optionally delivers it to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams use this skill to turn intake messages into a digest and a follow-up case comment, with a local case record and optional configured delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery can send support case data outside the local workspace without an in-run confirmation.

Mitigation: Leave delivery settings unset for local-only use; otherwise use only approved internal destinations.

## Reference(s):

- [Support Intake Digest release](https://clawhub.ai/wxt-ai/skills/support-followup-marker-complete)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the case digest, follow-up comment, local record receipt, and delivery status.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
