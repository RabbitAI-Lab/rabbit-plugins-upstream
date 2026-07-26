## Description: <br>
Search Airbnb listings by location, dates, price, beds, capacity, and host attributes via StayingAPI.com, including superhost, instant-book, and luxury presets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nikhonit](https://clawhub.ai/user/nikhonit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill when they explicitly need to search Airbnb-style stays by location, travel dates, guest mix, price range, and listing attributes through StayingAPI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Travel search criteria, such as location, dates, guest counts, and listing preferences, are sent to StayingAPI. <br>
Mitigation: Use the skill only when the user is comfortable sharing those details with StayingAPI, and avoid entering unusually sensitive itinerary details. <br>
Risk: The skill requires a StayingAPI key and successful searches may consume credits per listing returned. <br>
Mitigation: Use a dedicated low-privilege API key where possible, keep STAYINGAPI_KEY out of prompts and logs, and cap max_items for broad searches. <br>


## Reference(s): <br>
- [StayingAPI Homepage](https://stayingapi.com) <br>
- [StayingAPI OpenAPI Spec](https://stayingapi.com/openapi.json) <br>
- [StayingAPI Hosted MCP Server](https://api.stayingapi.com/mcp) <br>
- [ClawHub Skill Page](https://clawhub.ai/nikhonit/skills/airbnb-search) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Configuration] <br>
**Output Format:** [JSON-compatible Python dictionaries containing listing results, metadata, request IDs, async job envelopes, or error details.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires STAYINGAPI_KEY. Search calls can consume one StayingAPI credit per listing returned, so max_items should be capped for broad queries.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
