## Description: <br>
Tax Legal Tax Review helps agents produce structured Chinese tax and legal review guidance for pre-transaction tax due diligence, tax clauses in deal documents, tax-related legal templates, audit-standard tax review workflows, and forensic accounting quality control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, legal teams, finance teams, and agent developers use this skill to structure tax/legal due diligence, draft tax-related review materials, identify tax compliance risks, and generate practical review checklists for Chinese tax compliance contexts. Outputs are reference guidance and should be reviewed by qualified legal, tax, or audit professionals before use in high-stakes matters. <br>

### Deployment Geography for Use: <br>
Global; the skill content is focused on Chinese tax and legal compliance contexts. <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, legal, M&A, litigation, client, or taxpayer-identifying prompts may be processed by mcp.aitaxs.top. <br>
Mitigation: Use anonymized or synthetic facts for evaluation, avoid confidential inputs unless the publisher provides adequate privacy terms, and require professional review before relying on outputs. <br>
Risk: The skill stores API credentials, health state, cache data, and logs under a local tax-policy client directory. <br>
Mitigation: Protect the local user account, avoid sharing generated logs or config files, and remove local credentials and logs when the skill is no longer needed. <br>
Risk: Agent MCP client configuration can be changed when setup is explicitly enabled. <br>
Mitigation: Keep setup in dry-run mode during review, inspect proposed MCP configuration changes, and enable automatic setup only after approving the remote endpoint and generated backups. <br>
Risk: Tax and legal outputs may be incomplete, stale, or unsuitable for a specific transaction or dispute. <br>
Mitigation: Verify policy citations against official sources and have qualified tax, legal, or audit professionals review outputs before filing, negotiating, litigating, or closing a transaction. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-legal-tax-review) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text guidance with optional JSON tool results, Python workflow scripts, HTML workflow assets, and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can call remote MCP tools for tax policy questions, risk checks, tax calculations, and knowledge-base listings; offline scripts provide local reference guidance when the remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
