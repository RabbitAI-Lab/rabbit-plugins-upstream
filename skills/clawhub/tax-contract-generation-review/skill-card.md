## Description: <br>
Helps business legal, compliance, finance, and tax teams draft contract templates, review clauses, identify contract tax risks, and generate structured contract review reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business legal, compliance, finance, and tax users can use this skill to find contract templates, draft contract clauses, check legal and tax compliance issues, and prepare review reports across contract lifecycle workflows. The source content focuses on contract tax and compliance review, including risk indicators, clause revision suggestions, and report-ready findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive contract, employee, pricing, tax, or client information may be sent to a remote tax service. <br>
Mitigation: Review and redact prompts before use, and install only in environments where sending those scenarios to mcp.aitaxs.top is approved. <br>
Risk: Fallback behavior may use public search engines. <br>
Mitigation: Avoid submitting confidential scenarios when public-search fallback is possible, and restrict use to cases where public lookup is acceptable. <br>
Risk: API credentials and logs may be stored locally under the user's home directory. <br>
Mitigation: Review local storage locations, limit filesystem access, and remove stored credentials when the skill is no longer needed. <br>
Risk: Setup can modify MCP client configuration. <br>
Mitigation: Review configuration changes before enabling setup and install only for approved MCP clients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive contract compliance self-check](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown or plain text reports with structured checklists, risk ratings, clause suggestions, and implementation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include contract templates, risk findings, policy references, revision suggestions, and report sections.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
