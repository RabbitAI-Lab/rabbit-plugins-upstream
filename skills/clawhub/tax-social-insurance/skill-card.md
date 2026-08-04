## Description: <br>
A Chinese social-insurance and tax-compliance assistant for social-insurance contribution governance, payroll-tax alignment, flexible employment classification, historical underpayment remediation, risk grading, audit response, and self-check reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employers, HR teams, payroll teams, tax professionals, and developers use this skill to answer China social-insurance compliance questions, structure self-checks, estimate contribution differences, prepare remediation plans, and generate compliance guidance or reports. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and compliance scenarios may be sent to the mcp.aitaxs.top tax-policy service or fallback public search engines. <br>
Mitigation: Avoid submitting sensitive company identifiers, payroll details, personal data, or confidential compliance facts unless the publisher documents data handling clearly. <br>
Risk: The skill uses local logging and may store API keys or service configuration. <br>
Mitigation: Review local config, cache, and log files before and after use; protect or delete stored credentials and logs according to organizational policy. <br>
Risk: Optional setup can modify MCP client configuration. <br>
Mitigation: Inspect setup output and configuration changes before enabling automatic setup, especially in managed enterprise agent environments. <br>
Risk: Social-insurance and tax guidance can be outdated, incomplete, or jurisdiction-sensitive. <br>
Mitigation: Verify outputs against official tax and social-insurance authorities or qualified professionals before taking compliance action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Social-insurance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional structured text, shell command examples, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can depend on remote tax-policy MCP responses, public-search fallback behavior, and local offline reference workflows; compliance conclusions should be reviewed against official authorities.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
