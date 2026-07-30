## Description: <br>
Brave Search Tool Free guides an agent through Brave Search API-backed web search, result-count configuration, and URL content extraction without launching a browser. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual users use this skill to ask an agent for Brave Search API-based document lookup, fact lookup, current-information search, and Markdown extraction from known URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence marks the release as suspicious because it describes command execution but the package contains only Markdown and does not include the referenced scripts. <br>
Mitigation: Review the installed files before use and approve only commands whose target scripts are present and understood. <br>
Risk: The skill requires a Brave API key and can send user queries to an external search service. <br>
Mitigation: Provide the API key only in trusted environments and avoid submitting sensitive or confidential queries. <br>
Risk: The skill examples include npm setup, local script execution, and redirecting extracted content to files. <br>
Mitigation: Confirm npm-based setup steps, command paths, and file outputs before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/brave-search-tool-free) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with shell command examples and text or Markdown search-result output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Brave API key and command approval for any npm or script execution described by the skill.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
