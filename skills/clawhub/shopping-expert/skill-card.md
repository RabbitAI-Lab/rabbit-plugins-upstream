## Description: <br>
Shopping Expert helps agents find and compare online and local products using budget, preferences, availability, ratings, links, and store-location signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[udiedrichsen](https://clawhub.ai/user/udiedrichsen) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and shopping agents use this skill to compare products, find deals, and locate nearby stores with budget and preference filters. It is suitable when the user wants a ranked shopping list with links or directions, while understanding that queries and provided locations are sent to SerpAPI and Google Places. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/udiedrichsen/skills/shopping-expert) <br>
- [Publisher profile](https://clawhub.ai/user/udiedrichsen) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown shopping table by default, or structured JSON when requested.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires uv and SERPAPI_API_KEY for online search; local and hybrid searches also require GOOGLE_PLACES_API_KEY. Prices, availability, and store information depend on third-party API freshness and quotas.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
