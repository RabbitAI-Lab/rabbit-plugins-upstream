## Description: <br>
Helps users assess cross-border ecommerce and trade tax compliance risks, including import and export tax treatment, export refund documentation, withholding tax, CRS, beneficial ownership, VIE/red-chip structures, and Hainan Free Trade Port issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, finance teams, tax practitioners, and cross-border ecommerce operators use this skill to ask tax compliance questions, run structured self-checks, and prepare practical remediation checklists or report drafts. It supports risk triage and documentation workflows but does not replace qualified tax, audit, or legal advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax, client, identity, or business details may be processed by the remote mcp.aitaxs.top service. <br>
Mitigation: Review the provider's data handling terms before use and avoid entering confidential information unless remote processing is acceptable. <br>
Risk: The skill can persist service credentials or logs locally and includes broad setup or matrix-install behavior. <br>
Mitigation: Install only in environments where local credential and log persistence is acceptable, and use matrix install or auto-setup only when intentional. <br>
Risk: Tax calculations and compliance recommendations may be incomplete, outdated, or unsuitable for a specific filing position. <br>
Mitigation: Treat outputs as preliminary self-check guidance and have qualified tax, audit, or legal professionals verify material decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-crossborder) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Cross-border compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_crossborder.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [SkillHub cross-border tax skill page](https://skillhub.cn/skills/tax-crossborder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration, shell commands] <br>
**Output Format:** [Markdown guidance with checklists, risk summaries, report drafts, and optional setup or configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use remote MCP-backed processing and a local web self-check workflow; users should review generated guidance before relying on it.] <br>

## Skill Version(s): <br>
3.15.3 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
