## Description:

Sherpa helps agents retrieve personalized travel restrictions, document requirements, and concise trip requirement summaries through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to check Sherpa-powered travel restrictions, visa, and document requirements for itineraries. It is intended for read-only trip details and Markdown trip summaries through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a verified, pinned, or manually reviewed method, and require explicit user approval before any agent runs installer commands.

Risk: The skill depends on external account state, including OOMOL authentication, Sherpa connection status, and billing availability.

Mitigation: Treat authentication, connection, scope, expiration, and billing failures as setup or account-state issues and guide the user to resolve them before retrying.

## Reference(s):

- [Sherpa homepage](https://www.joinsherpa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sherpa)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented actions are read-only; successful use depends on an installed oo CLI, OOMOL authentication, a connected Sherpa account, and billing availability.]

## Skill Version(s):

1.0.3 (source: server evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
