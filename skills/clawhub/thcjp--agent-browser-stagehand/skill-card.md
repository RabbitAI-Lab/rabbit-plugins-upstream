## Description: <br>
Automates web browser interactions using natural-language CLI commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to navigate pages, perform browser actions, and extract page data through natural-language CLI instructions. It is suited to browser automation workflows where the user can review requested actions and resulting data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad browser, file, and command authority without enough scoping or user-control guidance. <br>
Mitigation: Run it in a restricted environment and require confirmation before commands, file writes, proxy or user-agent changes, or bulk extraction. <br>
Risk: Browser automation can access logged-in sessions, sensitive websites, or secret page content if the user grants that context. <br>
Mitigation: Avoid logged-in or sensitive websites unless that access is explicitly intended, and do not provide secrets unless necessary for the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent-browser-stagehand) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include browser action results, extraction summaries, execution logs, and error details.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
