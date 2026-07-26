## Description: <br>
Use Claude Code with the Chrome browser extension for web browsing and automation tasks as an alternative to OpenClaw's built-in browser tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dgriffin831](https://clawhub.ai/user/dgriffin831) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to have an agent check Chrome extension readiness, launch Claude Code with Chrome integration, and perform browser navigation or automation tasks from shell commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill instructs users to run Claude Code with broad auto-approval in a real Chrome session. <br>
Mitigation: Use a dedicated Chrome profile or test account, avoid sensitive logged-in sessions, keep prompts narrow and low-impact, and monitor or stop background claude processes. <br>
Risk: Browser automation can interact with pages, click elements, fill forms, and read web content through Chrome. <br>
Mitigation: Prefer safer built-in browser tools for simple read-only browsing and reserve this skill for tasks that require Chrome extension control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dgriffin831/skills/claude-chrome) <br>
- [Publisher profile](https://clawhub.ai/user/dgriffin831) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes timeout recommendations, prerequisite checks, and browser automation usage notes.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
