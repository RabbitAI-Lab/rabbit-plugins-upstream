## Description: <br>
个人社保全攻略智能助手，聚焦延迟退休年龄计算、基本养老金测算、灵活就业人员参保选档、4050社保补贴申领、社保关系转移接续、断缴影响与补救、居民医保与职工医保选择、异地就医直接结算、个人养老金制度等个人社保全场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and advisors use this skill to ask personal social-security planning questions, compare pension and contribution scenarios, and receive structured checklists for retirement timing, flexible employment contributions, medical insurance, transfer continuity, and benefit eligibility. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The package can make remote calls to mcp.aitaxs.top and register API-key based access for web or MCP-backed workflows. <br>
Mitigation: Install only when remote service use is expected, and avoid entering sensitive personal, pension, medical, employment, or company identifiers unless the publisher provides clear data-handling and consent details. <br>
Risk: The release includes broader tax-policy matrix clients, installers, routing logic, and possible local client configuration changes beyond a narrow social-security advisor. <br>
Mitigation: Review the included installer, routing, and configuration behavior before installation, especially in managed or production agent environments. <br>
Risk: Social-security calculations and benefit guidance can affect user decisions but may not match final agency determinations. <br>
Mitigation: Use outputs as planning guidance and verify final retirement age, pension amounts, eligibility, payments, and claims with official social-security or medical-insurance channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/social-security-advisor) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Personal social-security workflow](https://mcp.aitaxs.top/web/topic_workflow_personal_social_security.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax-policy MCP service endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions, Shell commands] <br>
**Output Format:** [Markdown responses with structured checklists, links, and occasional shell or configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct users to a web self-check workflow and remote MCP-backed policy tools.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
