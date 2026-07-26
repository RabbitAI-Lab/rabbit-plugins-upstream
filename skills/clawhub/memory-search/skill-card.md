## Description: <br>
Searches and retrieves relevant information from indexed memory files using semantic queries and direct file reads for context. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aigentic-net](https://clawhub.ai/user/aigentic-net) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents use this skill when answering questions that depend on the user's prior conversations, preferences, dates, project history, todos, people, or remembered context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Stored memories and enabled transcripts can contain sensitive personal context that may be resurfaced in normal responses. <br>
Mitigation: Install only when memory use is intended, review retained memory content, and use cited retrieved context when answering personal-context questions. <br>
Risk: Memory search may return incomplete or stale context for a personal-history question. <br>
Mitigation: Search before answering, fetch additional surrounding context only when needed, and state when no relevant memory was found instead of guessing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aigentic-net/skills/memory-search) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API calls, Text] <br>
**Output Format:** [Markdown guidance with JSON tool-call examples and text responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Memory search results may include snippets, relative paths, line ranges, relevance scores, and citations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
