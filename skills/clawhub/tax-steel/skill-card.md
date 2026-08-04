## Description: <br>
Provides metallurgy-focused tax compliance guidance for steel, non-ferrous, rare earth, and precious metals businesses, including resource tax, VAT refund, transfer pricing, self-check workflows, and report-oriented remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business teams use this skill to ask metallurgy-sector tax compliance questions, run structured self-checks, identify risk areas, and prepare practical remediation or compliance report content. It is aimed at advisory support and does not replace official tax filing, audit, legal, or licensed professional advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax and business compliance prompts may be sent to the mcp.aitaxs.top cloud service, and fallback searches may use public search engines. <br>
Mitigation: Install only when that data flow is acceptable; avoid submitting sensitive taxpayer data unless it has been reviewed and approved for that service. <br>
Risk: The skill can store credentials and logs under ~/.tax-policy-client. <br>
Mitigation: Review local credential and log handling before deployment, restrict filesystem access, and clear stored data when the skill is no longer needed. <br>
Risk: The skill can persistently modify MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled or config/init_agent.py is executed directly. <br>
Mitigation: Keep automatic setup disabled unless intentional, review configuration changes before enabling them, and prefer dry-run behavior during assessment. <br>
Risk: Generated tax compliance guidance may be incomplete or unsuitable for a specific filing, audit, dispute, or legal matter. <br>
Mitigation: Treat outputs as advisory support and confirm material decisions with official sources, tax authorities, or qualified tax and legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-steel) <br>
- [Metallurgy tax compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_steel.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text, code, shell commands, configuration] <br>
**Output Format:** [Markdown and plain text guidance, with optional JSON-like structured results and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP calls for tax policy answers, risk checks, calculations, and knowledge-base listing; offline fallback provides process guidance when the service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
