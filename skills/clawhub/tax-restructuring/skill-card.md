## Description: <br>
Tax Restructuring helps agents provide Chinese tax restructuring guidance, risk self-checks, policy-source prompts, and compliance report drafts for bankruptcy reorganization, listed-company restructuring, mergers, splits, debt restructuring, and cross-border restructuring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and business, finance, tax, and compliance teams use this skill to ask restructuring tax questions, run lightweight self-checks, identify likely tax risks, and draft action-oriented compliance analysis for Chinese restructuring scenarios. It is advisory support and does not replace filing, legal representation, or confirmation by tax authorities or qualified professionals. <br>

### Deployment Geography for Use: <br>
China-focused <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive tax questions and self-check metrics may be sent to mcp.aitaxs.top. <br>
Mitigation: Use the skill only after organizational approval for that data flow, and avoid company-identifying or confidential transaction details unless approved. <br>
Risk: The client can persist API credentials, health state, cache, and logs in a local user data directory. <br>
Mitigation: Review local client storage before enterprise deployment, restrict access to the user profile, and rotate or remove stored API keys when no longer needed. <br>
Risk: Optional setup behavior can add MCP configuration entries to supported clients when explicitly enabled. <br>
Mitigation: Keep automatic setup disabled unless intended, inspect MCP configuration changes after enabling it, and remove entries that are not approved. <br>
Risk: Tax restructuring guidance can be incomplete or time-sensitive for specific transactions. <br>
Mitigation: Confirm material restructuring advice with current official sources, the competent tax authority, or qualified tax and legal professionals before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-restructuring) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Restructuring self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_restructuring.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge matrix](https://skillhub.cn/skills/tax-policy-knowledge) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance, structured self-check results, copied report text, and MCP configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call cloud MCP tools for policy Q&A, risk checks, tax calculations, and knowledge-base metadata; offline workflows provide fallback process guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
