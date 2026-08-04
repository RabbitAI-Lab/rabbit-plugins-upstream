## Description: <br>
环保税与碳排放合规专项助手，帮助用户围绕环境保护税、污染物识别与监测核算、减排减免、按季申报、全国碳市场配额清缴、CCER/配额交易增值税处理、碳排放数据质量和整改闭环开展结构化自检、计算跟踪和合规问答。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance practitioners use this skill to ask Chinese environmental tax and carbon-compliance questions, run structured self-checks, calculate or track environmental-tax and carbon-quota items, and produce practical guidance for follow-up review. It is especially oriented to organizations with taxable pollutant emissions or national carbon-market obligations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is broader and more persistent than an environmental-tax-only description suggests. <br>
Mitigation: Review the installed package, expected tax-policy scope, remote MCP endpoint, and local state behavior before enabling it in a production agent. <br>
Risk: Company facts or tax scenarios may be sent to the remote MCP service or fallback search providers. <br>
Mitigation: Avoid entering sensitive company, client, or transaction details unless the organization has approved those remote services; redact or generalize prompts when possible. <br>
Risk: The client may leave MCP configuration and local state under user-level config locations, including ~/.tax-policy-client. <br>
Mitigation: On uninstall, inspect and remove related MCP client entries and local state/cache files that are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-environmental) <br>
- [Environmental tax and carbon compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_environmental.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON-like tool responses, Python scripts, MCP configuration snippets, and web workflow output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP calls, a local stdio proxy, local configuration/state under the user's home directory, fallback web search, and offline reference workflows.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
