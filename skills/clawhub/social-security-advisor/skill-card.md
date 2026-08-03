## Description: <br>
A China-focused personal social-security planning assistant for delayed retirement, pension estimates, flexible-employment contributions, 4050 subsidies, transfers, contribution gaps, medical-insurance choices, cross-region settlement, personal pensions, and related benefits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and individuals use this skill to ask China social-security questions, run pension and contribution self-checks, and receive planning guidance. The skill also reminds users that final retirement age, benefit amounts, eligibility, and reimbursements should be confirmed with official agencies. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary says the package connects to an aitaxs tax-policy MCP service and may register local or browser credentials. <br>
Mitigation: Install only when that remote service and credential registration are intended; review or remove the config Python files if only the social-security reference content is needed. <br>
Risk: The server security summary says config/init_agent.py may modify supported AI-client MCP settings. <br>
Mitigation: Do not run config/init_agent.py unless host MCP configuration changes are desired; inspect setup behavior before enabling it. <br>
Risk: The security verdict is suspicious because the advertised social-security helper is packaged with broader tax-policy MCP, web-search fallback, and credential-storage behavior. <br>
Mitigation: Deploy in a controlled environment, restrict network access if it is not required, and verify social-security conclusions against official agencies before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/social-security-advisor) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Personal social-security self-check page](https://mcp.aitaxs.top/web/topic_workflow_personal_social_security.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax-policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with optional links, code or configuration snippets, and web self-check content.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service and user-supplied social-security facts for policy lookup, self-checks, and calculators.] <br>

## Skill Version(s): <br>
3.15.8 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
