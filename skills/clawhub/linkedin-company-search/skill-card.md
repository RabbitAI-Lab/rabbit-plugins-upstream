## Description: <br>
Search LinkedIn company data through UpKuaJing by company name, industry, size, founding year, geography, and contact availability. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[upkuajing](https://clawhub.ai/user/upkuajing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales teams, marketers, and B2B lead-generation specialists use this skill to discover LinkedIn company profiles, enrich firmographic records, and research target accounts for customer acquisition, market research, competitor analysis, and account-based sales. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkedIn company-search queries and result data are sent to and returned from UpKuaJing's API. <br>
Mitigation: Use the skill only for searches appropriate to share with UpKuaJing, and review saved results for sensitive contact or firmographic data. <br>
Risk: API calls are paid and large searches can trigger multiple billable requests. <br>
Mitigation: Confirm current pricing and expected call count before running large searches or account top-up flows. <br>
Risk: The UpKuaJing API key may be stored locally in plaintext. <br>
Mitigation: Protect the local credential file, avoid sharing it, and remove or rotate the key when it is no longer needed. <br>
Risk: Search results and task metadata can remain in local files after execution. <br>
Mitigation: Delete task output files when they are no longer required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/upkuajing/skills/linkedin-company-search) <br>
- [UpKuaJing homepage](https://www.upkuajing.com) <br>
- [UpKuaJing Open Platform](https://developer.upkuajing.com/) <br>
- [UpKuaJing pricing](https://www.upkuajing.com/web/openapi/price.html) <br>
- [LinkedIn Company List API reference](references/linkedin-company-list-api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Files, Configuration] <br>
**Output Format:** [Markdown guidance with shell commands, JSON command output, and JSONL result files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Python and UPKUAJING_API_KEY; list searches can create local task metadata and result files.] <br>

## Skill Version(s): <br>
1.0.2 (source: server evidence and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
