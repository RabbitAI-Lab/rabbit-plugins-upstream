## Description: <br>
企业全业务生命周期合同模板库与全生命周期合规评审指引，支持合同类型模板查看、合同生成、条款审核、涉税风险防控和评审报告生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business, legal, compliance, finance, and tax users can use this skill to find contract templates, draft contract language, review clauses for tax and compliance risks, and produce structured review reports. It is especially oriented toward Chinese-language contract lifecycle workflows and tax-risk screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports cloud processing by mcp.aitaxs.top, local API-key storage, plaintext local logs, and possible MCP client configuration changes when setup is explicitly enabled. <br>
Mitigation: Review the skill before deployment, avoid submitting confidential contracts or regulated business facts unless external processing and local logging are acceptable, and enable setup only after reviewing the MCP configuration changes. <br>
Risk: The skill provides legal, tax, and compliance guidance that may be incomplete, outdated, or unsuitable for a specific jurisdiction or transaction. <br>
Mitigation: Treat generated templates, risk findings, and reports as drafting and review aids, then have qualified legal or tax professionals validate conclusions before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Contract compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese-language Markdown, structured text, JSON-like review data, Python workflow code, and MCP client configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce contract templates, tax-risk findings, review checklists, remediation guidance, and review reports; cloud-backed MCP behavior can supplement local fallback workflows.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
