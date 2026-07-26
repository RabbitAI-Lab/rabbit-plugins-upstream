## Description: <br>
Search Google News for headlines by keyword, topic, or publication as structured JSON: headline, source, date, and link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agents use this skill to retrieve fresh Google News headlines for current events, media monitoring, news research, and source-linked summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an API key and gives the agent access to a paid external API. <br>
Mitigation: Use a least-privilege SCAVIO_API_KEY, keep it in the environment rather than prompts, and inform users before broad pagination because each request costs 1 credit. <br>
Risk: News results may be time-sensitive, incomplete, cached, or temporarily unavailable from the upstream service. <br>
Mitigation: Use the API for current news, return only data received from the API, cite source links, and retry or broaden queries according to the documented failure handling. <br>


## Reference(s): <br>
- [Scavio Google News documentation](https://scavio.dev/docs/google-news) <br>
- [Scavio rate limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-google-news) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [Structured JSON responses with headline, source, date, link, response timing, credit usage, and cache status.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; each request costs 1 credit; agents should cite returned news sources and links.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
