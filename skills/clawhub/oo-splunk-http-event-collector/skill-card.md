## Description:

Enables agents to inspect the Splunk HTTP Event Collector connector schema and send structured or raw events through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to send structured or raw events to Splunk HTTP Event Collector through OOMOL while relying on live connector schemas for request shape. It is intended for authenticated OOMOL-connected environments where event payloads can be reviewed before write actions run.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes mutable remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a trusted source and verification process before using the skill.

Risk: The skill sends events to Splunk HTTP Event Collector and may transmit sensitive or unnecessary data if payloads are not reviewed.

Mitigation: Confirm each event payload and effect with the user before execution, and avoid sending secrets or unnecessary sensitive data.

Risk: The release security summary says the original description overstates what the skill can safely do.

Mitigation: Limit use to inspecting live connector schemas and sending structured or raw Splunk HEC events through an OOMOL-connected account.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/oomol/skills/oo-splunk-http-event-collector)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Splunk homepage](https://www.splunk.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before payload construction and user confirmation before write actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
