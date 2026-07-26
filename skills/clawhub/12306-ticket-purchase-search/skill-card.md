## Description: <br>
A Model Context Protocol (MCP) skill that helps agents search 12306 train-ticket information, including station codes, ticket availability, transfer options, and route stops. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to look up China Railway 12306 station codes, ticket availability, transfer options, and route stop details through the XiaoBenYang MCP API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes external API calls to the XiaoBenYang MCP service. <br>
Mitigation: Install only if external API calls are acceptable for the intended environment, and review returned ticket data before using it for automated actions. <br>
Risk: The skill stores XBY_APIKEY in a local plaintext .env file. <br>
Mitigation: Use a disposable or low-privilege API key when possible, keep .env out of version control, and rotate the key if exposure is suspected. <br>
Risk: Security evidence notes documentation inconsistencies. <br>
Mitigation: Review the setup documentation and test the expected query flow before relying on the skill for automated travel planning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/12306-ticket-purchase-search) <br>
- [XiaoBenYang API key site](https://xiaobenyang.com) <br>
- [XiaoBenYang MCP API endpoint](https://mcp.xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, API Calls, Guidance] <br>
**Output Format:** [Text or JSON summaries derived from API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires XBY_APIKEY and station/date parameters for ticket queries.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
