## Description:

Everhour lets agents read, create, and update Everhour data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to inspect Everhour action schemas, retrieve projects, tasks, users, timers, and time records, and perform confirmed time-entry or timer actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path may execute a remote installer directly in a shell.

Mitigation: Review the installer URL and prefer a trusted, verifiable release or package manager before installing the OOMOL oo CLI.

Risk: Write actions can create time records or start and stop timers in Everhour.

Mitigation: Confirm the exact payload and intended effect with the user before running any write action.

## Reference(s):

- [ClawHub Everhour skill page](https://clawhub.ai/oomol/skills/oo-everhour)
- [Everhour homepage](https://everhour.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions can be run directly; write actions require user confirmation of the exact payload and effect.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
