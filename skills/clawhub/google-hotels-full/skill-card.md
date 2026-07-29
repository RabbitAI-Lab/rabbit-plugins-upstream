## Description: <br>
Google Hotels - complete toolkit helps an agent search Google Hotels, check availability, quote prices, and compare cross-OTA offers through StayingAPI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[stayingapi](https://clawhub.ai/user/stayingapi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use this skill when an agent needs Google Hotels search, availability checks, price quotes, or cross-OTA price comparison using a StayingAPI key. It is not suitable for Google Hotels listing-detail or reviews workflows, which the evidence says are not supported for this platform. <br>

### Deployment Geography for Use: <br>
Use in regions where the user is permitted to access StayingAPI and Google Hotels data, subject to the user's local travel, privacy, and API compliance requirements. <br>

## Known Risks and Mitigations: <br>
Risk: The required StayingAPI key is a sensitive credential. <br>
Mitigation: Use a sandbox key for testing, store live keys in a secure runtime secret store when possible, and avoid placing keys in synced dotfiles, logs, or repositories. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/stayingapi/skills/google-hotels-full) <br>
- [StayingAPI homepage](https://stayingapi.com) <br>
- [StayingAPI documentation](https://stayingapi.com/docs) <br>
- [StayingAPI OpenAPI contract](https://api.stayingapi.com/openapi.json) <br>
- [StayingAPI pricing](https://stayingapi.com/pricing) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text] <br>
**Output Format:** [Markdown instructions, REST or MCP request guidance, environment variable setup commands, and response-handling notes.] <br>
**Output Parameters:** [Location, dates, occupancy, Google platform selection, listing identifiers or URLs, property names, Google hotel IDs, and the STAYINGAPI_KEY credential.] <br>
**Other Properties Related to Output:** [The skill expects internet access to api.stayingapi.com or the hosted MCP endpoint and distinguishes sandbox fixture keys from live data keys. Google Hotels listing-detail and reviews endpoints are outside its supported scope.] <br>

## Skill Version(s): <br>
1.1.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
