## Description: <br>
Provides Xinjiang regional tax incentive guidance, eligibility checks, incentive selection support, local-share exemption planning, park setup considerations, and compliance self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, business operators, and tax practitioners use this skill to evaluate Xinjiang-focused enterprise income tax incentives, compare eligibility paths, prepare compliance checklists, and identify practical risk points for tax planning discussions. <br>

### Deployment Geography for Use: <br>
China (Xinjiang-focused tax scenarios) <br>

## Known Risks and Mitigations: <br>
Risk: Tax and business questions or self-check data may be sent to mcp.aitaxs.top, and fallback searches may send query text to public search engines. <br>
Mitigation: Avoid confidential identifiers, detailed financial records, or privileged tax/legal facts unless the provider and its data handling are approved. <br>
Risk: Local setup code can persist MCP configuration in AI-client configuration files when run directly or when TAX_ENABLE_AUTOSETUP=1 is set. <br>
Mitigation: Do not run config/init_agent.py directly or enable TAX_ENABLE_AUTOSETUP unless local configuration changes are intentional and reviewed. <br>
Risk: Tax guidance can be time-sensitive, incomplete, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Treat outputs as advisory and confirm material tax decisions with official sources or qualified tax and legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-xinjiang-preferential) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Xinjiang compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_xinjiang_preferential.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown text with links and optional configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory tax and compliance outputs; material conclusions should be reviewed against official sources and qualified professional advice.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
