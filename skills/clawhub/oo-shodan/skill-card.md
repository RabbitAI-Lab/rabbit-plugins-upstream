## Description:

Provides an agent-facing Shodan connector for searching hosts, reading host details, resolving DNS data, and checking Shodan account information through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query Shodan data from an agent workflow, including host searches, host details, DNS lookups, domain information, and API account status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include one-line remote installer commands.

Mitigation: Use official, version-pinned installation steps with verification instead of running remote install scripts automatically.

Risk: Shodan queries and identifiers are routed through OOMOL as an intermediary.

Mitigation: Install only when OOMOL is an intended intermediary, and avoid sending sensitive IPs, domains, hostnames, or organization names unless that routing is acceptable.

## Reference(s):

- [Shodan homepage](https://www.shodan.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-shodan)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented Shodan connector actions after checking live action schemas.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
