## Description: <br>
Assists with Chinese high-tech enterprise certification and R&D expense super-deduction compliance through indicator checks, expense classification guidance, multi-basis reporting, self-check workflows, and audit-response guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax advisors, finance teams, and compliance teams use this skill to assess Chinese high-tech enterprise qualification, R&D super-deduction eligibility, evidence retention, auxiliary ledgers, and tax audit readiness. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, payroll, audit, or R&D information may be processed by cloud services at mcp.aitaxs.top. <br>
Mitigation: Use the skill only when that cloud processing is acceptable, avoid entering secrets or unnecessary company identifiers, and minimize confidential inputs. <br>
Risk: Credentials, logs, and raw prompts may be stored locally under ~/.tax-policy-client. <br>
Mitigation: Avoid entering secrets and periodically inspect or delete local logs and stored credentials. <br>
Risk: The skill can modify MCP client configuration when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless automatic setup is intentional, and review client configuration changes before enabling it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-high-tech-deduction) <br>
- [High-tech tax workflow](https://mcp.aitaxs.top/web/topic_workflow_high_tech.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown text with structured checklists, calculations, report sections, and links to interactive workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include self-check prompts, evidence-chain summaries, auxiliary-ledger guidance, and MCP setup guidance.] <br>

## Skill Version(s): <br>
3.15.10 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
