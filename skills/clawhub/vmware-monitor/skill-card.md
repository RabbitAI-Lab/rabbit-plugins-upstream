## Description:

Provides read-only monitoring, health summaries, inventory queries, and incident investigation for VMware vCenter and ESXi environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure operators use the skill to review VMware inventory, health, alarms, events, and selected logs, and to investigate issues without making vSphere changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports TLS troubleshooting guidance that could disable certificate verification and expose credentials or data.

Mitigation: Keep TLS verification enabled in production and use CA-signed certificates. Restrict disabled verification to isolated labs with self-signed certificates, as the setup guide describes.

Risk: The security review reports an installer version that is not pinned.

Mitigation: Install a version-pinned release, such as `uv tool install vmware-monitor==2.6.0`, and review the source before deployment.

Risk: The security review reports commands or controls that extend beyond the stated read-only monitoring scope.

Mitigation: Review commands before running them and use a dedicated vCenter account with only the required read privileges.

Risk: The scan covered only 7 of 8 components and one static analysis was degraded, so its results are incomplete.

Mitigation: Treat the security result as incomplete and obtain a complete scan and review before deployment.

## Reference(s):

- [VMware Monitor project homepage](https://github.com/vmware-skills/VMware-Monitor)
- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-monitor)
- [Setup and security guide](artifact/references/setup-guide.md)
- [Capabilities reference](artifact/references/capabilities.md)
- [Agent guardrails](artifact/references/agent-guardrails.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Readable monitoring summaries and structured query results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include sensitive infrastructure inventory, event, and log details.]

## Skill Version(s):

2.6.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
