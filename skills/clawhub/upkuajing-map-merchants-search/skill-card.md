## Description: <br>
Pull bulk Google Maps business data with radius-based filters, gather merchant contact information, analyze market density, and find distributors or overseas buyers for offline business expansion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, distribution, brand operations, and regional expansion teams use this skill to search UpKuaJing map merchant data by geography, radius, industry, keywords, and contact filters. It helps collect business leads, plan territories, compare local market density, and identify potential distributors or overseas buyers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an UpKuaJing API key and may store it in a local ~/.upkuajing/.env file. <br>
Mitigation: Keep the API key private, restrict access to ~/.upkuajing, and remove or rotate the key when it is no longer needed. <br>
Risk: Merchant search requests contact UpKuaJing servers and can incur usage fees for larger result counts. <br>
Mitigation: Review pricing before large searches and require explicit user confirmation before paid searches that exceed the documented threshold. <br>
Risk: Search results can contain business contact and location data that is written to local JSONL files. <br>
Mitigation: Store exported lead data only where authorized, limit sharing to approved workflows, and delete result files when they are no longer needed. <br>


## Reference(s): <br>
- [UpKuaJing Homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [Detailed Price Description](https://www.upkuajing.com/web/openapi/price.html) <br>
- [Merchants Search API](references/merchants-search-api.md) <br>
- [Country List API](references/country-list-api.md) <br>
- [Province List API](references/province-list-api.md) <br>
- [City List API](references/city-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples, JSON API responses, and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python, httpx, and UPKUAJING_API_KEY for paid merchant search; stores task metadata and result files locally under the skill task_data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
