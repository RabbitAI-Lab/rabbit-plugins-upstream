## Description:

Braze lets an agent read Braze campaign and Canvas information through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and teams with an OOMOL-connected Braze account use this skill to list campaigns and Canvases and retrieve campaign or Canvas metadata and message details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup fallback includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run the installer automatically; install the CLI only through a trusted, verified path.

Risk: The skill's scope language is broader than the listed read-only Braze actions.

Mitigation: Limit automatic execution to the listed read operations and confirm any Braze action outside that list before running it.

## Reference(s):

- [ClawHub Braze Skill](https://clawhub.ai/oomol/skills/oo-braze)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Braze Homepage](https://www.braze.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented Braze campaign and Canvas data; connector responses include data and metadata such as execution IDs.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
