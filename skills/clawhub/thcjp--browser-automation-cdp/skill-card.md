## Description: <br>
Browser Automation CDP helps agents drive a user's logged-in Edge or Chrome browser through Chrome DevTools Protocol for JavaScript-rendered navigation, interaction, screenshots, and data extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation-focused agents use this skill to operate pages that require login state, JavaScript rendering, or interactive browser actions when ordinary web fetching is insufficient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using CDP can act inside logged-in browser sessions and may access sensitive account data. <br>
Mitigation: Use a separate browser profile when possible, avoid sensitive accounts, and confirm the exact site and data scope before authenticated automation. <br>
Risk: The artifact discusses reading browser cookie databases, which can expose private account data. <br>
Mitigation: Do not allow the agent to read browser cookie databases or credential stores; rely on normal browser session state only. <br>
Risk: Remote debugging ports expose browser control to local processes while they are open. <br>
Mitigation: Enable remote debugging only for the task, use trusted local environments, and close or restart the browser after automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/browser-automation-cdp) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration] <br>
**Output Format:** [Markdown with inline PowerShell and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide an agent to return extracted page data, browser action results, or base64 PNG screenshots.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
