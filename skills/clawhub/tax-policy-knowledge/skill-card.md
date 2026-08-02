## Description: <br>
A tax policy and compliance assistant for Chinese tax questions, risk self-checks, invoice compliance, contract tax review, tax calculations, and compliance report guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax advisors, and compliance reviewers use this skill to answer China-focused tax policy questions, perform tax and invoice risk self-checks, calculate common tax scenarios, and draft practical compliance guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, payroll, contract, or compliance inputs may be sent to remote services or fallback public search engines. <br>
Mitigation: Avoid real client or customer data unless the publisher documents data handling, retention, opt-out controls, and setup behavior clearly enough for the deployment environment. <br>
Risk: Local credentials, cache files, and logs may be stored under ~/.tax-policy-client. <br>
Mitigation: Review local storage behavior before installation, restrict filesystem access where possible, and clear local credentials or logs according to the organization's data handling policy. <br>
Risk: Tax guidance can be jurisdiction-specific and may be incomplete or outdated if remote services or fallback search results are unavailable or stale. <br>
Mitigation: Require professional review and source verification before using outputs for filings, client advice, contractual decisions, or compliance remediation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-policy-knowledge) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or plain text responses with optional code, shell commands, configuration snippets, self-check lists, calculations, and report-style guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP tools for policy answers, risk checks, tax calculations, and knowledge-base listing; local offline workflows provide limited reference guidance when remote service is unavailable.] <br>

## Skill Version(s): <br>
3.15.7 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
