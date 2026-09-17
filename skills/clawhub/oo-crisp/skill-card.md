## Description:

Crisp lets an agent operate a connected Crisp account through the OOMOL oo CLI to retrieve website and conversation data and send confirmed operator messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support operators, and agents use this skill to inspect Crisp website and conversation data and send operator text messages from a connected OOMOL/Crisp account after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup asks the agent to execute remote installer scripts for the oo CLI.

Mitigation: Review the installer source or install the oo CLI from a trusted, versioned, or package-managed source before enabling the skill.

Risk: The skill can send operator text messages to Crisp conversations through the connected account.

Mitigation: Confirm the exact conversation target, message payload, and expected effect before allowing send_text_message.

Risk: The skill depends on an OOMOL-connected Crisp account and OOMOL-hosted setup flow.

Mitigation: Install only if OOMOL's hosting and connected-account handling are acceptable for the deployment, and revoke access when the connection is no longer needed.

## Reference(s):

- [ClawHub Crisp Skill](https://clawhub.ai/oomol/skills/oo-crisp)
- [Crisp Homepage](https://crisp.chat/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before JSON action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
