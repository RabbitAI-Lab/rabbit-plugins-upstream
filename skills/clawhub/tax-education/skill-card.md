## Description: <br>
学历教育免税、非学历教育简易计税、托育保育免税、非营利组织免税资格、培训机构预收学费与课时费收入确认、教师个税与社保、发票合规、私户收款隐匿收入与骗取留抵退税风险、真实稽查案例、合规报告与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External education and training operators, finance teams, and advisors use this skill to self-check Chinese tax compliance questions around VAT exemptions, non-degree training tax treatment, nonprofit school qualification, tuition revenue recognition, invoices, teacher tax, social insurance, and risk response. It provides guidance, risk checklists, self-check workflows, and report-oriented tax compliance suggestions; it does not replace licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts mcp.aitaxs.top and related SkillHub or ClawHub services for policy tools, registration, downloads, and web self-check workflows. <br>
Mitigation: Review the remote-service and retention posture before use, and avoid submitting confidential tax, payroll, student, or business data unless that posture is acceptable. <br>
Risk: The client can store local API credentials under the user profile. <br>
Mitigation: Treat the local client configuration as sensitive, restrict file access, and rotate or remove credentials when the skill is no longer trusted. <br>
Risk: Setup and installer paths can change local MCP/client configuration and install additional tax skills. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled and avoid setup or matrix installer scripts unless you intentionally want those local changes. <br>
Risk: Tax calculations, exemption checks, and risk scores are advisory and may be incomplete for a specific taxpayer or locality. <br>
Mitigation: Use outputs as a preliminary self-check and confirm material decisions with official tax sources or qualified tax, audit, or legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [Education tax compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Skill source manifest](artifact/SKILL.md) <br>
- [Matrix configuration](artifact/matrix.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with optional links, checklists, report text, and configuration or installation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools, use a local offline fallback for limited checks, and produce compliance self-check prompts or report-ready text.] <br>

## Skill Version(s): <br>
3.14.38 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
