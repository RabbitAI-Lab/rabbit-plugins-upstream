## Description:

LINE (line.me) helps agents read, create, and update LINE data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a LINE Official Account through an OOMOL-connected account, including retrieving bot or user profile information and sending broadcast, multicast, or push text messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path asks users to execute remote installer scripts directly without verification.

Mitigation: Install the oo CLI from a versioned, trusted release with checksum or signature verification before using the skill.

Risk: LINE broadcast, multicast, and push-message actions can send messages from the connected account.

Mitigation: Confirm the exact recipient set, payload, and effect with the user before allowing any write action to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-line)
- [LINE homepage](https://line.me)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce oo CLI commands that call live LINE connector schemas and actions.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
