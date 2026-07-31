## Description: <br>
Provides contract template guidance, contract drafting support, clause review, tax-risk checks, and review-report generation across common enterprise contract workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Enterprise legal, compliance, finance, tax, and management users use this skill to find contract templates, draft contract clauses, review tax and legal-risk indicators, and produce contract compliance review reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Contract text, tax scenarios, business identifiers, or legal-analysis prompts may be sent to a remote tax-policy service. <br>
Mitigation: Review the remote-service behavior before installation and avoid submitting confidential or regulated contract content unless the service is approved for that workspace. <br>
Risk: The skill may persist API keys, identifiers, and logs locally. <br>
Mitigation: Check whether browser local storage and ~/.tax-policy-client storage are acceptable, and clear or restrict those files when handling sensitive matters. <br>
Risk: Optional MCP client configuration changes may affect the agent's tool environment. <br>
Mitigation: Review MCP configuration changes before enabling the integration and limit installation to trusted workspaces. <br>
Risk: Tax and contract outputs can be mistaken for binding legal, tax, audit, or filing advice. <br>
Mitigation: Use outputs as drafting and review aids only, and require qualified legal or tax review before filing, signing, dispute handling, or high-value decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-contract-generation-review) <br>
- [Contract compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_contract.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional code, shell-command, configuration, and report-style sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide contract templates, clause suggestions, risk ratings, tax calculations, policy references, self-check links, and review-report content.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
