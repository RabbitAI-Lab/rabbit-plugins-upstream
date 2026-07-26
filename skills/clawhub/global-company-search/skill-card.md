## Description: <br>
Search global companies by name, industry, product, and website URL, and gather firmographic data for supplier research and overseas lead generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, sales teams, exporters, and B2B lead generation specialists use this skill to find companies, research target markets, source suppliers, and enrich firmographic records through the UpKuaJing global company database. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid API calls can incur costs, especially for larger company searches. <br>
Mitigation: Check current pricing and obtain explicit user confirmation before fee-incurring searches or top-ups. <br>
Risk: The UpKuaJing API key may be stored locally in ~/.upkuajing/.env. <br>
Mitigation: Protect the .env file, avoid exposing the key in logs or shared output, and rotate the key if it is disclosed. <br>
Risk: Company results may include contact-related firmographic data used for lead generation. <br>
Mitigation: Use contact-data filters only for outreach that complies with applicable privacy, consent, and anti-spam requirements. <br>
Risk: Search results are saved locally as JSONL task output files. <br>
Mitigation: Restrict access to exported result files and delete them when they are no longer needed. <br>


## Reference(s): <br>
- [Global Company List API](references/global-company-list-api.md) <br>
- [UpKuaJing](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing OpenAPI Pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [ClawHub Global Company Search](https://clawhub.ai/upkuajing/skills/global-company-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; scripts return JSON and save company records as JSONL files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large searches may require multiple paid API calls and create local JSONL result files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
