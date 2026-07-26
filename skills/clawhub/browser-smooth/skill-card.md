## Description: <br>
Browser for AI agents to navigate websites, fill forms, extract web data, test web apps, and automate browser workflows with Smooth CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antoniocirclemind](https://clawhub.ai/user/antoniocirclemind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to control Smooth CLI browser sessions for authenticated browsing, web data extraction, form filling, web app testing, file-assisted workflows, and structured browser automation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control authenticated browser sessions and preserve cookies, login sessions, and browser state through Smooth profiles. <br>
Mitigation: Use dedicated browser profiles for this skill, avoid sensitive accounts unless necessary, prefer read-only profiles when appropriate, and delete profiles or session mappings when the task is complete. <br>
Risk: The skill can upload local files into browser sessions and download files from sessions. <br>
Mitigation: Confirm every file upload or download with the user and avoid secrets, regulated documents, or other sensitive files unless the user has explicitly approved their use. <br>
Risk: The skill can execute JavaScript in browser pages. <br>
Mitigation: Restrict JavaScript execution to trusted pages and review the intended operation before running code in an authenticated or sensitive session. <br>
Risk: The skill can navigate the web and perform natural-language browser actions that may change account or application state. <br>
Mitigation: Constrain sessions with allowed URL patterns where possible, ask for confirmation before destructive or account-changing actions, and close sessions when work is done. <br>


## Reference(s): <br>
- [Smooth app and API key portal](https://app.smooth.sh) <br>
- [ClawHub Smooth Browser listing](https://clawhub.ai/antoniocirclemind/skills/browser-smooth) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON structured output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce Smooth CLI commands, session IDs, profile guidance, structured extraction schemas, file upload or download instructions, and browser automation task prompts.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
