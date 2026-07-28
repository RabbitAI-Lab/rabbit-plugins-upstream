## Description: <br>
上市审核税务合规专项助手，聚焦税收优惠依赖与可持续性红线、税收优惠披露要求、红筹架构完税凭证级核查、北交所全链条实质合规监管，提供结构化上市税务合规自检与全链路闭环实操，覆盖筹备期体检、优惠论证、研发加计、红筹完税、申报披露和审核回复全流程。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and tax/compliance practitioners use this skill to ask IPO tax compliance questions, run structured self-checks, identify tax preference, red-chip, R&D deduction, and disclosure risks, and prepare practical remediation or review steps. It is guidance-oriented and does not replace licensed tax, legal, or listing advisory work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions, self-check metrics, or compliance scenarios may be sent to a third-party cloud tax service. <br>
Mitigation: Review the operator, endpoint, and retention terms before use; avoid entering highly sensitive IPO, corporate, or personal tax data unless those terms are acceptable. <br>
Risk: The skill may store API credentials, client identifiers, cache data, or logs locally. <br>
Mitigation: Inspect local configuration and data directories, rotate or remove credentials when no longer needed, and avoid shared-machine use for sensitive matters. <br>
Risk: Optional setup and installer flows may modify MCP or client configuration and install related skills. <br>
Mitigation: Run setup or matrix installation only after reviewing the target configuration changes, and prefer dry-run or manual review before applying changes. <br>
Risk: Tax guidance can be incomplete or outdated for a specific listing, regulator, or fact pattern. <br>
Mitigation: Use outputs as decision support only and confirm material IPO tax, legal, and disclosure positions with qualified professionals and official sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/tax-ipo-tax) <br>
- [Publisher profile](https://clawhub.ai/user/zxj2devs) <br>
- [IPO tax compliance self-check page](https://mcp.aitaxs.top/web/topic_workflow_ipo_tax.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Comprehensive tax policy knowledge base](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Listed company lifecycle advisory skill](https://skillhub.cn/skills/tax-listed-advisory) <br>
- [Tax incentives skill](https://skillhub.cn/skills/tax-incentives) <br>
- [Tax restructuring skill](https://skillhub.cn/skills/tax-restructuring) <br>
- [Tax data asset skill](https://skillhub.cn/skills/tax-data-asset) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Shell commands, Configuration] <br>
**Output Format:** [Markdown and text guidance with optional code or shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call a third-party cloud tax service, provide a web self-check link, and offer offline workflow guidance when the cloud service is unavailable.] <br>

## Skill Version(s): <br>
3.15.3 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
