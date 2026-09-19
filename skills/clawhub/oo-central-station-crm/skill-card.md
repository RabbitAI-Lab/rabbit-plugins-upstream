## Description:

CentralStationCRM support for reading, creating, updating, and deleting CRM data through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to manage CentralStationCRM companies, people, deals, and current-user data through the oo CLI. It supports read, list, search, create, update, and delete workflows, with confirmation expected for write and destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an internet-downloaded installer run directly in a shell.

Mitigation: Review the installer source first and prefer an official package manager, pinned release, or checksum/signature-verified install.

Risk: CRM create, update, and delete actions can change or remove business records.

Mitigation: Approve these actions only after checking the exact target, payload, and expected effect.

## Reference(s):

- [CentralStationCRM Skill Page](https://clawhub.ai/oomol/skills/oo-central-station-crm)
- [CentralStationCRM homepage](https://centralstationcrm.de)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads and expects explicit confirmation before write or destructive CRM changes.]

## Skill Version(s):

1.0.2 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
