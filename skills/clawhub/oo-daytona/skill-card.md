## Description:

Daytona (daytona.io). Use this skill for ANY Daytona request: reading, creating, updating, and deleting data through the OOMOL Daytona connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Daytona sandboxes through an OOMOL-connected account. It guides an agent to inspect live action schemas and run Daytona connector actions for sandbox creation, lookup, listing, start, stop, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Create, start, stop, and delete actions can change Daytona sandbox state.

Mitigation: Confirm the exact payload and intended effect with the user before running any action tagged write or destructive.

Risk: Connector setup and CLI installation require trust in OOMOL and the user's connected account.

Mitigation: Only run installer, login, or connection steps when needed for this integration and after the user agrees to proceed.

Risk: Connector action inputs can drift from static skill text.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing any `oo connector run` payload.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-daytona)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Daytona Homepage](https://www.daytona.io/)
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Daytona Connector Setup](https://console.oomol.com/app-connections?provider=daytona)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to inspect the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
