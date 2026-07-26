## Description: <br>
Searches LinkedIn professional records through the UpKuaJing Open Platform API using filters such as name, company, job title, industry, country, and contact-signal availability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External recruiters, sales teams, and B2B lead-generation users can use this skill to find people in LinkedIn data by company, role, industry, geography, and contact-signal filters. It supports candidate sourcing, headhunting, lead discovery, and profile-result collection through a paid third-party API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid third-party API and searches can incur charges. <br>
Mitigation: Confirm pricing and expected call count before execution, especially when query_count exceeds one result page. <br>
Risk: The UpKuaJing API key may be stored in a local plaintext dotfile. <br>
Mitigation: Prefer an environment variable when possible, restrict local file access, and remove the key when it is no longer needed. <br>
Risk: Returned profile results are retained on disk. <br>
Mitigation: Delete local task data and logs when retention is no longer necessary. <br>
Risk: The skill can support broad contact-data enrichment. <br>
Mitigation: Use only authorized, purpose-limited searches and avoid broad collection that does not meet privacy, legal, or organizational requirements. <br>


## Reference(s): <br>
- [LinkedIn Person List API reference](references/linkedin-person-list-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-person-search) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing API pricing](https://www.upkuajing.com/web/openapi/price.html) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON status output, and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires UPKUAJING_API_KEY; API calls are billable; search results are persisted locally by task ID.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
