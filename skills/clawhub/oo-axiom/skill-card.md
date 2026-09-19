## Description:

Axiom (axiom.co). Use this skill for ANY Axiom request — reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Axiom datasets and run Axiom Processing Language queries through an OOMOL-connected account. It supports read, write, and destructive Axiom actions with explicit confirmation guidance for state-changing operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes first-time setup guidance that pipes a remote installer directly into a shell.

Mitigation: Install the oo CLI through a trusted, verified method and do not let an agent run the remote installer automatically.

Risk: The skill can create and delete Axiom datasets.

Mitigation: Confirm the exact target, payload, and intended effect before allowing write or destructive actions.

## Reference(s):

- [ClawHub Axiom Skill](https://clawhub.ai/oomol/skills/oo-axiom)
- [Axiom Homepage](https://axiom.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Axiom Connection Settings](https://console.oomol.com/app-connections?provider=axiom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are expected to use the oo CLI and JSON payloads that match the live connector schema.]

## Skill Version(s):

1.0.2 (source: evidence release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
