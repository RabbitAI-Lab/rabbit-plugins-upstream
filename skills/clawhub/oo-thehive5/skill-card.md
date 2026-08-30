## Description:

Enables agents to read, create, and update TheHive 5 data through the OOMOL thehive5 connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Security operations teams and developers use this skill to list, retrieve, and create TheHive 5 alerts and cases from an agent through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create TheHive 5 cases and alerts through the user's connected OOMOL account.

Mitigation: Confirm write payloads and expected effects with the user before running write actions.

Risk: Using the connector depends on trusting the oo CLI and OOMOL account integration.

Mitigation: Only complete setup or reconnect the account when the user trusts that integration.

Risk: Connector action schemas may differ from assumptions in a prompt.

Mitigation: Inspect the live action schema before constructing each connector payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-thehive5)
- [TheHive 5 homepage](https://strangebee.com/thehive)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write actions require confirmation of the exact payload and expected effect before execution.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
