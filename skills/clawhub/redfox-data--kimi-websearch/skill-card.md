## Description: <br>
Kimi Websearch submits natural-language queries to RedFox/Kimi web search, polls for completion, and returns structured answers with source citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, students, and researchers use this skill to run real-time web searches from natural-language questions and receive structured answers with sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to an external RedFox/Kimi service. <br>
Mitigation: Do not use the skill with secrets, private documents, regulated data, or prompts that should not be processed by an external search service. <br>
Risk: The skill requires a REDFOX_API_KEY for the external API. <br>
Mitigation: Store the key in environment configuration, verify its source, scope, expiration, and reset or revoke it if exposed. <br>


## Reference(s): <br>
- [Kimi Websearch on ClawHub](https://clawhub.ai/redfox-data/skills/kimi-websearch) <br>
- [README.en.md](README.en.md) <br>
- [RedFoxHub API keys](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, markdown, shell commands, guidance] <br>
**Output Format:** [JSON from the search script, with agent-facing text or Markdown summaries that can include citations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY; sends natural-language search queries to an external RedFox/Kimi API and polls for up to 5 minutes.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
