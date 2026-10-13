## Description:

Helps agents inspect VMware datastores, iSCSI storage, vSAN health and capacity, and Fibre Channel paths, with guarded iSCSI changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure administrators and engineers use this skill to inspect VMware storage, diagnose datastore and path issues, and plan or approve iSCSI changes on vCenter or ESXi targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An iSCSI change can interrupt access to storage and dependent workloads.

Mitigation: Review the affected hosts, devices, and datastores in the change preview, and require explicit approval before applying a write.

Risk: vCenter credentials can expose production infrastructure if mishandled.

Mitigation: Use a least-privilege service account and a secret manager where available; avoid plaintext production or root passwords.

Risk: Insecure TLS or skipped authentication checks can leave a target unverified.

Mitigation: Keep TLS certificate verification enabled and do not treat --skip-auth as proof of authentication.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-storage)
- [Project homepage (skill metadata)](https://github.com/vmware-skills/VMware-Storage)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Agent guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON results]

**Output Format:** [Markdown guidance with command examples and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results include storage status and capacity; write previews describe the affected storage before confirmation.]

## Skill Version(s):

1.12.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
