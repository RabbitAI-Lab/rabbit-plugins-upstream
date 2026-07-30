## Description: <br>
Get a real Airbnb price quote for a listing and dates, then compare that property against the offers StayingAPI can resolve for it to find the cheapest rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to quote a known Airbnb or lodging listing for specific dates and occupancy, then compare available rates for the same property across supported booking platforms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A live StayingAPI key can expose paid or account-scoped API access if committed to files or logs. <br>
Mitigation: Store live keys in the agent runtime's secret store or another protected credential manager, avoid committing keys to repositories or dotfiles, and rotate any exposed key. <br>
Risk: Sandbox responses are fixture data and may not match the requested listing, dates, or occupancy. <br>
Mitigation: Use sandbox keys only to validate parsing and error handling, and switch to a live key before presenting results as real prices. <br>
Risk: Cross-OTA comparison coverage varies by property and can return one aggregated-lowest offer rather than several platform offers. <br>
Mitigation: Inspect the returned offer count before describing a response as a multi-platform comparison. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI docs](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [API key setup](references/auth-setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/stayingapi/skills/airbnb-prices) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API calls] <br>
**Output Format:** [Markdown with REST and MCP usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a StayingAPI key stored as STAYINGAPI_KEY; sandbox keys return fixture data.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
