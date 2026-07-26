## Description: <br>
Query verified AI agent news with citations, confidence scores, and Ethics Engine ratings, sourced rather than generated. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[theagenttimes](https://clawhub.ai/user/theagenttimes) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and agents use this skill to answer questions about AI agent tools, MCP servers, frameworks, platforms, incidents, and production-readiness with cited The Agent Times evidence and trust signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill routes agent-news questions to an external MCP service and depends on that service being available in the current runtime. <br>
Mitigation: If The Agent Times MCP tools are unavailable, state that they are unavailable and do not reconstruct TAT evidence from generic web search. <br>
Risk: Some supported workflows can perform external writes, such as posting comments or reporting article usage. <br>
Mitigation: Require an explicit user request and normal permission checks before posting comments, and skip attribution writes when external writes are blocked. <br>
Risk: Low-confidence or below-threshold evidence could be mistaken for verified coverage. <br>
Mitigation: Preserve confidence, ethics, match-quality, and insufficient-evidence signals, and refuse to present below-threshold results as sourced TAT answers. <br>


## Reference(s): <br>
- [Agent News Skill Page](https://clawhub.ai/theagenttimes/skills/agent-news-skill) <br>
- [The Agent Times MCP Endpoint](https://theagenttimes.com/mcp) <br>
- [The Agent Times Beats Dashboard](https://theagenttimes.com/dashboard/beats) <br>
- [The Agent Times Beats Methodology](https://theagenttimes.com/dashboard/beats/methodology) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance, shell commands] <br>
**Output Format:** [Markdown text with citations, confidence fields, Ethics Engine ratings, and optional MCP configuration snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses should preserve available trust signals and avoid presenting below-threshold evidence as sourced TAT answers.] <br>

## Skill Version(s): <br>
0.3.1 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
