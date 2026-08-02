## Description: <br>
China Tax Guidance helps users obtain practical China tax filing workflows, required materials, filing reminders, invoice guidance, tax risk checks, and compliance report guidance for electronic tax bureau scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zxj2devs](https://clawhub.ai/user/zxj2devs) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External business tax staff, finance teams, and individual taxpayers use this skill to ask China tax process questions, prepare filing checklists, understand invoice and declaration paths, and perform preliminary compliance self-checks. It supports guidance and triage, but users remain responsible for confirming final filing actions with the relevant tax authority or a qualified professional. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Tax questions and scenarios may be sent to the remote mcp.aitaxs.top service. <br>
Mitigation: Do not enter taxpayer IDs, bank details, confidential filings, or other sensitive tax data unless the service provider and privacy terms are acceptable. <br>
Risk: Fallback queries may be sent to public search services such as Bing or Baidu when the remote service is unavailable. <br>
Mitigation: Treat fallback results as preliminary guidance and verify important conclusions against official tax authority sources or qualified professional advice. <br>
Risk: The skill may store local credentials, cache, health data, or logs under ~/.tax-policy-client. <br>
Mitigation: Review local storage policies before deployment and clear that directory when removing the skill or rotating credentials. <br>
Risk: Optional automatic setup can modify MCP client configuration. <br>
Mitigation: Keep TAX_ENABLE_AUTOSETUP unset unless you intentionally want client configuration changes and have reviewed the target MCP configuration. <br>
Risk: Security evidence marks the release for Review due to under-disclosed remote sharing, storage, fallback search, and configuration behavior. <br>
Mitigation: Complete human review before broad deployment and make those behaviors visible to users who may submit tax or filing information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zxj2devs/skills/china-tax-guidance) <br>
- [Tax compliance path self-check page](https://mcp.aitaxs.top/web/topic_workflow_china_tax_guidance.html) <br>
- [Tax compliance self-check portal](https://mcp.aitaxs.top/web/index_topic_pages.html) <br>
- [Tax policy knowledge skill](https://skillhub.cn/skills/tax-policy-knowledge) <br>
- [Tax invoice compliance skill](https://skillhub.cn/skills/tax-invoice-compliance) <br>
- [VAT law implementation skill](https://skillhub.cn/skills/tax-vat-law) <br>
- [Tax judicial cases skill](https://skillhub.cn/skills/tax-tax-judicial) <br>
- [Social insurance tax compliance skill](https://skillhub.cn/skills/tax-social-insurance) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON-like tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include filing paths, required-material checklists, risk summaries, calculation results, compliance report guidance, and offline fallback guidance.] <br>

## Skill Version(s): <br>
3.15.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
