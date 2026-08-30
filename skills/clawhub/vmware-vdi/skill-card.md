## Description:

Operates VMware/Omnissa Horizon VDI environments through the Connection Server API, covering desktop pools, RDS farms, published apps, sessions, machines, entitlements, events, health, statistics, and instant-clone image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators, help-desk operators, and automation engineers use this skill to inspect and administer VMware/Omnissa Horizon VDI broker-layer resources, including user sessions, desktop machines, pools, farms, entitlements, health, events, and image-push tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Horizon write operations can affect production users, including logoff, reset, remove, entitlement removal, image push, and task cancellation.

Mitigation: Install only for users authorized to administer Horizon VDI, prefer read-only Horizon roles unless writes are required, and use dry-run previews and confirmation for production-impacting actions.

Risk: Credentials for the configured Connection Server can expose administrative access if local password storage is not protected.

Mitigation: Protect the local password file, keep restrictive file permissions, or inject VMWARE_VDI_<TARGET>_PASSWORD from a secret manager.

Risk: Disabling TLS verification can weaken connection security outside lab environments.

Mitigation: Keep TLS verification enabled for normal use and reserve verify_ssl: false for controlled self-signed lab targets only.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vdi)
- [Capabilities](references/capabilities.md)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and MCP or CLI configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run recommendations, operational cautions, and structured MCP tool response summaries.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
