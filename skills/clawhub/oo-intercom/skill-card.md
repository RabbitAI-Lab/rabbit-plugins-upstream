## Description:

This skill helps an agent handle Intercom requests through OOMOL's oo CLI, including reading, creating, updating, and deleting Intercom data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support, operations, and engineering teams use this skill to read and manage Intercom workspace data through OOMOL-connected Intercom actions, including contacts, conversations, tickets, articles, tags, events, counts, and admin records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include piping remote installer scripts directly into a shell.

Mitigation: Prefer a verified package-manager or installer path, and review any remote script locally before execution.

Risk: Write actions can change Intercom contacts or conversations.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before execution.

Risk: The close conversation action is destructive.

Mitigation: Require explicit approval for the specific conversation target before running the action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-intercom)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Intercom homepage](https://www.intercom.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are intended for the OOMOL oo CLI and may return JSON responses from Intercom connector actions.]

## Skill Version(s):

1.0.6 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
