## Description: <br>
Helps agents produce tax and legal review guidance for M&A tax due diligence, tax-related legal documents, audit-standard tax checks, forensic accounting quality control, and integrated legal-finance-tax review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and advisors use this skill to structure Chinese tax and legal compliance reviews, create due diligence checklists and document guidance, and triage transaction or audit risks before professional review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and risk scenarios may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Use non-confidential inputs unless the publisher documents endpoint ownership, retention, logging, and opt-out controls clearly enough for the deployment environment. <br>
Risk: The skill can store a local API key, device identifier, raw questions, and scenarios. <br>
Mitigation: Review local storage and logs before use with client, M&A, tax, or legal matter data; avoid entering secrets or regulated personal data. <br>
Risk: Fallback behavior can use public search engines when the remote service is unavailable. <br>
Mitigation: Treat fallback search results as unverified references and confirm policy, tax, and legal conclusions against authoritative sources or qualified professionals. <br>
Risk: Autosetup or setup script execution can modify MCP client configuration. <br>
Mitigation: Keep autosetup disabled unless needed, review proposed MCP configuration changes, and verify backups before enabling the skill in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-legal-tax-review) <br>
- [Legal-tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_legal_tax_review.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and structured text, with optional Python workflow scripts, HTML workflow output, shell commands, and MCP JSON responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include legal-tax risk triage, checklists, document guidance, calculations, workflow steps, and self-check reports; substantive tax or legal conclusions should be reviewed by qualified professionals.] <br>

## Skill Version(s): <br>
3.15.10 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
