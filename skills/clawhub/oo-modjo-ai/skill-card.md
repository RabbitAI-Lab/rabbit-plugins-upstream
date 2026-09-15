## Description:

Modjo AI connector for searching and reading Modjo account, call, contact, deal, team, user, tag, and topic data through OOMOL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Modjo AI data through an OOMOL-connected account, including calls, transcripts, notes, contacts, deals, teams, users, tags, topics, summaries, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote scripts executed directly in a shell.

Mitigation: Review the setup path before installing, prefer safer official installation methods, inspect downloaded installers, verify signatures or checksums when available, and avoid running one-line installers from an elevated shell.

Risk: Connector use can expose sensitive Modjo AI business, CRM, and call information to the agent session.

Mitigation: Run only the read actions needed for the user's task, inspect live action schemas before sending payloads, and avoid requesting broader records than necessary.

## Reference(s):

- [Modjo AI homepage](https://www.modjo.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON data with execution metadata when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
