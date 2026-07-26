## Description: <br>
Unified search API across Google, Amazon, Yelp, OpenTable, Walmart, and more. Use when searching for products, local businesses, restaurants, shopping, images, news, or any web search. One API key, many engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ianpcook](https://clawhub.ai/user/ianpcook) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to run web, local, shopping, news, image, and product searches through SerpAPI from a CLI wrapper, returning structured JSON or readable summaries for downstream use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms and any provided or inferred location are sent to SerpAPI. <br>
Mitigation: Avoid sensitive personal queries, set location explicitly for location-sensitive searches, and use the skill only when sending that data to SerpAPI is acceptable. <br>
Risk: The skill requires SERPAPI_API_KEY for API access. <br>
Mitigation: Manage the key as a secret, keep it out of prompts and logs, and scope or rotate it according to the user's SerpAPI account controls. <br>


## Reference(s): <br>
- [SerpAPI homepage](https://serpapi.com) <br>
- [ClawHub SerpAPI skill](https://clawhub.ai/ianpcook/skills/serpapi) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [JSON or plain text emitted by a CLI command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SERPAPI_API_KEY and may use query, engine, location, result count, page, country, and language options.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
