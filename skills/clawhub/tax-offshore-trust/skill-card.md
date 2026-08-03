## Description: <br>
A tax compliance assistant for offshore trusts and cross-border family wealth scenarios, covering income tax obligations, foreign-income reporting, CFC considerations, CRS compliance, anti-avoidance checks, and structured self-assessment workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, and agents use this skill to answer offshore-trust tax questions, run compliance self-checks, identify filing and withholding obligations, and draft practical remediation or reporting guidance. It is especially focused on cross-border family wealth, foreign income, CRS, CFC, and anti-avoidance scenarios. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send tax questions, scenarios, and self-check metrics to mcp.aitaxs.top and may use public search engines during fallback. <br>
Mitigation: Do not enter client-identifying, account, trust, beneficiary, or confidential financial details unless the publisher documents retention, endpoint scope, and security controls clearly enough for the intended use. <br>
Risk: The remote tax service is broad and not clearly scoped to the advertised offshore-trust purpose. <br>
Mitigation: Review endpoint scope and tool behavior before deployment, and restrict network use where only local or reviewed sources are acceptable. <br>
Risk: The skill includes auto-setup/configuration-writing paths and persistent credential storage. <br>
Mitigation: Review or disable auto-setup and persistent API-key storage before using the skill in regulated, shared, or managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-offshore-trust) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Offshore trust compliance workflow](https://mcp.aitaxs.top/web/topic_workflow_offshore_trust.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Cross-border tax skill](https://skillhub.cn/skills/tax-crossborder) <br>
- [Individual tax and social insurance skill](https://skillhub.cn/skills/tax-social-insurance) <br>
- [Tax compliance dispute skill](https://skillhub.cn/skills/tax-compliance-dispute) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown text with structured checklists, practical guidance, optional configuration snippets, and shell commands for local workflows.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a remote tax policy MCP service and may use offline reference workflows when remote service access is unavailable.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
