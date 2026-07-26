## Description: <br>
Access global customs trade data from 220+ countries to search import-export records by company, HS code, or product and identify buyers, suppliers, and competitor trade activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External trade, sales, and sourcing teams use this skill to find international buyers or suppliers, inspect customs shipment history, enrich company records, and monitor competitor cross-border activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an UpKuaJing API key that may be stored locally. <br>
Mitigation: Protect ~/.upkuajing/.env as a secret file and avoid sharing API-key values in prompts, logs, or support requests. <br>
Risk: Search and enrichment operations can incur paid API charges. <br>
Mitigation: Review fee prompts, expected call counts, pricing information, and account balance before approving searches or enrichment calls. <br>
Risk: Company contact-data retrieval may raise privacy, outreach, or compliance obligations. <br>
Mitigation: Use retrieved emails, phone numbers, social profiles, and websites under applicable privacy, anti-spam, and business-outreach rules. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/upkuajing/skills/upkuajing-customs-trade-company-search) <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Company Detail API Reference](references/company-detail-api.md) <br>
- [Company List API Reference](references/company-list-api.md) <br>
- [Contact Fetch API Reference](references/contact-fetch-api.md) <br>
- [Trade List API Reference](references/trade-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON or JSONL API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search tasks may write JSONL result files and return task IDs, fee information, balances, and file paths.] <br>

## Skill Version(s): <br>
1.0.9 (source: evidence.release.version and SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
