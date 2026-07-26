## Description: <br>
Search Google via SerpAPI (Google Search, Google News, Google Local). Use when you need to search the web, find news articles, or look up local businesses. Supports country/language targeting for region-specific results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericsantos](https://clawhub.ai/user/ericsantos) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve Google web, news, and local results through SerpAPI with country, language, location, result-count, and raw JSON options. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a SerpAPI key. <br>
Mitigation: Prefer an environment variable or managed secret store over a plaintext config file, monitor SerpAPI usage or billing, and rotate the key if trust changes. <br>
Risk: Search terms are sent to SerpAPI. <br>
Mitigation: Avoid sensitive queries and review whether external search disclosure is appropriate for the use case. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ericsantos/skills/serpapi-search) <br>
- [SerpAPI search endpoint](https://serpapi.com/search.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, configuration] <br>
**Output Format:** [Plain text search results or raw JSON from SerpAPI, with shell command examples and API key configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, python3, and a SERPAPI_API_KEY credential.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
