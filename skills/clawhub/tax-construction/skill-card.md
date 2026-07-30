## Description: <br>
Tax Construction helps agents answer construction-industry tax compliance questions, run structured self-checks, identify risk signals, and draft practical remediation guidance for topics such as cross-region prepayment, invoice controls, affiliated contracting, bid-rigging exposure, and project tax reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, tax practitioners, and business users can use this skill to support construction tax compliance workflows, including policy Q&A, risk screening, self-check report drafting, and offline fallback guidance. The skill is informational and should not replace professional tax, audit, or legal review for filings or disputes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags remote service registration, persistent identifiers, local logging, and optional MCP/client configuration changes as insufficiently disclosed for sensitive tax workflows. <br>
Mitigation: Review the skill before installation, avoid entering raw ledgers, IDs, full tax numbers, confidential contracts, or company-identifying details, and enable auto-setup only when configuration changes are intended. <br>
Risk: The skill can generate tax, payroll, contract, project, and compliance guidance that may be incorrect, incomplete, stale, or jurisdiction-specific. <br>
Mitigation: Treat generated answers and self-check reports as decision support, verify policy sources and calculations, and consult qualified tax, audit, or legal professionals before filings, disputes, or material business decisions. <br>
Risk: The artifact can contact remote MCP and web endpoints and can store API keys, a client identifier, cache files, and logs locally. <br>
Mitigation: Run it in an environment approved for outbound network access and local persistence, inspect stored configuration under the documented local data directory, and remove cached credentials or logs when no longer needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/zxj2devs/skills/tax-construction) <br>
- [Construction Compliance Self-Check](https://mcp.aitaxs.top/web/topic_workflow_construction.html) <br>
- [Tax Compliance Self-Check Portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, structured text, JSON-like tool results, HTML self-check output, and Python command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; includes offline reference utilities for degraded operation.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
