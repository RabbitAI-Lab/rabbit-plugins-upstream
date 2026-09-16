## Description:

This skill helps agents handle Sendlane requests through the OOMOL connector, including reading, creating, updating, and deleting Sendlane data instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Sendlane through an OOMOL-connected account, including listing campaigns and managing contact lists, tags, and custom fields. The skill is intended for agent-assisted Sendlane tasks that should use the OOMOL connector instead of direct API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes mutable remote installer scripts executed directly in a shell.

Mitigation: Review the installer before use and prefer a safer pinned or signed installation method when available.

Risk: Write and destructive Sendlane actions can change or delete contact-list and tag data.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sendlane)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Sendlane homepage](https://www.sendlane.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
