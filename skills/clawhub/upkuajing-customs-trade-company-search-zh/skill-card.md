## Description: <br>
调取真实可靠的全球海关进出口记录，挖掘各行各业的进口商、出口商与采购商；可依托产品品类及原产国筛选目标企业、海外采购客户和优质供应商，助力外贸人员精准开发全球合作伙伴。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade, sales, and sourcing teams use this skill to search customs trade records, find buyers and suppliers, inspect company trade activity, and enrich selected companies with profile or contact information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores the Upkuajing API key in a plaintext home-directory file. <br>
Mitigation: Do not display or share ~/.upkuajing/.env, and restrict the file permissions manually after installation. <br>
Risk: API calls can charge the user's Upkuajing API balance. <br>
Mitigation: Confirm fee-bearing actions before execution and use the pricing command or pricing page for current costs. <br>
Risk: The skill can retrieve business contact data. <br>
Mitigation: Use contact-data features only where the intended outreach complies with applicable privacy and business communication rules. <br>
Risk: Search results are written locally as JSONL task output files. <br>
Mitigation: Review result files before sharing and handle downloaded trade or contact data according to the user's data-handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/upkuajing-customs-trade-company-search-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [Upkuajing OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Trade list API reference](references/trade-list-api.md) <br>
- [Company list API reference](references/company-list-api.md) <br>
- [Company detail API reference](references/company-detail-api.md) <br>
- [Contact fetch API reference](references/contact-fetch-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, API calls, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON API responses, and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [List searches write task metadata and result JSONL files under the skill task_data directory; detail and contact lookups print JSON responses with fee information.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence release.version and SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
