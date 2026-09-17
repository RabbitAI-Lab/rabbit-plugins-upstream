## Description:

This skill helps agents search and read Sling workplace scheduling data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve Sling sessions, shifts, users, groups, tasks, calendar events, and coworker details through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security verdict is suspicious because fallback setup can execute a remote CLI installer directly.

Mitigation: Install the oo CLI through a reviewed, version-pinned, or checksum-verified method before using the skill.

Risk: Sling access depends on OOMOL as an intermediary for credentials and connector execution.

Mitigation: Install only when the user is comfortable with OOMOL-mediated Sling access and the account connection process.

Risk: Future connector actions could change or delete Sling data.

Mitigation: Require explicit user confirmation before running any action tagged write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-sling)
- [Sling Homepage](https://getsling.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL oo CLI connector calls and returns Sling connector JSON responses when actions run.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
