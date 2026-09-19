## Description:

Listen Notes (listennotes.com). Use this skill for ANY Listen Notes request - searching and reading data. Whenever a task involves Listen Notes, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search and read Listen Notes podcast and episode data through their OOMOL-connected Listen Notes account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that could execute code on the user's machine.

Mitigation: Install the oo CLI through a verified package manager or versioned release, or validate the installer checksum or signature before running it.

Risk: Connector calls depend on a signed-in OOMOL account and an active Listen Notes connection.

Mitigation: Run authentication or connection setup only after a command fails with the matching auth or connection error, then retry the intended read action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-listennotes)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Listen Notes Homepage](https://www.listennotes.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Listen Notes Icon](https://static.oomol.com/logo/third-party/Listen%20Notes.svg)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to inspect live action schemas before running Listen Notes connector actions.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
