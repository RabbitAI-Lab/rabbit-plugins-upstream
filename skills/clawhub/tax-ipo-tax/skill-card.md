## Description: <br>
Tax IPO Tax is a Chinese IPO tax-compliance assistant for tax incentive dependency, disclosure requirements, red-chip structure tax evidence, Beijing Stock Exchange review concerns, self-check workflows, and compliance report preparation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax professionals, finance teams, and IPO advisers use this skill to structure Chinese IPO tax-compliance self-checks, identify tax review issues, and draft practical remediation or disclosure guidance. It supports question answering, risk screening, tax calculation calls, web-based self-check prompts, and offline process guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed tax assistance may send tax questions, scenarios, or self-check data to the publisher's remote service. <br>
Mitigation: Avoid submitting confidential IPO, financing, personal, company-identifying, or client-sensitive details unless the publisher's data handling is acceptable. <br>
Risk: The package can persist API credentials for the remote service. <br>
Mitigation: Review stored credential files after installation and rotate or remove credentials if the skill is no longer trusted or needed. <br>
Risk: Local logs and cache files may retain prompts, scenarios, statuses, or operational metadata. <br>
Mitigation: Review and clear the local data, cache, and log directories when handling sensitive matters. <br>
Risk: Autosetup behavior can modify supported client MCP configuration files when explicitly enabled. <br>
Mitigation: Keep autosetup disabled unless wanted, inspect configuration diffs or backups, and remove the MCP entry if it is not approved. <br>
Risk: Public-search fallback may query external search engines when the remote tax service is unavailable. <br>
Mitigation: Disable or avoid fallback public search for sensitive facts and use sanitized, non-identifying search terms. <br>
Risk: Tax and IPO review guidance can be incomplete, outdated, or unsuitable for a specific regulated transaction. <br>
Mitigation: Treat outputs as draft guidance and confirm material tax positions with current official rules and qualified professionals before filing, disclosure, or transaction decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [IPO tax workflow page](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge service](https://mcp.aitaxs.top/api/services/tax-policy-knowledge) <br>
- [Comprehensive tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Listed-company advisory skill](https://skillhub.cn/skills/tax-listed-advisory) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with optional JSON tool results, Python workflow output, configuration snippets, downloadable CSV files, and copied prompt/report text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy answers, risk checks, tax calculations, and knowledge-base metadata; includes local offline fallback guidance when cloud access is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
