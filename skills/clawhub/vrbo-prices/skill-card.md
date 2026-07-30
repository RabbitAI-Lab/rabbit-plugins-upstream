## Description: <br>
Get a real Vrbo price quote for a listing and dates, then compare that property against the offers StayingAPI can resolve for it to find the cheapest rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to quote a specific Vrbo listing for requested dates and occupancy, then compare resolved offers to identify the lowest available rate. It is suited to price checks and cross-OTA comparisons, not broad lodging search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends listing URLs, dates, occupancy, and property details to StayingAPI for quote and comparison requests. <br>
Mitigation: Use the skill only when the user is comfortable sharing those travel details with StayingAPI. <br>
Risk: A live StayingAPI key can consume credits for successful live API usage. <br>
Mitigation: Use a sandbox key for evaluation and store live keys only in an appropriate environment variable or agent secret store. <br>


## Reference(s): <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [Auth setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with price summaries, API result interpretation, and optional shell commands for setup or verification] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a StayingAPI key and internet access to StayingAPI; live calls may consume credits.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
