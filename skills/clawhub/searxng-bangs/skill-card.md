## Description: <br>
Privacy-respecting web search via SearXNG with DuckDuckGo-style bangs support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rpeters511](https://clawhub.ai/user/rpeters511) <br>

### License/Terms of Use: <br>
CC0 <br>


## Use Case: <br>
Developers and agent users use this skill to run privacy-focused web, news, image, video, science, and direct bang searches through a configured SearXNG instance. It is useful when search privacy, multi-engine aggregation, or avoiding API keys is more important than a hosted search API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the configured SearXNG endpoint, so an untrusted public instance could observe queries or apply rate limits. <br>
Mitigation: Use a trusted HTTPS SearXNG instance, prefer self-hosting for sensitive searches, and avoid sensitive queries on unknown public instances. <br>
Risk: Using a floating SearXNG Docker image can make installs less reproducible over time. <br>
Mitigation: Pin the SearXNG Docker image version or digest for repeatable deployments. <br>


## Reference(s): <br>
- [SearXNG API Reference](references/api.md) <br>
- [SearXNG Installation Guide](https://docs.searxng.org/admin/installation.html) <br>
- [SearXNG Public Instances](https://searx.space) <br>
- [ClawHub Skill Page](https://clawhub.ai/rpeters511/skills/searxng-bangs) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [JSON search results and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include query, number_of_results, and result objects with url, title, and content fields.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
