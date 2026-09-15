## Description:

HotspotSystem (hotspotsystem.com). Use this skill for ANY HotspotSystem request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect HotspotSystem action schemas and run read actions for owners, customers, subscribers, locations, and location options through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote script execution for installing the oo CLI.

Mitigation: Review the setup path before installing and prefer a verified, signed, or package-manager installation of the oo CLI.

Risk: The connector can retrieve broad customer and subscriber records through a third-party connector.

Mitigation: Connect a least-privilege HotspotSystem account and review returned customer or subscriber data before sharing it.

## Reference(s):

- [HotspotSystem Skill Page](https://clawhub.ai/oomol/skills/oo-hotspotsystem)
- [HotspotSystem Homepage](https://www.hotspotsystem.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
