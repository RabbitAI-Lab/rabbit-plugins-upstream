## Description: <br>
减资撤资（未实缴减资）个人所得税专项助手，帮助 users analyze capital reduction and shareholder withdrawal tax scenarios, run self-checks, estimate personal income tax exposure, and draft compliance guidance or report templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, tax professionals, and business users use this skill to evaluate Chinese company capital reduction, unpaid subscribed-capital reductions, shareholder withdrawals, company share repurchases, and related personal income tax risks. It provides structured compliance self-checks, policy-oriented guidance, calculations, evidence checklists, and report-style outputs for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan says the skill may send tax questions and self-check indicators to remote services. <br>
Mitigation: Do not enter confidential taxpayer, company, or transaction details unless the service operator's privacy and retention terms have been reviewed and accepted. <br>
Risk: The security scan says the skill stores API credentials and logs locally. <br>
Mitigation: Review local storage behavior before deployment, restrict file permissions where possible, and avoid sharing logs or configuration files that may contain sensitive scenario details or credentials. <br>
Risk: The security scan says setup behavior can alter MCP client configuration. <br>
Mitigation: Run setup only in a controlled environment, inspect proposed configuration changes, and keep backups of existing MCP client configuration. <br>
Risk: The security scan summary says the main skill description does not clearly disclose remote services, local key storage, local logging, and MCP configuration changes. <br>
Mitigation: Review the full artifact and security guidance before installing, and disclose these behaviors to users who will rely on the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-capital-reduction) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Capital reduction self-check page](https://mcp.aitaxs.top/web/topic_workflow_capital_reduction.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown and plain text responses with optional Python tools, MCP configuration snippets, and web self-check links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include tax-risk summaries, calculation guidance, evidence checklists, report templates, MCP setup guidance, and fallback offline workflow text.] <br>

## Skill Version(s): <br>
3.15.4 (source: evidence.release.version and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
