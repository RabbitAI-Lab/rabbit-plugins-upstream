## Description: <br>
税收优惠与资质认定专业助手，帮助企业梳理高新技术企业、研发费用加计扣除、西部大开发、专精特新等优惠条件、测算口径和合规风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, and compliance users use this skill to evaluate China-focused tax incentive eligibility, prepare self-checks, and identify documentation or filing risks before relying on a benefit. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, metrics, or fallback search queries may leave the local environment through mcp.aitaxs.top or public search engines. <br>
Mitigation: Review endpoint use before installation, avoid submitting confidential taxpayer data, and prefer offline fallback materials for sensitive scenarios. <br>
Risk: Local files may store API credentials, cache data, health records, or question logs. <br>
Mitigation: Inspect the local data directory and logs, restrict file permissions, remove sensitive history, and rotate any exposed credentials. <br>
Risk: Setup behavior can alter AI-client MCP configuration when explicitly enabled. <br>
Mitigation: Run setup in dry-run mode first, review configuration changes and backups, and enable write mode only after approval. <br>
Risk: Tax guidance may be incomplete, time-sensitive, or not applicable to a specific business fact pattern. <br>
Mitigation: Confirm material conclusions against current official policy and a qualified tax professional or主管税务机关 before filing or claiming incentives. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-incentives) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Tax incentive self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_incentives.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown and text responses with checklist-style analysis, optional MCP tool calls, and configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May provide offline fallback guidance; does not complete filings, act as a licensed tax representative, or guarantee final eligibility.] <br>

## Skill Version(s): <br>
3.15.6 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
