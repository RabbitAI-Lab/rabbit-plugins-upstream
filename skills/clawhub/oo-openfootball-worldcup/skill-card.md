## Description:

OpenFootball World Cup lets agents query World Cup groups, matches, qualification playoffs, squads, stadiums, and teams from the public OpenFootball JSON dataset through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to inspect action schemas and retrieve public OpenFootball World Cup data through the OOMOL connector. It supports read-oriented lookup workflows for World Cup groups, matches, qualification playoffs, squads, stadiums, and teams.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded code.

Mitigation: Prefer a version-pinned, signed, or checksum-verified installation path from the publisher before installing the oo CLI.

Risk: The World Cup data comes from a public community dataset and is not a real-time or official results source.

Mitigation: Use the connector for lookup and analysis, and verify time-sensitive match results against an official source before relying on them.

Risk: Future connector schemas could expose actions beyond the listed read-only operations.

Mitigation: Inspect the live action schema before execution and get explicit user approval before running any write or destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openfootball-worldcup)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OpenFootball World Cup dataset](https://github.com/openfootball/worldcup.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data payload and meta.executionId when run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
