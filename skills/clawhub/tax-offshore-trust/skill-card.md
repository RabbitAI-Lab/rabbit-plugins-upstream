## Description: <br>
Tax Offshore Trust helps agents answer and structure compliance workflows for offshore trust personal income tax, cross-border family wealth, foreign income reporting, controlled foreign company, CRS, and anti-avoidance scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, and agents use this skill to triage offshore trust personal income tax obligations, run structured self-checks, and produce compliance-oriented answers, checklists, calculations, and report-style guidance. It is not a substitute for licensed tax, legal, filing, or trust advisory services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive trust, tax residency, asset, beneficiary, or family wealth details may be sent to the remote mcp.aitaxs.top service and raw prompts or scenarios may be logged locally. <br>
Mitigation: Use redacted and minimized scenarios; do not enter sensitive details unless the user accepts the remote-service and local-logging behavior. <br>
Risk: Optional auto-setup can persistently modify MCP client configuration files when config/init_agent.py is run directly or TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep auto-setup disabled unless intentional, review backups and client MCP configuration before and after setup, and avoid running config/init_agent.py directly during routine use. <br>
Risk: The security scan verdict is suspicious because the release combines remote service registration, broad tax-tool proxying, and local logging. <br>
Mitigation: Review the package and server endpoints before installation, run it in a controlled environment, and prefer offline fallback guidance when remote disclosure is unacceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Offshore trust workflow page](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Remote MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance and JSON tool results, with optional configuration snippets for MCP clients.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can use a remote MCP service for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline fallback scripts provide local text guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
