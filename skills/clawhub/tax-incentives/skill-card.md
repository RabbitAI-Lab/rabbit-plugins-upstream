## Description: <br>
Tax Incentives helps users assess Chinese tax incentive eligibility, qualification planning, R&D super-deduction issues, western-region preferences, and compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax practitioners, and business operators use this skill to answer tax-incentive questions, check qualification conditions, estimate incentive eligibility, and identify compliance risks before filing or professional review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Questions may include confidential company, audit, financial, or compliance details that could be sent to the remote MCP service or public-search fallback. <br>
Mitigation: Review the skill before installation and avoid submitting sensitive details unless the deployment accepts calls to mcp.aitaxs.top and public search services. <br>
Risk: The skill can store local API-key and log data during use. <br>
Mitigation: Review local data retention expectations and protect or remove local configuration, cache, and log files according to the user's security policy. <br>
Risk: Optional setup behavior may modify MCP client configuration when setup scripts are run directly or TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep automatic setup disabled unless intended, inspect proposed client configuration changes, and rely on backups before accepting MCP config updates. <br>
Risk: Tax guidance is time-sensitive and may not replace qualified advice for filings, audits, or regulated professional services. <br>
Mitigation: Verify material conclusions against official sources, tax authorities, or qualified tax professionals before taking action. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Tax incentive self-check page](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration, Shell commands] <br>
**Output Format:** [Markdown and plain text guidance with optional structured checklists, links, configuration snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, use public-search fallback, store local API-key and log files, and provide offline reference output when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
