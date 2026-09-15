## Description:

This skill lets an agent use an OOMOL-connected ngrok account to inspect endpoints, reserved domains, tunnel sessions, and tunnels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query ngrok account resources from an agent session through the OOMOL connector workflow. It is focused on read-only endpoint, domain, tunnel session, and tunnel listing or lookup tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can execute a remote installer with a pipe-to-shell command.

Mitigation: Use that installer only after independently trusting and verifying the source, or install the oo CLI through an approved internal path.

Risk: ngrok request and response data is routed through OOMOL when the connector is used.

Mitigation: Connect ngrok with the least privileges needed and confirm that routing this data through OOMOL is acceptable for the account and task.

## Reference(s):

- [ngrok homepage](https://ngrok.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ngrok)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and an execution identifier when commands are run with JSON output.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
