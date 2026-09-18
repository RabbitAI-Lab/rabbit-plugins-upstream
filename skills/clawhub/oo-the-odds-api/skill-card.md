## Description:

The Odds API (the-odds-api.com) skill helps agents search and read live sports odds, events, participants, market keys, and scores through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill when they need read-only access to The Odds API data, including sports, events, odds, markets, participants, and scores, without calling the API directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Install the oo CLI only from a trusted and verified source and version; avoid running pipe-to-shell commands automatically or from an elevated shell.

Risk: Authentication or connector setup may be triggered unnecessarily if setup steps are run before an actual command failure.

Mitigation: Run authentication or connection setup only after a command returns the matching auth or connection error.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-the-odds-api)
- [The Odds API Homepage](https://the-odds-api.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
