## Description: <br>
个人社保全攻略智能助手，帮助用户查询延迟退休、养老金测算、灵活就业参保、4050补贴、社保转移、断缴补救、医保选择、异地就医、个人养老金、失业保险、工伤保险、生育保险与生育津贴等个人社保场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and advisors use this skill to ask Chinese personal social-security policy questions, compare retirement and pension scenarios, plan flexible-employment contributions, and review social-security risk or subsidy options. It also provides interactive self-check and calculator workflows for social-security planning. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The server security verdict is suspicious because the package presents as a personal social-security advisor but includes broader tax-policy tooling and compliance workflows. <br>
Mitigation: Review the full package scope before installation and treat it as a broader tax and compliance integration, not only a narrowly scoped social-security advisor. <br>
Risk: Queries or self-check data may be sent to a remote tax-policy-backed service. <br>
Mitigation: Avoid entering sensitive personal data unless the deployment has approved the remote service and data-handling posture. <br>
Risk: The artifact includes local API-key and log persistence. <br>
Mitigation: Review local storage paths and retention expectations before use, and clear stored credentials or logs according to organizational policy. <br>
Risk: The artifact includes optional MCP client configuration changes. <br>
Mitigation: Install only after reviewing proposed MCP configuration changes and confirming they point to expected services. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/social-security-advisor) <br>
- [Interactive personal social-security workflow](https://mcp.aitaxs.top/web/topic_workflow_personal_social_security.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown guidance with links, calculations, checklists, and optional configuration instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote tax-policy MCP services, local fallback workflows, and an interactive HTML workflow for self-checks and calculators.] <br>

## Skill Version(s): <br>
3.15.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
