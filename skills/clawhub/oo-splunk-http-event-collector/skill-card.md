## Description:

Operate Splunk HTTP Event Collector through an OOMOL-connected account using the oo CLI for schema inspection and event submission.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect live OOMOL connector schemas and send structured or raw events to connected Splunk HTTP Event Collector instances while keeping credentials in OOMOL-managed connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The available actions write structured or raw event data into Splunk.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: Incorrect event payloads could be rejected or create misleading Splunk data.

Mitigation: Fetch the live connector schema before constructing each payload and match the authoritative action contract.

Risk: First-time use may require local oo CLI installation and OOMOL sign-in.

Mitigation: Install and authenticate only when the command fails for missing CLI, authentication, or connection reasons.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-splunk-http-event-collector)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Splunk HTTP Event Collector homepage](https://www.splunk.com)
- [OOMOL app connection setup](https://console.oomol.com/app-connections?provider=splunk_http_event_collector)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown with inline bash, PowerShell, text, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
