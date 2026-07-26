## Description: <br>
依托全球企业数据库，通过产品品类、所属行业、企业规模筛选目标公司，助力外贸从业者挖掘潜在客户、优质供应商以及长期合作伙伴。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Exporters, sales teams, B2B lead builders, and market researchers use this skill to search a global company database by product, industry, company name, geography, contact availability, or URL. It helps agents discover prospects, suppliers, and target-market companies while producing structured company-search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reads the third-party API key from ~/.upkuajing/.env. <br>
Mitigation: Confirm only whether the key exists, avoid printing it, and restrict local file permissions for the credential file. <br>
Risk: API calls are paid and recharge flows can create payment links. <br>
Mitigation: Before any paid operation or recharge action, disclose the expected action and wait for the user's explicit confirmation in a separate message. <br>
Risk: Search results can include business contact data. <br>
Mitigation: Use returned contact data only under applicable privacy, marketing, anti-spam, and platform rules. <br>


## Reference(s): <br>
- [全球企业库公司列表 API](references/global-company-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/global-company-search-zh) <br>
- [Upkuajing homepage](https://www.upkuajing.com) <br>
- [Upkuajing developer platform](https://developer.upkuajing.com/) <br>
- [OpenAPI pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance, shell commands, JSON summaries, and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Company search results are written under task_data as JSONL files; API responses include task identifiers, status, counts, file paths, and fee information.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
