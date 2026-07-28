## Description: <br>
行业涉税风险图谱专项助手，帮助用户识别加油站变票、网络货运虚开、物流企业、大宗商品贸易、税收洼地等高风险行业场景中的涉税风险、成因和应对路径。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Tax, finance, compliance, and legal users can use this skill to structure industry tax-risk self-checks, compare high-risk transaction patterns against compliance controls, and draft practical remediation guidance. Outputs are reference material only and should be confirmed with official tax authorities or qualified professionals for high-stakes matters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top, and fallback behavior may use public search engines. <br>
Mitigation: Avoid entering highly confidential taxpayer, employee, transaction, account, or non-public business details; use sanitized scenarios where possible. <br>
Risk: The skill can store local configuration, credentials, cache, logs, and browser localStorage data. <br>
Mitigation: Review and delete ~/.tax-policy-client logs, cached files, and browser localStorage on shared or sensitive machines. <br>
Risk: Auto-setup and matrix installation behavior can modify local MCP client configuration or install multiple related skills. <br>
Mitigation: Do not enable TAX_ENABLE_AUTOSETUP or run the matrix installer unless local MCP configuration changes and bulk skill installation are intentional. <br>
Risk: The skill provides tax-risk guidance that may be incomplete, outdated, or unsuitable for a specific taxpayer or jurisdiction. <br>
Mitigation: Treat outputs as reference material and confirm important conclusions with official tax sources, qualified tax advisors, or legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-industry-tax-risk) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax compliance topic portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown and structured text, with occasional code or shell command snippets for setup workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax-policy service, use offline fallback workflows, and generate risk summaries, checklists, reports, or setup guidance.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
