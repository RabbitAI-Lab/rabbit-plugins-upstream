## Description: <br>
Company Search WDY helps agents query WenDaoYun company information APIs for basic company data, operating details, financial information, public opinion signals, and risk indicators. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rose-develop](https://clawhub.ai/user/rose-develop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to look up company records and risk-related data through WenDaoYun. The skill first searches for matching companies, waits for the user to confirm the selected company, and then routes the requested detail lookup to the relevant API interface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The WenDaoYun API key is sensitive and may be exposed if pasted into prompts, shared logs, or unprotected configuration. <br>
Mitigation: Store WENDAOYUN_API_KEY as an environment variable, avoid displaying it in agent responses, and revoke the key in the WenDaoYun platform if exposure is suspected. <br>
Risk: Company names, identifiers, and lookup intent may be sent to the external WenDaoYun API. <br>
Mitigation: Use the skill only when WenDaoYun's pricing, privacy terms, and data handling are acceptable for the queried company information. <br>
Risk: A fuzzy search can return multiple companies, and querying details for the wrong entity can produce misleading results. <br>
Mitigation: Show the first search results and wait for explicit user confirmation of the selected company before requesting detailed records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rose-develop/skills/company-wdy) <br>
- [WenDaoYun Open Platform](https://open.wintaocloud.com/home) <br>
- [WenDaoYun API invoke endpoint](https://h5.wintaocloud.com/prod-api/api/invoke) <br>
- [Skill usage and routing instructions](artifact/SKILL.md) <br>
- [Company fuzzy search API reference](artifact/references/fuzzy-search-org.md) <br>
- [Company risk API reference](artifact/references/get-risk.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown or plain text with optional shell command snippets and structured company information summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WENDAOYUN_API_KEY and waits for user confirmation before detailed company lookups.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
