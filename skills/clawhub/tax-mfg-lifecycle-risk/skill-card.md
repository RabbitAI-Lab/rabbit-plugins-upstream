## Description: <br>
Manufacturing tax lifecycle risk guidance for establishment, operations, R&D deductions, accelerated depreciation, restructuring, expansion, liquidation, and structured compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users use this skill to identify manufacturing lifecycle tax risks and generate structured self-check guidance, checklists, and remediation-oriented prompts. It supports Chinese manufacturing scenarios such as VAT input classification, export refund documentation, R&D super-deduction support records, restructuring tax treatment, environmental and resource taxes, and liquidation tax cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check prompts may be transmitted to the mcp.aitaxs.top cloud service and locally logged. <br>
Mitigation: Use the skill only when cloud processing is acceptable, avoid confidential company identifiers or detailed financial facts, and review local records under ~/.tax-policy-client after use. <br>
Risk: The skill may persist credentials locally for MCP service access. <br>
Mitigation: Inspect and manage the local ~/.tax-policy-client configuration and remove stored credentials when they are no longer needed. <br>
Risk: Running config/init_agent.py directly can modify MCP client configuration. <br>
Mitigation: Do not run config/init_agent.py unless MCP configuration changes are intended; review any proposed client configuration changes before accepting them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Manufacturing lifecycle self-check page](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, policy references, prompts, and optional configuration or shell command snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route tax questions and self-check requests to a cloud MCP service and provide offline fallback guidance when service access is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
