## Description:

Provides Dynatrace search and read access for monitored entities and problems through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to inspect Dynatrace monitored entities and list Dynatrace problem records through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer pipe commands for the OOMOL CLI.

Mitigation: Review and verify the installer from OOMOL before running it, or install the CLI through an approved internal process.

Risk: Dynatrace operational data is routed through OOMOL-managed connector infrastructure.

Mitigation: Confirm that using OOMOL for Dynatrace data access is approved for the environment before connecting the account.

Risk: Connector action inputs may change over time.

Mitigation: Inspect the live action schema before constructing and running each connector payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dynatrace)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Dynatrace homepage](https://www.dynatrace.com)
- [OOMOL Dynatrace connection](https://console.oomol.com/app-connections?provider=dynatrace)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-managed Dynatrace credentials and live connector schemas before action execution.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
