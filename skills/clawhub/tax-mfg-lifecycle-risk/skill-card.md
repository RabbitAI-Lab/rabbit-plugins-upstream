## Description: <br>
制造业全生命周期涉税风险专项助手，帮助企业围绕设立、运营、重组、扩张和清算阶段进行合规自检、风险扫描、政策依据梳理和整改清单生成。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business users, finance and tax staff, and advisors use this skill to organize manufacturing tax risk reviews across formation, operations, restructuring, expansion, and liquidation scenarios. It produces practical self-check guidance, risk flags, policy references, and remediation-oriented checklists for Chinese manufacturing tax compliance workflows. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts mcp.aitaxs.top, stores a local API key and client ID, and can write local logs. <br>
Mitigation: Use it only if the remote service and local storage behavior are acceptable; avoid entering confidential business, transaction, payroll, or personally identifying tax details unless that trust decision has been made. <br>
Risk: Setup can optionally modify MCP client configuration and the matrix installer can install related skills from ZIP endpoints. <br>
Mitigation: Keep setup in dry-run or review mode unless configuration changes are intended, and inspect target MCP configuration plus any downloaded packages before enabling automatic installation. <br>
Risk: Remote proxying and public search fallback can expose prompts or tax scenarios outside the local environment. <br>
Mitigation: Limit submitted content to the minimum scenario details needed, avoid sensitive identifiers, and disable or restrict networked workflows in environments that require local-only processing. <br>
Risk: Tax guidance can be incomplete, outdated, or unsuitable for a specific taxpayer's facts. <br>
Mitigation: Verify policy citations, rates, deadlines, and filing positions against current official tax authority materials and qualified professional review before acting. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-mfg-lifecycle-risk) <br>
- [Manufacturing lifecycle self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_mfg_lifecycle.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge core skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [High-tech and R&D additional deduction skill](https://skillhub.cn/skills/tax-high-tech-rd) <br>
- [Enterprise restructuring tax skill](https://skillhub.cn/skills/tax-restructuring) <br>
- [VAT law implementation skill](https://skillhub.cn/skills/tax-vat-law) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown text with structured checklists, risk ratings, policy references, and optional shell or configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include web workflow links and MCP service guidance; tax conclusions require review against current official rules and competent authority requirements.] <br>

## Skill Version(s): <br>
3.15.3 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
