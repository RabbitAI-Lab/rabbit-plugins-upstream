## Description: <br>
Advanced AI-powered search skill using SearXNG as a universal search backend for multi-engine query orchestration, dork generation, and result analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[welove111](https://clawhub.ai/user/welove111) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and authorized security or OSINT practitioners use this skill to send natural-language or dork-style search tasks through a configured SearXNG instance and receive ranked, deduplicated, LLM-ready search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill automates sensitive reconnaissance and public-secret discovery without built-in scope controls. <br>
Mitigation: Use only for authorized security research or OSINT on public data, and restrict searches to domains or targets the operator owns or has explicit permission to assess. <br>
Risk: Search queries are sent to the configured SearXNG instance and may be forwarded to third-party search engines. <br>
Mitigation: Use a trusted SearXNG instance and avoid submitting sensitive, confidential, personal, credential, or internal target data without informed consent and authorization. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/welove111/skills/search-intelligence-skill) <br>
- [Publisher profile](https://clawhub.ai/user/welove111) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown or structured text containing ranked search results, source URLs, summaries, generated queries, and integration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a configured SearXNG instance; output may include network-derived public search results and generated dork queries.] <br>

## Skill Version(s): <br>
0.2.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
