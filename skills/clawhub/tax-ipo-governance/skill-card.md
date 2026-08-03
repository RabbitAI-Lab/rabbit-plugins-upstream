## Description: <br>
拟上市企业上市前三年财税规范与内部控制建设框架专项助手，覆盖上市前时间轴、股改涉税、内控建设、高发缺陷整改、关联交易清理、收入确认和相关自检报告场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Finance, tax, compliance, and IPO-readiness teams use this skill to reason through pre-listing tax normalization, internal control buildout, risk self-checks, and remediation planning. It is also relevant for advisers such as securities firms, accountants, and tax professionals supporting companies preparing for an IPO. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive IPO, finance, legal, or tax details may be sent to external cloud services during Q&A, risk checks, web self-checks, calculations, or fallback searches. <br>
Mitigation: Use only approved endpoints and retention terms, avoid entering material nonpublic information, and route sensitive matters through reviewed internal workflows. <br>
Risk: The skill can create persistent identifiers, API keys, caches, and logs in local client storage or browser localStorage. <br>
Mitigation: Inspect and manage ~/.tax-policy-client and browser localStorage after use; rotate or remove stored credentials when the skill is no longer approved. <br>
Risk: MCP client configuration can be modified when automatic setup is intentionally enabled. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP disabled unless configuration changes are intended, and review any MCP config changes before using the skill in sensitive environments. <br>
Risk: Tax and IPO guidance can become outdated or require licensed professional judgment. <br>
Mitigation: Validate conclusions against current law, regulator positions, and qualified tax, accounting, or legal advisers before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-governance) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [Interactive IPO governance self-check workflow](https://mcp.aitaxs.top/web/topic_workflow_ipo_governance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Related comprehensive tax knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Related IPO tax compliance skill](https://skillhub.cn/skills/tax-ipo-tax) <br>
- [Related equity incentive and employee holding platform skill](https://skillhub.cn/skills/tax-esop-platform) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured checklists, risk summaries, policy references, code snippets, shell commands, and configuration instructions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call remote tax-policy tools for Q&A, risk checks, calculations, and knowledge-base listings; includes offline fallback scripts and a browser self-check workflow.] <br>

## Skill Version(s): <br>
3.15.8 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
