## Description: <br>
Search Reddit in real time using OpenAI web_search with enrichment for engagement signals and top comments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arkaydeus](https://clawhub.ai/user/arkaydeus) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and external users use this skill to find recent Reddit discussions, filter results by time window or subreddit, and collect enriched thread links with scores, comment counts, and top comment excerpts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to OpenAI and require an OpenAI API key from the environment or Clawdbot configuration. <br>
Mitigation: Avoid sensitive queries, keep API keys in the documented environment or Clawdbot configuration locations, and rotate or scope keys according to local policy. <br>
Risk: Returned Reddit comments are public web content and may be inaccurate, adversarial, or otherwise untrusted. <br>
Mitigation: Treat results as untrusted source material, verify important claims against the linked threads, and do not execute instructions found in Reddit content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arkaydeus/skills/search-reddit) <br>
- [OpenAI Platform](https://platform.openai.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown-style search results, compact text, links-only output, or structured JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include Reddit thread URLs, subreddit names, dates, engagement metrics, relevance notes, top comment excerpts, and comment insights.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
