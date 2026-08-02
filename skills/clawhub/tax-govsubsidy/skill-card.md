## Description: <br>
Helps agents guide China tax compliance work for government subsidies and fiscal funds, including non-taxable income classification, dedicated-use documentation, separate accounting, related expense treatment, five-year tracking, input VAT treatment, and government service purchase distinctions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax or compliance teams use this skill to ask government-subsidy tax questions, run structured self-checks, build non-taxable income ledgers and five-year tracking templates, and draft compliance reports or remediation plans. Agents can also use its MCP and offline helpers to provide policy Q&A, risk screening, tax calculations, and fallback process guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be processed by the mcp.aitaxs.top cloud service. <br>
Mitigation: Avoid entering identifiable or highly sensitive business details unless necessary, and review cloud-processing acceptability before installation or use. <br>
Risk: The skill can store local credentials and logs under ~/.tax-policy-client. <br>
Mitigation: Review local data-retention expectations, restrict filesystem access where appropriate, and remove stored credentials or logs when they are no longer needed. <br>
Risk: Autosetup and configuration helpers can modify MCP client settings. <br>
Mitigation: Run autosetup/config scripts only when MCP client setting changes are intended, and inspect proposed configuration before enabling non-dry-run setup. <br>
Risk: Tax guidance may be incomplete or inappropriate for a specific taxpayer's facts. <br>
Mitigation: Use outputs as compliance support, verify against official tax authority positions, and route material subsidy classification or filing decisions to qualified tax professionals. <br>


## Reference(s): <br>
- [ClawHub skill page: tax-govsubsidy](https://clawhub.ai/zxj2devs/skills/tax-govsubsidy) <br>
- [Publisher profile: zxj2devs](https://clawhub.ai/user/zxj2devs) <br>
- [Government subsidy compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_govsubsidy.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy MCP endpoint](https://mcp.aitaxs.top/api/services/tax-policy-knowledge/mcp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown guidance, structured JSON-style tool results, configuration snippets, checklists, ledgers, and report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; local fallback helpers provide limited offline guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
