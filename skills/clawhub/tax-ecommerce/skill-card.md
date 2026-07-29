## Description: <br>
Provides China ecommerce and livestreaming tax-compliance guidance for platform sellers, MCNs, influencers, private-account collection risk, platform tax reporting, invoice handling, self-check workflows, cases, report templates, and operational remediation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce sellers, livestreaming operators, MCNs, influencers, and tax-compliance advisors use this skill to ask China ecommerce tax questions, run lightweight compliance self-checks, identify common risk patterns, and draft remediation-oriented compliance reports. It is not a substitute for licensed tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions, scenarios, and self-check metrics may be sent to mcp.aitaxs.top, and local credentials or logs may be stored on the user's machine. <br>
Mitigation: Avoid entering tax IDs, bank details, customer data, or confidential transaction specifics unless the publisher's data handling terms are acceptable; periodically inspect local client state such as ~/.tax-policy-client and browser localStorage. <br>
Risk: Client setup behavior can modify local MCP configuration when automatic setup is enabled. <br>
Mitigation: Review or disable TAX_ENABLE_AUTOSETUP before running setup scripts, and inspect proposed MCP configuration changes before allowing them to persist. <br>
Risk: The skill provides auxiliary tax guidance and calculations that may be incomplete, outdated, or unsuitable for a specific filing, audit, dispute, or legal matter. <br>
Mitigation: Confirm material conclusions against official tax authority sources and qualified tax, audit, or legal professionals before filing, paying, disputing, or restructuring. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Ecommerce compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance, structured checklists, report-style prose, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; includes offline fallback guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.4 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
