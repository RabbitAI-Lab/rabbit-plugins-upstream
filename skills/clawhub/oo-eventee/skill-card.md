## Description:

Eventee helps agents read Eventee event content, participants, registrations, groups, and session reviews through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when an agent needs to retrieve Eventee event data from a connected OOMOL account without calling the Eventee API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documentation recommends executing remote installer scripts directly in a shell.

Mitigation: Install the oo CLI through a verified package manager or downloaded installer with checksum or signature verification before using the skill.

Risk: Connector actions depend on an authenticated OOMOL account and an active Eventee connection.

Mitigation: Run Eventee actions only after the CLI is signed in and the Eventee connection is configured; handle authentication, scope, expiry, and billing errors before retrying.

## Reference(s):

- [ClawHub Eventee Skill](https://clawhub.ai/oomol/skills/oo-eventee)
- [Eventee homepage](https://eventee.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Eventee connector schemas before running read-only actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
