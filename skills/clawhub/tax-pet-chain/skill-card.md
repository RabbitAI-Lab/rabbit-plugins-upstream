## Description: <br>
Tax Pet Chain helps agents answer China-focused pet chain tax compliance questions, run risk self-checks, and produce practical guidance for pet medical, food, grooming, boarding, franchise, live-animal sale, and import scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External businesses, finance teams, tax advisors, and agents use this skill to classify pet-chain tax scenarios, identify compliance risks, calculate or estimate tax impacts, and draft self-check reports or operating guidance. Outputs should be reviewed by qualified tax or legal professionals before filing, audit, dispute, or other high-stakes use. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, risk scenarios, and self-check metrics may be sent to the operator's cloud service, and fallback searches may be sent to public search engines when the cloud service is unavailable. <br>
Mitigation: Use only data approved for external processing, avoid confidential business or personal details unless reviewed, and disable or avoid fallback search for sensitive matters. <br>
Risk: Credentials, cache data, health state, and logs may be stored locally under ~/.tax-policy-client. <br>
Mitigation: Protect that directory as sensitive, restrict local access, rotate or remove stored credentials when no longer needed, and clear logs or cache according to organizational policy. <br>
Risk: Optional setup paths can modify agent or MCP client configuration when run directly or when TAX_ENABLE_AUTOSETUP is enabled. <br>
Mitigation: Review setup behavior in dry-run mode first, keep TAX_ENABLE_AUTOSETUP unset unless approved, and inspect configuration backups and changes before regular use. <br>
Risk: Tax outputs may be incomplete, outdated, or unsuitable for a specific filing, audit, or dispute. <br>
Mitigation: Treat outputs as decision support only and require review by qualified tax or legal professionals for high-stakes use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-pet-chain) <br>
- [Pet chain compliance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_pet_chain.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance and structured tool results, with optional shell commands, configuration snippets, and report-style text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use cloud MCP tools for policy Q&A, risk checks, tax calculation, and knowledge-base metadata; local offline helpers provide limited reference guidance when cloud service is unavailable.] <br>

## Skill Version(s): <br>
3.15.10 (source: SKILL.md frontmatter and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
