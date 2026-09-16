## Description:

Devin (devin.ai). Use this skill for ANY Devin request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Devin organization sessions through an OOMOL-connected account, including creating sessions, inspecting identity and session data, sending messages, and terminating sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running installer scripts from the internet.

Mitigation: Review the installer, prefer a verified release or package manager, and require explicit approval before allowing an agent to install the oo CLI.

Risk: Write actions can create sessions or send messages that change Devin state.

Mitigation: Confirm the exact payload and expected effect with the user before running create_session or send_message.

Risk: The terminate_session action can end a Devin session.

Mitigation: Confirm the target session and obtain explicit approval before terminating or archiving a session.

## Reference(s):

- [ClawHub Devin Skill](https://clawhub.ai/oomol/skills/oo-devin)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Devin](https://devin.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo CLI commands that return JSON responses from Devin connector actions.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
