## Description: <br>
Agent Browser Assistant helps agents automate browser interactions and web data collection, including navigation, element interaction, extraction, retries, proxy configuration, and structured responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and automation teams can use this skill to direct an agent through authorized browser automation and web data extraction workflows. It is intended for Chinese-language interaction and returns structured success, data, and error information for follow-up processing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad file and command access for browser automation workflows. <br>
Mitigation: Require explicit approval before running commands, custom scripts, proxies, or file writes, especially in sensitive workspaces or accounts. <br>
Risk: The skill promotes anti-bot bypass techniques. <br>
Mitigation: Use it only for clearly authorized browser automation or data extraction, and avoid using it to bypass anti-bot or anti-scraping controls. <br>
Risk: Dynamic pages and selectors can fail or produce incomplete extracted data. <br>
Mitigation: Review extracted results, retry cautiously, and update selectors or instructions when page structure changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-browser-assistant) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with JSON response examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose browser actions, command execution, file access, proxy configuration, and structured success/error results.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
