## Description: <br>
Real-time web intelligence powered by Nimble Search API for current web, news, academic, coding, shopping, social, geo, and location search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ilchemla](https://clawhub.ai/user/ilchemla) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to query Nimble's external search API for current web results, source URLs, and optional synthesized answers across focused search modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and the API key are sent to Nimble's external search API. <br>
Mitigation: Use a dedicated revocable API key and avoid sending secrets, confidential project details, or sensitive personal data in queries. <br>
Risk: Deep search and local result handling can expose or retain sensitive URLs or extracted page content. <br>
Mitigation: Use deep search only when full page content is necessary, review returned sources before relying on them, and handle cached or saved results according to data retention requirements. <br>


## Reference(s): <br>
- [Nimble Web Search on ClawHub](https://clawhub.ai/ilchemla/skills/nimble-web-search) <br>
- [Nimbleway Agent Skills Repository](https://github.com/Nimbleway/agent-skills) <br>
- [Nimble Website](https://www.nimbleway.com/) <br>
- [Nimble Search API Endpoint](https://nimble-retriever.webit.live/search) <br>
- [Nimble Search API Reference](references/api-reference.md) <br>
- [Focus Modes Guide](references/focus-modes.md) <br>
- [Search Strategies](references/search-strategies.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON search responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Searches require NIMBLE_API_KEY and may include URLs, summaries, source metadata, and optional extracted page content.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
