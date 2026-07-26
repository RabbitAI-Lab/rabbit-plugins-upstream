## Description: <br>
Searches CreatorDB for YouTube creators and retrieves profile, content, sponsorship, audience, and performance information. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[poi5305](https://clawhub.ai/user/poi5305) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to call CreatorDB's YouTube API with a user-provided API key and inspect creator search results, channel profiles, audience demographics, sponsorship details, content records, and performance metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated CreatorDB requests send YouTube lookup terms and channel identifiers to a third-party API. <br>
Mitigation: Use a dedicated CreatorDB API key, avoid sensitive private search terms, and confirm that CreatorDB use is appropriate for the intended workflow. <br>
Risk: CreatorDB API usage can consume quota or incur account billing. <br>
Mitigation: Monitor CreatorDB quota and billing for the API key used by the agent. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/poi5305/skills/creatordb-youtube-v3) <br>
- [CreatorDB homepage](https://www.creatordb.app) <br>
- [CreatorDB YouTube search endpoint](https://apiv3.creatordb.app/youtube/search) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, API Calls, JSON, Guidance] <br>
**Output Format:** [Markdown with curl commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and CREATORDB_API_KEY; API responses may consume CreatorDB quota.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
