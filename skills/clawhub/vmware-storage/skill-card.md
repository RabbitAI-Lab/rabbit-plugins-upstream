## Description: <br>
Use this skill to manage VMware storage tasks such as datastore browsing, deployable image scans, iSCSI target configuration, and vSAN health and capacity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, infrastructure engineers, and VMware administrators use this skill to inspect datastores, find deployable images, configure iSCSI targets, and review vSAN health and capacity from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change VMware storage configuration, including iSCSI targets, which may affect host or datastore availability. <br>
Mitigation: Restrict use to VMware administrators, use a dedicated least-privilege vSphere account, review policy gates, and run dry-run before iSCSI changes. <br>
Risk: Credentials and local audit logs may contain sensitive operational data. <br>
Mitigation: Keep ~/.vmware-storage/.env at 600 permissions or inject secrets from a manager, and treat ~/.vmware/audit.db as sensitive operational data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage) <br>
- [Project homepage](https://github.com/zw008/VMware-Storage) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [VMware Storage Capabilities](references/capabilities.md) <br>
- [Operating vmware-storage with a local / small model](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI/MCP workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes local VMware storage administration guidance; write operations should use dry-run, policy gates, and audit logging.] <br>

## Skill Version(s): <br>
1.8.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
