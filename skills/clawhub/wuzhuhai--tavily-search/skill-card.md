## Description: <br>
Tavily Search gives agents Tavily-powered web search, research-mode search, image search, source citations, and structured search results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wuzhuhai](https://clawhub.ai/user/wuzhuhai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to run current web searches, deeper multi-page research, and image searches through Tavily with text or JSON results that include source URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and retrieved content are sent to Tavily, an external service. <br>
Mitigation: Avoid sensitive or regulated queries and review service handling requirements before use. <br>
Risk: The release ships with a plaintext Tavily API key in config.json. <br>
Mitigation: Replace or remove the bundled key before use and store a user-owned Tavily key in a safer secret mechanism when available. <br>


## Reference(s): <br>
- [Tavily Website](https://tavily.com/) <br>
- [Tavily Search API Endpoint](https://api.tavily.com/search) <br>
- [ClawHub Skill Page](https://clawhub.ai/wuzhuhai/skills/tavily-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [Plain text or JSON search results with source URLs and optional image URLs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return generated answers, result titles, source links, publication dates, snippets, response time, and optional images.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
