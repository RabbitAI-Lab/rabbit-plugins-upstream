## Description: <br>
新疆区域税收优惠与落地经营实操专题助手，帮助用户评估新疆困难地区两免三减半、喀什霍尔果斯五免、西部大开发15%及相关落地经营合规风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business tax, finance, and compliance users use this skill to compare Xinjiang regional corporate income-tax preferences, test eligibility assumptions, prepare operating checklists, and identify self-check risks before seeking professional confirmation. <br>

### Deployment Geography for Use: <br>
China, with focus on Xinjiang regional tax incentives. <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check indicators may be sent to mcp.aitaxs.top. <br>
Mitigation: Use only non-sensitive or redacted scenarios unless the publisher's data handling and retention practices are acceptable for the intended business use. <br>
Risk: API credentials and logs may persist locally. <br>
Mitigation: Protect the local client data directory and browser storage, and clear stored keys or logs before sharing a machine or workspace. <br>
Risk: Optional setup can modify AI client MCP configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled and review config/init_agent.py behavior before running setup that writes client configuration. <br>
Risk: Tax outputs are advisory and may be incomplete for filing-ready decisions. <br>
Mitigation: Confirm material conclusions with official sources, the主管 tax authority, or a qualified tax professional before filing or restructuring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-xinjiang-preferential) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Xinjiang preferential tax self-check page](https://mcp.aitaxs.top/web/topic_workflow_xinjiang_preferential.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown text with structured checklists, tax-risk self-check reports, and occasional configuration or command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP tax-policy service, persist local API credentials and logs, and fall back to local reference workflows when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
