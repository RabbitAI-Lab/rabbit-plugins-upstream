## Description: <br>
Provides tax and governance guidance for equity transfers, family holding structures, state-owned enterprise mixed-ownership reform, VIE/red-chip structures, tax-burden comparison, risk self-checks, calculations, and response planning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and business teams use this skill to assess equity transaction and governance tax risks, compare structures, calculate indicative tax exposure, and produce self-check or remediation guidance. It is intended as decision support and should be verified against current official policy and qualified professional advice for material transactions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, self-check data, and fallback searches may be processed by cloud or public search services. <br>
Mitigation: Avoid confidential deal details, personal identifiers, and non-public restructuring facts unless the provider and data terms have been reviewed. <br>
Risk: API keys, identifiers, logs, and cached data may be stored locally. <br>
Mitigation: Review and manage ~/.tax-policy-client and browser localStorage before and after use, especially on shared systems. <br>
Risk: Optional auto-setup can change local MCP client configuration. <br>
Mitigation: Leave TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended, and review any generated MCP client entries and backups. <br>
Risk: Tax conclusions can vary by jurisdiction, time, facts, and local tax authority practice. <br>
Mitigation: Verify material guidance against official tax authority sources or a qualified tax professional before filing, restructuring, or executing a transaction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Equity governance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown or structured text with calculations, checklists, policy references, and configuration guidance when MCP setup is relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services or local fallback workflows; outputs are advisory and require review for current jurisdiction, facts, and official policy.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
