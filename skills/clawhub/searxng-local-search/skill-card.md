## Description: <br>
Search the web using SearXNG. Use when you need current information, research topics, find documentation, verify facts, or look up anything beyond your knowledge. Returns ranked results with titles, URLs, and content snippets. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noblepayne](https://clawhub.ai/user/noblepayne) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to query a configured self-hosted SearXNG instance for current information, documentation, fact checks, URLs, and technical references. It supports category, time range, language, and result-count options and returns ranked search result summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to the configured SearXNG server and may expose sensitive or private information. <br>
Mitigation: Use only trusted SearXNG instances and avoid submitting secrets, private data, or confidential internal information as search queries. <br>
Risk: The documented search script is referenced but not included in the artifact. <br>
Mitigation: Verify any separately supplied search script before running it. <br>


## Reference(s): <br>
- [SearXNG API Reference](artifact/references/api-guide.md) <br>
- [SearXNG Documentation](https://docs.searxng.org/) <br>
- [SearXNG GitHub](https://github.com/searxng/searxng) <br>
- [SearXNG Search API Documentation](https://docs.searxng.org/dev/search_api.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/noblepayne/skills/searxng-local-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Formatted plain text search results with titles, URLs, snippets, scores, and engines] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires babashka via the bb command and a configured SEARXNG_URL; supports category, time_range, language, and num_results options.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
