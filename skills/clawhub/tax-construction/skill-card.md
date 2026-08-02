## Description: <br>
Tax Construction helps agents provide Chinese construction-industry tax compliance guidance for VAT prepayment, simplified taxation, invoices, affiliated operations, payroll, stamp tax, environmental tax, and cross-region filing scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, and compliance teams use this skill to ask construction-project tax questions, perform lightweight compliance self-checks, and structure risk remediation guidance for Chinese construction business scenarios. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and risk scenarios may be processed by the publisher's remote service. <br>
Mitigation: Do not enter raw taxpayer identifiers, payroll details, bank or account data, or confidential project documents unless the publisher's privacy and retention practices have been reviewed. <br>
Risk: API credentials, cache data, and logs may be stored locally. <br>
Mitigation: Restrict local file permissions, review the local data directory before deployment, and remove stored credentials, cache files, and logs when the skill is decommissioned. <br>
Risk: Optional setup code can modify agent MCP configuration when explicitly enabled. <br>
Mitigation: Review config/init_agent.py before running it directly or enabling TAX_ENABLE_AUTOSETUP, and require administrator approval for managed environments. <br>
Risk: The authoritative scan verdict is suspicious because disclosure is incomplete for remote processing, credential storage, logging, and configuration changes. <br>
Mitigation: Treat the skill as needing administrative review before broad deployment, even though the scan found no individual risk findings. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Construction compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance, JSON-like tool responses, code snippets, and configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use the publisher's remote MCP service for policy questions, risk checks, tax calculations, and knowledge-base metadata; includes offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
