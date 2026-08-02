## Description: <br>
Helps users assess Chinese tax incentive eligibility, qualification planning, research and development deduction scenarios, Western Development incentives, specialized enterprise incentives, and related compliance risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax practitioners use this skill to ask about Chinese tax incentive eligibility, compare qualification requirements, run self-check workflows, and prepare compliance-oriented next steps. It is most useful for preliminary analysis and should be confirmed against official policy sources or qualified tax advice for material decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and self-check metrics may be sent to a remote service. <br>
Mitigation: Review the service trust boundary before use and avoid entering confidential business or personal tax details unless the service is approved for that data. <br>
Risk: The package can optionally modify local MCP client configuration. <br>
Mitigation: Do not run config/init_agent.py with write mode or set TAX_ENABLE_AUTOSETUP unless configuration changes are intended and reviewed. <br>
Risk: Persistent credentials, local logs, and browser storage may remain after use. <br>
Mitigation: Clear ~/.tax-policy-client and relevant browser localStorage entries when uninstalling or rotating stored identifiers and API keys. <br>
Risk: Tax incentive guidance can become outdated or may not match a specific taxpayer's facts. <br>
Mitigation: Confirm material filing or qualification decisions against official policy sources, the competent tax authority, or qualified tax professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Tax incentives self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with optional structured checklists, risk summaries, calculations, links, and setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP services for policy answers, risk checks, tax calculations, and knowledge base listing; includes offline fallback guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
