## Description:

Use this skill to search and read Drimify data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve individual Drimify app data collection records and list collections with optional app, session, and creation-time filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote installer commands for the oo CLI.

Mitigation: Review the CLI installation path before use, avoid running pipe-to-shell installers from an elevated shell, and prefer a verified or package-manager installation path.

Risk: Broad action-routing language could route future connector actions beyond the listed read actions.

Mitigation: Treat the current release as suitable for the listed read actions, and explicitly review and approve any future write or destructive connector action before use.

## Reference(s):

- [Drimify ClawHub skill page](https://clawhub.ai/oomol/skills/oo-drimify)
- [Drimify homepage](https://drimify.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects when run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
