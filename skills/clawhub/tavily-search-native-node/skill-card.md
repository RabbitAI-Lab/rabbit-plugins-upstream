## Description: <br>
Minimal Tavily web search for OpenClaw using native Node.js and a Tavily API key, returning summarized search results with source citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jwestburg](https://clawhub.ai/user/jwestburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search current web or news information through Tavily when model knowledge may be stale, then present concise, source-backed results for user review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to Tavily and may disclose sensitive user-provided text. <br>
Mitigation: Do not search secrets, confidential incident text, client identifiers, or private internal strategy unless the user explicitly approves sending that query to Tavily. <br>
Risk: Searches consume Tavily API credits and may encounter Tavily rate limits. <br>
Mitigation: Use targeted searches, prefer basic depth unless deeper research is needed, and review Tavily account usage and limits before relying on the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/tavily-search-native-node) <br>
- [Tavily API endpoint](https://api.tavily.com/search) <br>
- [Tavily app and API key management](https://app.tavily.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Human-readable text by default, or raw JSON when invoked with the JSON flag] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TAVILY_API_KEY; outputs include the searched query and may consume Tavily API credits.] <br>

## Skill Version(s): <br>
1.0.12 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
