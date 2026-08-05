## Description: <br>
Search X, read tweets and their replies and retweeters, pull user profiles and their tweets, replies, media, followers, and followings, and get trending topics as structured JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to retrieve public X search results, tweet details, replies, retweeters, user profiles, user timelines, social graph data, media posts, and country-level trends through Scavio. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can collect public X profiles, replies, followers, followings, and engagement metrics. <br>
Mitigation: Use it for necessary, user-directed searches, avoid broad harvesting without a clear reason, and handle stored or shared social data according to applicable platform, privacy, and legal obligations. <br>
Risk: Pagination can expand collection scope and consume Scavio credits. <br>
Mitigation: Inform the user before paginating through many pages and stop when the returned next_cursor is null or the requested scope is satisfied. <br>
Risk: Social metrics, tweet IDs, handles, or replies could be fabricated if an agent fills gaps without API data. <br>
Mitigation: Return only Scavio API data, preserve engagement metrics as provided, and surface missing or empty results instead of inventing values. <br>


## Reference(s): <br>
- [Scavio X API documentation](https://scavio.dev/docs/x-api) <br>
- [Scavio homepage](https://scavio.dev) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-x) <br>
- [Publisher profile](https://clawhub.ai/user/scavio-ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, API Calls, JSON] <br>
**Output Format:** [Markdown guidance with bash and Python examples; API responses are structured JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY. Paginated endpoints use cursor values and every X endpoint costs 1 credit.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
