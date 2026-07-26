## Description: <br>
Manage Microsoft Intune and Entra ID device management through Microsoft Graph, including devices, policies, apps, reporting, enrollment, Conditional Access, and remote actions with confirmation tiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mattiacirillo](https://clawhub.ai/user/mattiacirillo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
IT administrators, MSP operators, and automation engineers use this skill to query, report on, and administer Microsoft Intune and Entra-managed devices, policies, apps, enrollment, Conditional Access, and related Microsoft Graph resources from an OpenClaw-compatible agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform tenant-admin Intune and Entra actions, including destructive device and policy changes. <br>
Mitigation: Install it only on trusted machines and agent accounts, grant only the Microsoft Graph permissions needed, and prefer read-only Graph permissions with INTUNE_READ_ONLY=true for reporting workflows. <br>
Risk: Device wipe, retire, policy, Conditional Access, group, app, and update-ring changes can have broad tenant impact. <br>
Mitigation: Review the skill's confirmations carefully before write operations; Tier 3 actions require the exact confirmed object name before execution. <br>
Risk: Microsoft Graph credentials and token cache access are sensitive. <br>
Mitigation: Protect the local user account and cache directory, keep client secrets out of logs and command output, and use the bundled token helper and Graph wrapper rather than ad hoc requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mattiacirillo/skills/openclaw-intune-skill) <br>
- [Kaffee & Code](https://kaffeeundcode.com) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>
- [Microsoft Graph Intune documentation](https://learn.microsoft.com/en-us/graph/api/resources/intune-graph-overview) <br>
- [README](README.md) <br>
- [Devices reference](references/devices.md) <br>
- [Policies reference](references/policies.md) <br>
- [Apps reference](references/apps.md) <br>
- [Platform reference](references/platform.md) <br>
- [Network and updates reference](references/network-updates.md) <br>
- [Reporting reference](references/reporting.md) <br>
- [Admin reference](references/admin.md) <br>
- [Workflows reference](references/workflows.md) <br>
- [Troubleshooting reference](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and tables with inline shell commands and JSON request bodies when changes are proposed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses required Intune environment variables and optional read-only/profile flags; the wrapper handles Microsoft Graph JSON responses internally while the agent summarizes results for the user.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
