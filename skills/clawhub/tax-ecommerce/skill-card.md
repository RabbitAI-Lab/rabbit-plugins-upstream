## Description: <br>
A Chinese-language tax compliance assistant for domestic ecommerce, livestream sales, MCNs, platform reporting, revenue recognition, invoice risk, private-account payment risk, case review, report templates, and practical self-check guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax-compliance practitioners use this skill to ask ecommerce and livestream tax questions, perform risk self-checks, review common compliance scenarios, and produce practical checklists or report-style guidance for follow-up review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and self-check metrics may be sent to the provider's cloud service. <br>
Mitigation: Avoid entering confidential taxpayer, bank, identity, or trade-secret details unless the provider's privacy and retention practices have been reviewed. <br>
Risk: The skill can store local or web API credentials for MCP-backed use. <br>
Mitigation: Review where credentials are stored, restrict access to the local profile, and remove stored keys when the skill is no longer needed. <br>
Risk: Optional setup code can add MCP server entries to local agent configuration. <br>
Mitigation: Run setup in dry-run or review mode first, inspect configuration changes before enabling them, and keep backups of existing agent configuration files. <br>
Risk: Tax calculations, risk scores, and compliance guidance may be incomplete or jurisdiction-sensitive. <br>
Mitigation: Treat outputs as review aids and confirm material filing, audit, or legal positions with qualified tax or legal professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ecommerce) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Ecommerce compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_ecommerce.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration] <br>
**Output Format:** [Markdown and plain text guidance with optional links, checklists, risk summaries, and report-style sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include self-check results, tax-risk explanations, policy-reference summaries, and setup/configuration guidance for MCP-backed use.] <br>

## Skill Version(s): <br>
3.15.5 (source: evidence.release.version, artifact/SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
