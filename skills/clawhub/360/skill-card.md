## Description: <br>
360-web-search, also called 360智搜 or 360Aiso, helps agents search Chinese web pages, images, news, and other current information through the 360 search API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tonylwj](https://clawhub.ai/user/tonylwj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve current Chinese-language web, image, news, market, policy, product, and China-related information from 360 search results. It is intended for search tasks that need freshness, source URLs, summaries, and page timing signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation rules may route ordinary Chinese, China-related, freshness, or search-like user queries to 360's third-party API unexpectedly. <br>
Mitigation: Prefer explicit invocations such as asking to use 360 search, and narrow or confirm provider routing before using the skill for sensitive or personal queries. <br>
Risk: Search requests send query text and a UUID session ID to api.360.cn. <br>
Mitigation: Avoid sensitive or personal queries unless the user is comfortable sending that information to the provider. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tonylwj/skills/360) <br>
- [360 AI Open Platform](https://ai.360.com/platform) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown search summaries with source URLs and page times; curl-based API calls are used for execution.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SEARCH_360_API_KEY, curl, and outbound HTTPS access to api.360.cn; each request generates a new sid.] <br>

## Skill Version(s): <br>
1.3.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
