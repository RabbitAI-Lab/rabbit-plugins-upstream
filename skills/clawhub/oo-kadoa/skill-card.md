## Description:

Kadoa helps agents search, read, inspect, and export Kadoa workflow data through the OOMOL `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators with an OOMOL-connected Kadoa account use this skill to inspect connector schemas, list workflows, retrieve workflow configuration and extracted records, and export matching workflow data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute downloaded scripts.

Mitigation: Review installation commands before use and prefer a pinned, signed, or checksum-verified oo CLI release path.

Risk: Exported Kadoa workflow data may contain sensitive records and can be delivered through temporary signed download URLs.

Mitigation: Limit exports to the needed records, share signed URLs only with authorized users, and store downloaded data according to the organization's data-handling policy.

## Reference(s):

- [ClawHub Kadoa Skill](https://clawhub.ai/oomol/skills/oo-kadoa)
- [Kadoa Homepage](https://www.kadoa.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Text]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return temporary signed download URLs for exported workflow data.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
