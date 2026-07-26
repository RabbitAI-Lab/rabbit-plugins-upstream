## Description: <br>
Search the web using DuckDuckGo through the ddgs Python library without requiring an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neobotjan2026](https://clawhub.ai/user/neobotjan2026) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to let an agent perform current web searches via DuckDuckGo and return result titles, URLs, and snippets for follow-up reading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to an external DuckDuckGo search service. <br>
Mitigation: Avoid submitting secrets, credentials, private identifiers, or confidential internal text in search queries. <br>
Risk: The DuckDuckGo access path may rate limit or fail if service behavior changes. <br>
Mitigation: Handle search failures gracefully, avoid heavy automated query volume, and verify availability before relying on the skill for time-sensitive workflows. <br>
Risk: Search result snippets can be incomplete, stale, or misleading. <br>
Mitigation: Fetch and review primary source pages before using search results for decisions or downstream content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/neobotjan2026/skills/neo-ddg-search) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text search results with a title, URL, and snippet for each result] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default result count is 5, with an optional count up to 20.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
