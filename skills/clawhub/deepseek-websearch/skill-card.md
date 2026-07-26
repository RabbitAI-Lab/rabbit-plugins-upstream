## Description: <br>
Deepseek WebSearch lets an agent submit natural-language web search queries to RedFox/Deepseek and return real-time answers with source citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, researchers, content creators, and developers use this skill to retrieve current web information, fact-check claims, follow trends, and perform technical research through AI-assisted search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to RedFox/Deepseek for third-party processing. <br>
Mitigation: Avoid sending secrets, private documents, credentials, or sensitive personal data unless organizational policy permits that processing. <br>
Risk: The skill requires a REDFOX_API_KEY in the local environment. <br>
Mitigation: Store the key in an environment variable or approved agent configuration, keep it out of code and logs, and confirm it can be reset or revoked. <br>


## Reference(s): <br>
- [Deepseek WebSearch ClawHub release](https://clawhub.ai/redfox-data/skills/deepseek-websearch) <br>
- [Core Workflow](references/core_workflow.md) <br>
- [RedFoxHub API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with source citations, plus JSON results from the search script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires REDFOX_API_KEY and sends search terms to RedFox/Deepseek.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
