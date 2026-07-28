## Description: <br>
学历教育免税、非学历教育简易计税、托育保育免税、非营利组织免税资格、培训机构预收学费与课时费收入确认、教师个税与社保、发票合规、私户收款隐匿收入与骗取留抵退税风险、真实稽查案例、合规报告与实操指引专题助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External education providers, training organizations, private schools, childcare or early-education operators, and their advisors use this skill to ask tax compliance questions, run structured self-checks, identify common risk indicators, and draft practical remediation or compliance report guidance for China-focused education-sector tax scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts mcp.aitaxs.top and uses a locally stored API key and logs. <br>
Mitigation: Install only if that remote service, local credential storage, and logging model are acceptable; avoid entering confidential taxpayer, payroll, customer, or business-identifying details unless retention and logging controls are clarified. <br>
Risk: The package includes capabilities to install or route to a broader tax-skill matrix. <br>
Mitigation: Review the matrix entries and downloaded packages before use, install only needed related skills, and prefer dry-run or local-source installation paths when auditing behavior. <br>
Risk: Tax calculations, risk ratings, and policy interpretations can be incomplete or time-sensitive. <br>
Mitigation: Treat outputs as educational compliance support, verify conclusions against current official requirements, and consult a qualified tax or legal professional before filings or high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page: tax-education](https://clawhub.ai/zxj2devs/skills/tax-education) <br>
- [ClawHub publisher profile: zxj2devs](https://clawhub.ai/user/zxj2devs) <br>
- [Education compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_education.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, policy references, report templates, optional JSON-like tool results, and setup or installation commands when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote MCP service, store a local API key and logs, provide offline fallback guidance, and route or install related tax-skill matrix packages.] <br>

## Skill Version(s): <br>
3.15.3 (source: server evidence release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
