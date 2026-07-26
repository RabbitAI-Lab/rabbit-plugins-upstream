## Description: <br>
Governed Nutanix Prism Central v4 operations for estate health, inventory, VM lifecycle, storage, networking, data protection, alerts, LCM upgrades, capacity forecasting, and RCA through a 51-tool MCP and CLI surface. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to inspect, diagnose, and operate Nutanix Prism Central v4 estates from an agent workflow. It is intended for Nutanix environments only and includes both read-only diagnostics and write-capable maintenance workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes powerful Prism Central write actions without an in-skill approval or read-only policy gate. <br>
Mitigation: Install it with a deliberately scoped Prism Central account; start with a read-only Viewer role and use write-capable credentials only for controlled maintenance contexts. <br>
Risk: High-risk operations can delete, migrate, restore, fail over, or update infrastructure resources. <br>
Mitigation: Use the documented dry-run previews, CLI double confirmation, ETag handling, and audit annotations before running destructive or state-changing actions. <br>
Risk: Secrets and local audit or undo databases may contain sensitive operational information. <br>
Mitigation: Protect NUTANIX_AIOPS_MASTER_PASSWORD as a secret, avoid the legacy plaintext password fallback, and review handling of audit.db and undo.db under the Nutanix AIops home directory. <br>
Risk: Some behavior is validated against mocked v4 REST responses and still needs live verification for production confidence. <br>
Mitigation: Run nutanix-aiops doctor and perform live validation in a Nutanix Community Edition or controlled Prism Central environment before relying on LCM update, PD failover, or ESXi VM listing paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/nutanix-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/Nutanix-AIops) <br>
- [Capabilities reference](references/capabilities.md) <br>
- [CLI reference](references/cli-reference.md) <br>
- [Setup and security guide](references/setup-guide.md) <br>
- [Agent guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and MCP tool outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces operational observations, RCA summaries, dry-run previews, task references, and configuration guidance for Prism Central workflows.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
