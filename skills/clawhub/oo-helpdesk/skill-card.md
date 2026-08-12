## Description:

HelpDesk lets agents read, create, update, move, and delete HelpDesk tickets through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Customer support operators and agents use this skill to manage HelpDesk tickets, agents, and teams from a connected OOMOL account while preserving confirmation gates for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and destructive actions can create, update, move, or delete HelpDesk tickets.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running state-changing actions.

Risk: Connector action schemas may change and invalid payloads can cause failed or unintended requests.

Mitigation: Inspect the live action schema with `oo connector schema` before building each action payload.

Risk: Authentication, connection, scope, or billing failures can block execution.

Mitigation: Run setup or remediation steps only after a command fails with the matching error.

## Reference(s):

- [HelpDesk Homepage](https://www.helpdesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live HelpDesk connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
