## Description: <br>
Search Korean news articles using Naver Search API. Use when searching for Korean news, getting latest news updates, finding news about specific topics, or preparing daily news summaries. Supports relevance and date-based sorting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steamb23](https://clawhub.ai/user/steamb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw agents use this skill to search, filter, and collect Korean news articles from Naver News for daily summaries, topic monitoring, breaking-news alerts, and custom news feeds. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires Naver developer credentials and sends news search terms to Naver. <br>
Mitigation: Store NAVER_CLIENT_ID and NAVER_CLIENT_SECRET in environment configuration or a secret store, avoid committing secrets or placing them in prompts, and avoid sending sensitive search terms unless that data sharing is acceptable. <br>
Risk: Automated pagination and recurring news workflows can consume Naver API quota. <br>
Mitigation: Use display, min-results, and max-pages limits deliberately, and monitor usage against the documented daily API-call limit. <br>


## Reference(s): <br>
- [Naver News Search API documentation](https://developers.naver.com/docs/serviceapi/search/news/news.md) <br>
- [Naver developer portal](https://developers.naver.com/) <br>
- [Local Naver News API reference](references/api.md) <br>
- [Daily news summary workflow example](examples/daily-summary.md) <br>
- [ClawHub skill page](https://clawhub.ai/steamb23/skills/naver-news) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, code, guidance] <br>
**Output Format:** [Formatted terminal text or JSON from the Python search helper, with Markdown guidance and examples in the skill documentation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 plus NAVER_CLIENT_ID and NAVER_CLIENT_SECRET environment variables; supports display, start, sort, after, min-results, max-pages, and json options.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
