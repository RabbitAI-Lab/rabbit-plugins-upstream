## Description:

vmware-storage helps agents manage VMware vSphere storage by browsing datastores, finding deployable images, configuring iSCSI adapters and targets, and checking vSAN health and capacity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure operators and VMware administrators use this skill to inspect datastore contents, find deployable image files, manage iSCSI storage targets, and review vSAN health and capacity from an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can disable TLS certificate verification while using privileged VMware infrastructure credentials.

Mitigation: Use verify_ssl: true with a trusted CA, avoid administrator or root accounts, and use a least-privileged VMware service account.

Risk: Persistent .env passwords may expose infrastructure credentials if local files are readable.

Mitigation: Prefer a secret manager or process-injected environment variables, keep .env permissions restricted to owner read/write, and avoid persistent plaintext passwords.

Risk: iSCSI changes, especially target removal, can disrupt LUN access and affected workloads.

Mitigation: Require dry-run previews and explicit approval before iSCSI changes, verify targets and reachability first, and use audit and policy gates for production.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-storage)
- [VMware Storage project homepage](https://github.com/vmware-skills/VMware-Storage)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [VMware Storage Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with CLI commands and structured VMware storage result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include dry-run previews, datastore and vSAN summaries, and operator guidance for approval-gated storage changes.]

## Skill Version(s):

1.9.1 (source: server release metadata and install examples)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
