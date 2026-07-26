## Description: <br>
高企认定与研发费用加计扣除全链条财税合规助手，帮助企业测算高企认定指标、归集和分摊研发费用、生成辅助账和多口径报表，并提示资格维持与稽查风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and R&D compliance teams use this skill to evaluate Chinese high-tech enterprise qualification and R&D super-deduction scenarios, prepare self-checks, and generate working guidance for evidence-chain, allocation, ledger, and reporting workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security summary flags cloud processing of tax inputs by mcp.aitaxs.top. <br>
Mitigation: Review before installing when handling confidential tax, payroll, R&D, employee, or financial records, and use only if cloud processing by mcp.aitaxs.top is acceptable. <br>
Risk: The authoritative security summary flags local credential and log storage under ~/.tax-policy-client and browser localStorage credentials for the web page. <br>
Mitigation: Limit use on shared machines, protect the local user profile, and review local storage policies before entering sensitive business data. <br>
Risk: The authoritative security guidance flags possible installation or replacement of additional skills through the matrix installer. <br>
Mitigation: Avoid the matrix installer unless package provenance is verified and changes under ~/.skills are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [Interactive high-tech tax compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax policy knowledge service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with optional JSON, CSV, shell command, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy Q&A, risk checks, calculations, and knowledge-base metadata; includes local offline fallback guidance and a browser workflow.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
