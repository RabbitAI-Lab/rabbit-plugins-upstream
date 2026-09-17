## Description:

OpenFootball World Cup helps agents inspect schemas and query public World Cup groups, matches, teams, squads, stadiums, and qualification playoff data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search and read public OpenFootball World Cup JSON data through the OOMOL connector without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running remote installer scripts directly in a shell.

Mitigation: Prefer a pinned, signed, or checksum-verified oo CLI installation method and avoid installing in sensitive or privileged environments.

Risk: OpenFootball World Cup data comes from a public community dataset and is not a real-time or official results source.

Mitigation: Verify time-sensitive or official World Cup results against an authoritative source before relying on them.

## Reference(s):

- [OpenFootball World Cup dataset](https://github.com/openfootball/worldcup.json)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
