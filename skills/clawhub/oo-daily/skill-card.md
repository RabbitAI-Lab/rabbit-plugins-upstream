## Description:

Daily (daily.co) skill for reading, creating, updating, and deleting Daily rooms, meeting tokens, and domain configuration through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Daily video infrastructure from an agent through an OOMOL-connected account. It supports room lifecycle operations, meeting token creation, domain configuration lookup, and setup guidance when authentication, connection, or billing errors occur.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup guidance can execute mutable remote installer scripts directly in a shell.

Mitigation: Prefer a verified package or separately downloaded, inspected, version-pinned installer before installing the oo CLI.

Risk: Daily write and destructive actions can create, update, or delete remote resources.

Mitigation: Confirm the exact payload, target, and expected effect with the user before allowing write or delete actions to run.

## Reference(s):

- [Daily homepage](https://www.daily.co/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI commands, action schema inspection steps, JSON request payload guidance, and user-confirmation prompts for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
