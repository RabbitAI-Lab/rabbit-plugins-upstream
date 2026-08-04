## Description: <br>
Battery consumption tax compliance assistant focused on tiered tax rates, exemption eligibility, CMA report prerequisites, processing-deduction handling, self-use transfer filing, lightweight self-checks, and risk scan guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External tax, finance, and compliance users use this skill to ask battery consumption tax questions, run self-check workflows, identify common filing risks, and generate practical compliance guidance. Developers and agent operators may also use its MCP and offline workflow files to connect the skill to tax-policy tools or fallback reference flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and self-check data may be routed to the vendor cloud service. <br>
Mitigation: Review the vendor service terms before installation and avoid entering confidential identifiers or sensitive business facts unless that routing is acceptable. <br>
Risk: Fallback searches may be sent to public search engines when the remote service is unavailable. <br>
Mitigation: Use non-sensitive, generalized queries in fallback mode and verify important tax conclusions against official sources or qualified advisors. <br>
Risk: The skill may store API credentials and raw query logs under ~/.tax-policy-client. <br>
Mitigation: Inspect and manage local files under ~/.tax-policy-client, restrict local access to that directory, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Optional auto-setup can modify local MCP client configuration. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run init_agent.py directly unless you intend to add the skill's MCP configuration to the local agent client. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-consumption-tax) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Battery consumption tax self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_consumption_tax.html) <br>
- [Tax policy knowledge portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge MCP service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text guidance, JSON tool responses, generated report text, and MCP/configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for policy questions, risk checks, tax calculations, and knowledge-base metadata; includes local offline reference workflows for degraded operation.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
