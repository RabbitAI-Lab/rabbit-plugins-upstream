## Description: <br>
各类型拟上市与上市公司全生命周期财税顾问与内控框架专项助手，覆盖上市路径论证、上市前财税规范、内控框架设计、股改涉税、再融资、并购重组、分拆上市、境外架构、持续督导和股权激励等场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, company finance and compliance teams, directors' office staff, CFOs, controllers, and professional advisers use this skill to structure questions and receive tax, internal-control, listing-path, restructuring, disclosure, and remediation guidance for Chinese listed or pre-listing company scenarios. <br>

### Deployment Geography for Use: <br>
China, with cross-border considerations for H-share, red-chip, VIE, and offshore listing structures. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, listing plans, transaction structures, shareholder details, or compliance scenarios may be sent to remote services. <br>
Mitigation: Use only approved, non-confidential or appropriately authorized data, and confirm the organization's data-sharing approval before using cloud-backed policy, risk, or calculation tools. <br>
Risk: Setup behavior can edit local MCP client configuration when autosetup is intentionally enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP unset unless configuration changes are intended; review proposed MCP client changes and backups before enabling setup. <br>
Risk: Tax and listing guidance may be incomplete or outdated for a specific company, filing, exchange, or regulator interaction. <br>
Mitigation: Treat outputs as advisory drafting and self-check support; have qualified tax, accounting, legal, and sponsor professionals validate conclusions before filings or transactions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-listed-advisory) <br>
- [上市业务财税合规自检与专项风险扫描](https://mcp.aitaxs.top/web/topic_workflow_listed_advisory.html) <br>
- [财税合规自检门户](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown responses with structured checklists, risk summaries, remediation plans, policy references, self-check prompts, and optional JSON/tool outputs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for policy answers, risk checks, tax calculations, and knowledge-base listings; includes offline workflow scripts for limited fallback guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
