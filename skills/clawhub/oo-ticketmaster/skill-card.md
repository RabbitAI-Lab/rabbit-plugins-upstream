## Description:

Ticketmaster helps agents search and retrieve Ticketmaster events, venues, attractions, classifications, event images, suggestions, section maps, and season-ticketing command results through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for Ticketmaster search and lookup workflows, including events, venues, attractions, classifications, event images, suggestions, section maps, and season-ticketing command execution through connected OOMOL credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad season-ticketing command may change Ticketmaster-related account, order, ticket, or season-ticketing state.

Mitigation: Require explicit user confirmation of the exact action, target, payload, and expected effect before running execute_season_ticketing_command or any similar state-changing action.

Risk: Remote installer commands can execute code from a fetched script during first-time setup.

Mitigation: Prefer a verified oo CLI installation method and review the installer source before running pipe-to-shell commands.

Risk: The skill depends on OOMOL and the Ticketmaster connector for credentialed access.

Mitigation: Install and use the skill only when the user trusts OOMOL and the Ticketmaster connector, and avoid handling raw credentials directly.

## Reference(s):

- [ClawHub Ticketmaster Skill](https://clawhub.ai/oomol/skills/oo-ticketmaster)
- [Ticketmaster Homepage](https://www.ticketmaster.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
