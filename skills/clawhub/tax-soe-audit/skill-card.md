## Description: <br>
A Chinese tax compliance assistant for state-owned enterprise economic responsibility audits, focused on tax risk identification, evidence-chain preparation, remediation tracking, and related self-check workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, compliance teams, auditors, and tax practitioners use this skill to structure Chinese SOE tax-audit self-checks, identify common tax-risk scenarios, prepare supporting evidence, and draft practical remediation guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive audit and tax prompts, self-check metrics, and pseudonymous identifiers may be sent to mcp.aitaxs.top or public search engines during fallback. <br>
Mitigation: Avoid taxpayer identifiers, confidential allegations, vendor details, and internal financial facts unless the organization has approved that data flow; use anonymized scenarios or offline reference workflows where appropriate. <br>
Risk: The skill stores credentials and logs locally, including browser localStorage credentials for the web workflow and local client data under the tax-policy client directory. <br>
Mitigation: Review local credential and log storage before enterprise deployment, avoid shared-browser use for sensitive work, and clear or rotate stored keys according to organizational policy. <br>
Risk: Setup modes can modify MCP client configuration files. <br>
Mitigation: Keep automatic setup in dry-run mode unless configuration changes are approved, review generated MCP entries before enabling them, and retain backups for rollback. <br>
Risk: Tax and audit guidance is time-sensitive and may not resolve disputes or official determinations. <br>
Mitigation: Validate outputs against current laws, competent tax authorities, audit authorities, and qualified professional review before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-soe-audit) <br>
- [Interactive SOE audit tax workflow](https://mcp.aitaxs.top/web/topic_workflow_soe_audit.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured text, JSON-style tool responses, Python snippets, shell commands, and MCP configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base listing; offline workflows provide local reference guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
