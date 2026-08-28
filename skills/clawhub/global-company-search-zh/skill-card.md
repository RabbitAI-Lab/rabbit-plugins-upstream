## Description:

依托全球企业数据库，通过产品品类、所属行业、企业规模筛选目标公司，助力外贸从业者挖掘潜在客户、优质供应商以及长期合作伙伴。

This skill is ready for commercial/non-commercial use.

## Publisher:

[upkuajing](https://clawhub.ai/user/upkuajing)

### License/Terms of Use:

MIT-0

## Use Case:

External export, sales, B2B lead generation, market research, and supplier sourcing users can search global company records by product, industry, company name, website URL, geography, and contact-data filters. The skill helps agents find target companies, enrich company profiles, and continue larger searches through task files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A paid Upkuajing API key may be stored in plaintext at ~/.upkuajing/.env.

Mitigation: Use a dedicated, scoped API key where possible, restrict local file access, rotate the key if exposed, and avoid sharing the .env file.

Risk: The skill contacts Upkuajing for searches, account actions, version checks, and user-approved error reports.

Mitigation: Review these remote calls before installation and run paid or reporting actions only after explicit user confirmation.

Risk: Search results and error reports can involve contact data, request parameters, or response details.

Mitigation: Avoid sending raw secrets, unnecessary personal data, or full payload dumps, and use returned contact data only with a lawful and appropriate basis.

## Reference(s):

- [Global Company List API Reference](artifact/references/global-company-list-api.md)
- [Skill Error Report API Reference](artifact/references/skill-error-report-api.md)
- [Upkuajing Homepage](https://www.upkuajing.com)
- [Upkuajing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html)
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/global-company-search-zh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, files, guidance]

**Output Format:** [Markdown guidance with shell commands; scripts emit JSON summaries and JSONL task result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search operations can create local task_data files and may incur paid API calls. Query count is limited to 20-1000 records per run.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
