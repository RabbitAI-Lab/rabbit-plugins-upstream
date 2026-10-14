## Description:

Helps agents inspect VMware datastores, iSCSI storage, vSAN health and capacity, and Fibre Channel paths, with gated iSCSI configuration changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure administrators and engineers use this skill to inspect VMware storage, diagnose datastore and path issues, check vSAN health, and preview or carry out approved iSCSI changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to vCenter or ESXi exposes sensitive storage inventory and permits storage configuration changes.

Mitigation: Use least-privilege VMware service accounts and limit deployment to environments where this access is authorized.

Risk: iSCSI writes or rescans can affect production storage availability.

Mitigation: Review the previewed impact and obtain human approval before executing iSCSI changes or rescans in production.

Risk: Stored passwords or disabled certificate verification can expose infrastructure credentials.

Mitigation: Prefer a secret manager over a persistent .env file and keep SSL verification enabled.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-Storage)
- [Setup guide](references/setup-guide.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Natural-language reports with optional commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports storage inventory and diagnostics; changes require user approval.]

## Skill Version(s):

2.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
