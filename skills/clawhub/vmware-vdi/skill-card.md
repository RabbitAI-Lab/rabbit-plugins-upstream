## Description: <br>
VMware VDI helps agents operate VMware/Omnissa Horizon VDI through a Connection Server, including pool, farm, published app, session, machine, entitlement, event, health, statistics, and instant-clone image operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, IT administrators, and help-desk operators use this skill to inspect and manage Horizon VDI broker-layer resources through CLI or MCP workflows. Typical tasks include checking health, listing sessions and machines, managing entitlements, logging off or resetting sessions and desktops, and pushing instant-clone images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact VDI administration actions can log off users, reset or remove desktops, disable pools, cancel tasks, or push images across a pool. <br>
Mitigation: Use Horizon RBAC with read-only roles for monitoring, separate targets for write access, and review dry-run previews before approving write actions. <br>
Risk: The local b64: password storage described by the artifact is obfuscation, not strong secret protection. <br>
Mitigation: Inject VMWARE_VDI_<TARGET>_PASSWORD from an approved secret manager or protected environment variable for sensitive environments. <br>
Risk: Image push operations can affect every desktop in a pool and may disrupt active users. <br>
Mitigation: Check affected-desktop and in-session-user counts in the preview, warn users when needed, and proceed only after confirming the blast radius. <br>
Risk: Disabling TLS verification can expose Horizon credentials and administrative operations to interception. <br>
Mitigation: Keep TLS verification enabled for production targets and reserve verify_ssl: false for controlled self-signed lab environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-vdi) <br>
- [Capabilities](artifact/references/capabilities.md) <br>
- [CLI Reference](artifact/references/cli-reference.md) <br>
- [Setup Guide](artifact/references/setup-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, configuration snippets, and structured MCP tool output descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent output may include dry-run previews, paginated list summaries, task status, and operational guidance for Horizon VDI actions.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
