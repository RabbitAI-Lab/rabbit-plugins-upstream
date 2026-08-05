## Description: <br>
Easy English Tool connects agents to an English-learning MCP and REST service with tools for vocabulary, articles, quizzes, copy practice, text-to-speech, and pronunciation evaluation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dengkane](https://clawhub.ai/user/dengkane) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and their agents use this skill to manage English study activity, including vocabulary review, article practice, quizzes, copy practice, text-to-speech, and progress checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents may handle account credentials, user IDs, learning history, and study actions on a remote service. <br>
Mitigation: Require explicit user confirmation before login, profile or history reads, article deletion, quiz submission, or other account-data changes. <br>
Risk: REST fallback instructions can lead agents to call remote endpoints directly when MCP is not configured. <br>
Mitigation: Confirm the target service URL and the intended action before using REST fallback calls, especially for write or delete operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dengkane/skills/easy-english-tool) <br>
- [Publisher profile](https://clawhub.ai/user/dengkane) <br>
- [Production service](https://english.geeyo.com) <br>
- [MCP streamable HTTP endpoint](https://english.geeyo.com/api/mcp/http) <br>
- [MCP SSE endpoint](https://english.geeyo.com/api/mcp/sse) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, API Calls, Text, Markdown] <br>
**Output Format:** [Markdown guidance with JSON configuration snippets and tool or REST call instructions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return links to MP3 audio or PNG check-in poster assets through the connected service.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
