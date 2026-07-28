## Description: <br>
Provides Chinese tax and corporate-governance guidance for equity transfers, family holding structures, state-owned enterprise mixed-ownership reform, VIE/red-chip structures, and equity-structure tax burden analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax and compliance teams, and advisors use this skill to reason through China-focused equity tax scenarios, generate self-check guidance, compare governance structures, and prepare risk-response checklists. It can also route related questions to adjacent tax skills and provide offline fallback guidance when the cloud service is unavailable. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can connect to cloud tax services, so sensitive shareholder, restructuring, or tax facts may leave the local agent environment. <br>
Mitigation: Use only if the publisher and remote endpoints are trusted, and avoid entering confidential business or personal tax data unless the data-handling terms are acceptable. <br>
Risk: The skill can register and store API credentials and log local question or scenario text. <br>
Mitigation: Review the credential and logging behavior before installation, use test data first, and periodically inspect or clear local configuration and log files. <br>
Risk: The skill includes installer and configuration behavior that can modify MCP client settings or install additional tax skills. <br>
Mitigation: Prefer dry-run or manual review before enabling setup or matrix installation, and verify the target skills directory and MCP configuration before use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-equity-governance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Equity governance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_equity_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with optional command snippets, configuration snippets, and structured checklist-style results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote tax-policy MCP tools, open the web self-check workflow, or use local offline fallback guidance depending on availability.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
