## Description: <br>
Provides social-insurance tax-compliance guidance for contribution-base checks, personal-income-tax and social-insurance matching, employment classification, remediation planning, risk grading, and self-check reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business, tax, payroll, HR, and compliance users can ask social-insurance compliance questions, run self-check workflows, compare payroll and social-insurance bases, classify employment scenarios, estimate remediation exposure, and generate risk-focused action guidance. The skill is most relevant to China-oriented social-insurance and tax-compliance workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The security review flags under-disclosed remote service enrollment and calls to mcp.aitaxs.top. <br>
Mitigation: Review the publisher's data-handling terms before use, and avoid entering payroll, employee identity, or confidential business details unless those terms are acceptable. <br>
Risk: The package can persist a local API key and client identifier for MCP service access. <br>
Mitigation: Install only in trusted workspaces, inspect local credential files before sharing machines or backups, and rotate or remove credentials if the skill is no longer used. <br>
Risk: Optional setup code can modify local MCP client configuration. <br>
Mitigation: Keep auto-setup disabled unless intentional, review proposed MCP configuration changes, and prefer dry-run setup in managed or regulated environments. <br>
Risk: Social-insurance and tax guidance can become outdated or may not match a specific authority's interpretation. <br>
Mitigation: Treat generated answers and self-check reports as review aids, verify material conclusions against current official rules, and consult qualified professionals for filings, disputes, or remediation decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-social-insurance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Social-insurance compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_social_insurance.html) <br>
- [Tax-compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, JSON-like tool responses, generated report text, Python helper code, shell commands, and MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, open or reference a hosted web workflow, and use local offline fallback scripts when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: evidence.release.version and artifact/SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
