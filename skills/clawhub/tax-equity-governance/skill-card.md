## Description: <br>
股权与公司治理涉税专业助手，支持股权转让、家族股权架构、国企混改、VIE/红筹架构和股权架构税负优化场景的问答、测算、风险预警与自查报告生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, legal, and governance practitioners use this skill to triage equity-transfer and company-governance tax questions, run structured self-checks, compare common ownership structures, and produce practical compliance guidance for review by qualified professionals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, self-check inputs, or metrics may be sent to the cloud service at mcp.aitaxs.top. <br>
Mitigation: Avoid submitting confidential taxpayer, transaction, or identity data unless the service is approved for that data; redact sensitive facts before use. <br>
Risk: The skill can register and store local service credentials for cloud-backed MCP calls. <br>
Mitigation: Review the local client configuration before use, protect the credential file, and rotate or remove credentials if the environment is shared or no longer trusted. <br>
Risk: Client setup and matrix installation paths can modify local agent configuration or install related skills. <br>
Mitigation: Use dry-run or review mode first, confirm target directories and package checksums, and install only the related skills needed for the workflow. <br>
Risk: Tax guidance may depend on current law, local tax authority practice, and case-specific facts. <br>
Mitigation: Treat outputs as decision support and confirm material conclusions with the relevant tax authority or a qualified tax professional before filing or transacting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Equity governance self-check web workflow](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Matrix package entry](artifact/matrix.json) <br>
- [Skill source manifest](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-like structured responses, with optional shell commands and configuration snippets for local MCP setup or matrix installation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for tax policy Q&A, risk checks, tax calculation, and knowledge-base metadata; includes offline fallback guidance and a browser self-check workflow.] <br>

## Skill Version(s): <br>
3.14.38 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
