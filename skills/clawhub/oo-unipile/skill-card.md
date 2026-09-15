## Description:

Unipile helps an agent search and read Unipile account, chat, and message data through an OOMOL-connected oo CLI session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve Unipile accounts, chats, messages, and chat message lists through an OOMOL-connected oo CLI session. The skill guides the agent to inspect live connector schemas before sending JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts directly in a shell.

Mitigation: Prefer a verified, versioned oo CLI installation or inspect the installer before execution; do not run the installer automatically unless the user trusts the OOMOL endpoint.

## Reference(s):

- [Unipile homepage](https://www.unipile.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-unipile)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
