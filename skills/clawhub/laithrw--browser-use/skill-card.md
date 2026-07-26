## Description: <br>
Browser Use 3.0 guides agents in using the browser-use CLI to navigate websites, interact with pages, fill forms, capture screenshots, and extract web data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[laithrw](https://clawhub.ai/user/laithrw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to automate browser workflows for testing, form filling, screenshots, authenticated browsing, and structured web data extraction. It is most useful when the agent needs repeatable browser control with explicit inspection and verification steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local mode can control the user's signed-in Chrome session with broad browser authority. <br>
Mitigation: Use cloud or isolated browser mode for sensitive workflows, and require explicit confirmation before logged-in account actions, purchases, posting, or destructive changes. <br>
Risk: Browser automation can expose secrets or private account data if credentials are pasted, logged, or used on the wrong page. <br>
Mitigation: Treat BROWSER_USE_API_KEY and account credentials as secrets; pass API keys through stdin when supported and avoid writing secrets to pages, files, or logs. <br>
Risk: Cloud browser sessions may continue running and billing after the task is complete. <br>
Mitigation: Ask whether to close cloud browsers at the end of work and stop named remote daemons when they are no longer needed. <br>


## Reference(s): <br>
- [Browser Use 3.0 on ClawHub](https://clawhub.ai/laithrw/skills/browser-use) <br>
- [Browser Use GitHub Repository](https://github.com/browser-use/browser-use) <br>
- [Browser Use Install Guide](https://github.com/browser-use/browser-harness/blob/main/install.md) <br>
- [Browser Use Interaction Skills](https://github.com/browser-use/browser-harness/tree/main/interaction-skills) <br>
- [Browser Use Cloud](https://cloud.browser-use.com?utm_source=skill&utm_medium=browser-use&utm_campaign=v4) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May lead the agent to produce screenshots, browser state observations, and extracted web data when following the workflow.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
