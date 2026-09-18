## Description:

AroFlo (aroflo.com) supports AroFlo searching and read-only data retrieval through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect AroFlo clients, tasks, users, and public API health through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes unverified remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use an official installer path that can be inspected or verified first; avoid allowing an agent to run curl|bash or irm|iex automatically.

Risk: Connector actions depend on an authenticated OOMOL account and an active AroFlo connection.

Mitigation: Run setup or connection steps only after an auth or connection failure, and connect AroFlo intentionally before using read actions.

Risk: Action payloads may become incorrect if connector schemas change.

Mitigation: Inspect the live action schema before constructing a payload for any connector run.

## Reference(s):

- [ClawHub AroFlo Skill Page](https://clawhub.ai/oomol/skills/oo-aroflo)
- [AroFlo Homepage](https://aroflo.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only AroFlo connector actions; live action schemas should be checked before building payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
