## Description:

Respond.io helps agents operate Respond.io through OOMOL's `oo` CLI for contact, tag, conversation, channel, and user workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read and manage Respond.io workspace data through an OOMOL-connected account. It supports contact management, tag changes, conversation assignment and status updates, internal comments, and paginated listing of channels, contacts, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote shell installer commands for the oo CLI.

Mitigation: Install only after trusting OOMOL and the oo CLI, and prefer a manually verified or official package-manager installation before use.

Risk: The connector can create, update, delete, assign, close, or retag Respond.io CRM records.

Mitigation: Require explicit confirmation of the exact target, payload, and effect before any write, delete, tag removal, conversation assignment, or status change.

Risk: Incorrect payloads could affect the wrong contact or conversation.

Mitigation: Fetch the live connector schema before constructing payloads and verify identifiers such as contact ID, email address, or phone number with the user for state-changing actions.

## Reference(s):

- [Respond.io ClawHub skill page](https://clawhub.ai/oomol/skills/oo-respond-io)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Respond.io homepage](https://respond.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads or connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payload construction; state-changing and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
