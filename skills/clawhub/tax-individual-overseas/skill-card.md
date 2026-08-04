## Description: <br>
A Chinese-language tax-compliance assistant for individuals and advisors planning overseas securities, deposits, real estate, CRS consistency, foreign-income reporting, tax credits, and compliant investment channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals with overseas assets and tax advisors use this skill to assess China-related reporting, tax-credit, investment-channel, CRS, and residency questions, then produce structured risk notes, checklists, calculations, and compliance plan guidance. It is advisory support only and should be reviewed by qualified tax or legal professionals for filing, disputes, or high-value matters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to the provider's cloud MCP service. <br>
Mitigation: Avoid entering names, account numbers, tax IDs, exact balances, or other identifiers unless they are necessary and approved for disclosure. <br>
Risk: Fallback searches may send query text to Bing or Baidu when the remote service is unavailable. <br>
Mitigation: Use generalized, non-identifying facts in questions and review fallback results before relying on them. <br>
Risk: The client can store API keys, health/cache data, and logs under ~/.tax-policy-client. <br>
Mitigation: Inspect and clear local logs or cache after sensitive sessions, and manage the stored API key according to local credential-handling policy. <br>
Risk: Optional auto-setup can modify local AI-client MCP configuration. <br>
Mitigation: Do not set TAX_ENABLE_AUTOSETUP or run config/init_agent.py directly unless you intend to make those local configuration changes. <br>
Risk: Tax calculations and legal-policy guidance may be incomplete, time-sensitive, or jurisdiction-specific. <br>
Mitigation: Treat outputs as planning support and confirm material filing, dispute, or investment decisions with official sources and qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-individual-overseas) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Personal overseas investment self-check page](https://mcp.aitaxs.top/web/topic_workflow_individual_overseas.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown and structured text with occasional configuration snippets or command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools, fall back to public web search, and generate local offline reference output.] <br>

## Skill Version(s): <br>
3.15.10 (source: SKILL.md frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
