## Description: <br>
Provides tax and compliance guidance for traditional Chinese medicine clinics and medical institutions, including VAT exemptions, income tax treatment, physician individual income tax, invoicing, medical insurance settlement, risk self-checks, and remediation reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External clinic operators, finance teams, and compliance advisors use this skill to ask China-focused tax compliance questions, run medical-institution self-checks, identify invoice and medical-insurance risk areas, and draft practical remediation guidance. It is not a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive clinic, tax, financial, physician-income, invoice, or medical-insurance compliance details may be sent to mcp.aitaxs.top during Q&A, risk checks, calculations, or web self-checks. <br>
Mitigation: Review the skill before installation, avoid entering unnecessary identifiers or confidential records, and use it only where sending those scenario details to the remote service is acceptable. <br>
Risk: The Python and browser clients can create persistent local or browser API keys and client identifiers. <br>
Mitigation: Inspect local configuration and browser storage after use, rotate or delete generated credentials when no longer needed, and avoid shared machines for sensitive compliance work. <br>
Risk: Optional setup code can modify MCP client configuration when explicitly enabled or run directly. <br>
Mitigation: Run setup in dry-run mode first, review any proposed MCP configuration changes, and keep backups of client configuration before enabling automatic setup. <br>
Risk: The skill provides compliance guidance and self-check outputs that may be incomplete, stale, or unsuitable for a specific filing, audit, dispute, or legal matter. <br>
Mitigation: Treat outputs as preliminary guidance, verify against official tax authority sources, and consult licensed tax, audit, or legal professionals for high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/zxj2devs/skills/tax-tcm-clinic) <br>
- [TCM clinic compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_tcm_clinic.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown answers, structured self-check results, Python utility output, HTML workflow output, and MCP configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP services for policy Q&A, risk checks, tax calculations, and topic self-checks; includes local fallback guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
