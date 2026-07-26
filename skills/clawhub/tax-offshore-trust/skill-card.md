## Description: <br>
Provides structured personal income tax compliance guidance and self-check workflows for offshore trusts, cross-border family wealth, foreign-income reporting, CFC, CRS, and anti-avoidance scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax-focused agents use this skill to reason through offshore trust personal income tax obligations, cross-border family wealth compliance, foreign-income reporting, CFC, CRS, and anti-avoidance checkpoints. It can return structured self-check guidance and point users to an interactive workflow for deeper scenario review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use only when that remote data flow is acceptable; avoid real names, account numbers, and detailed family or financial identifiers. <br>
Risk: The package can store API credentials and logs locally. <br>
Mitigation: Review the local data directory and credential handling before use on shared or managed machines. <br>
Risk: Matrix-install phrases can trigger broad installation of related tax skills. <br>
Mitigation: Use those phrases only when broad installation is intended. <br>
Risk: Autosetup can modify supported MCP client configuration files when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP unset unless configuration changes are desired, and review backups or diffs after enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Offshore trust workflow](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax policy MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>
- [Related tax policy skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related cross-border tax skill](https://skillhub.cn/skills/tax-crossborder) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Configuration] <br>
**Output Format:** [Markdown and plain text with links, checklists, prompts, and optional command or configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service and local fallback workflows; avoid sending sensitive identifiers unless the user accepts that data flow.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
