## Description: <br>
Searches Threads posts by keyword or hashtag and returns matching posts with engagement metrics, extracted from SSR-embedded JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to search public Threads posts by keyword or hashtag, choose top or recent ordering, and collect matching post text, URLs, author details, timestamps, and engagement metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads public Threads search-page data through browser automation and may be affected by page redesigns, search index delays, or anti-scraping changes. <br>
Mitigation: Review results for completeness, retry after navigation failures, and follow the artifact guidance to record only unexpected operational notes. <br>
Risk: A local optional memory file may retain operational notes across runs. <br>
Mitigation: Review or periodically clear the memory file when local retention of operational notes is not desired. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/threads-keyword-search) <br>
- [Threads Search Endpoint](https://www.threads.com/search/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON result objects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns public Threads search results with keyword, sort filter, post metadata, engagement metrics, and page information; unauthenticated searches are limited to about 17-18 results and no pagination.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
