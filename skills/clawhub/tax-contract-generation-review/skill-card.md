## Description: <br>
企业全业务生命周期合同模板库与全生命周期合规评审指引。支持全行业合同类型模板查看、合同生成、条款审核、涉税风险防控、评审报告一键生成等完整业务闭环。内置全行业合同涉税风险防控体系，覆盖劳动人事、买卖交易、租赁物业、服务合作、建设工程、金融投资、知识产权、数据合规、政府合同、生活服务等十大类别100+细分模板；合同涉税五大高风险条款自动识别（兼营/混合销售、价外费用、阴阳合同、关联交易、政采工程），多项风险指标（C01-C21）逐项检查与红黄绿风险分级；五维权合同审查框架（主体资格/权利义务/金额条款/期限条款/法律合规），自动风险定位+法律条文引用+条款修改建议+判例参考；合同全生命周期业务闭环（模板选择→对话引导填写→AI智能起草→条款建议→合同审核→评审报告→修改复核→合同签署→履约管理→合同归档），支持Word导出与版本管理。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise legal, compliance, finance, and tax teams use this skill to draft contract templates, review contract clauses for tax and legal compliance risks, and generate structured review reports with remediation guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-connected tax service behavior may send prompts, scenarios, metrics, and generated identifiers to mcp.aitaxs.top. <br>
Mitigation: Use only with data approved for that service; avoid confidential contract text, company identifiers, and regulated personal data unless enterprise review approves the data flow. <br>
Risk: Local logging and credential storage are called out by the security scan. <br>
Mitigation: Review local configuration, cache, and log locations before enterprise use, and rotate or remove stored API credentials if the skill is no longer used. <br>
Risk: Optional MCP client reconfiguration may alter local agent settings. <br>
Mitigation: Keep auto-setup disabled unless needed, review proposed client configuration changes first, and use dry-run behavior where available. <br>
Risk: Fallback behavior may query public search engines. <br>
Mitigation: Disable fallback or avoid sensitive prompts when cloud service health is uncertain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Hosted contract self-check page](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>
- [Cloud MCP tax policy service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and plain text guidance with contract drafts, clause review findings, risk ratings, remediation steps, and compliance report content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include links to a hosted self-check page and may rely on cloud MCP responses when enabled.] <br>

## Skill Version(s): <br>
3.15.6 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
