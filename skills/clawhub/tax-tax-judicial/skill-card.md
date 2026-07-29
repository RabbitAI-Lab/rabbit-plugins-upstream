## Description: <br>
A Chinese tax judicial and tax-dispute guidance skill focused on tax-collection crime cases, false VAT invoice sentencing and non-criminalization rules, downstream invoice recipient rights, mechanical tax assessment challenges, and structured tax criminal/dispute risk self-checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, tax teams, and advisors use this skill to ask Chinese tax judicial and dispute questions, run lightweight risk self-checks, and receive structured next-step guidance for evidence collection, procedure review, reconsideration or litigation planning, and internal remediation. It is not a substitute for licensed legal, tax, or criminal-defense representation. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax or legal scenarios may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Avoid entering company identifiers, invoice details, or confidential facts unless the user has approved that disclosure. <br>
Risk: Local credentials, configuration, and raw query logs may be stored under the user's tax policy client directory. <br>
Mitigation: Review or clear local config and log files as needed, and disclose this storage behavior before handling sensitive matters. <br>
Risk: Client MCP configuration can be modified when automatic setup is explicitly enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP unset unless the user intentionally wants the skill to update MCP client configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-tax-judicial) <br>
- [Interactive tax judicial self-check page](https://mcp.aitaxs.top/web/topic_workflow_tax_judicial.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured risk notes, MCP tool results, and optional code or configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Online operation may call the mcp.aitaxs.top service for policy questions, risk checks, calculations, and knowledge-base listings; offline files provide process guidance and keyword self-checks.] <br>

## Skill Version(s): <br>
3.15.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
