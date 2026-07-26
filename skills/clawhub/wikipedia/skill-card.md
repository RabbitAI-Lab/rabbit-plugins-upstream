## Description: <br>
Access Wikipedia through MCP to search articles, retrieve summaries, random facts, dinosaur facts, featured articles, and multi-language results across 10 wikis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[evanfoglia](https://clawhub.ai/user/evanfoglia) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to query Wikipedia from an MCP-compatible agent for research, quick article summaries, trivia, and daily content prompts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User queries are sent to Wikipedia through the local MCP server. <br>
Mitigation: Install only if this network behavior is acceptable for the intended use case. <br>
Risk: The Python dependency is lower-bounded but not pinned or tightly bounded. <br>
Mitigation: For stronger supply-chain hygiene, prefer a release that pins or tightly bounds the dependency. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia) <br>
- [Wikipedia REST API v1 endpoint](https://en.wikipedia.org/api/rest_v1) <br>
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown] <br>
**Output Format:** [Markdown text returned through MCP tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses may include source article links and summary images; supported languages are en, de, es, fr, ja, zh, pt, it, ru, and nl.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence and target metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
