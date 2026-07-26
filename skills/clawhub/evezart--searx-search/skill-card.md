## Description: <br>
Query a local SearXNG instance for privacy-focused web searches, returning JSON results with customizable categories, languages, engines, and pagination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evezart](https://clawhub.ai/user/evezart) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to query a local SearXNG service for privacy-first web search results and to format those results for downstream reasoning or review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Container administration examples can stop, restart, remove, or recreate the local SearXNG container. <br>
Mitigation: Use the curl search examples freely, but run Docker stop, remove, recreate, or restart commands only when intentionally administering the local service. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evezart/skills/searx-search) <br>
- [Submitted SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands, jq examples, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output depends on the local SearXNG instance configuration and selected engines.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
