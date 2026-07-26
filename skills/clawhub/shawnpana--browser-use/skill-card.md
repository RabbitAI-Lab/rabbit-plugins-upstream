## Description: <br>
Automates browser interactions for web testing, form filling, screenshots, and data extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shawnpana](https://clawhub.ai/user/shawnpana) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to navigate websites, inspect page state, interact with elements, fill forms, capture screenshots, extract page data, and manage browser sessions through the browser-use CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose logged-in browser sessions, cookies, and authenticated profiles to agent-driven browser actions. <br>
Mitigation: Use isolated or temporary browser profiles by default, treat cookies as credentials, and require explicit approval before connecting to an authenticated profile. <br>
Risk: Cloud browser usage and profile syncing can move sensitive browser state outside the local environment. <br>
Mitigation: Avoid syncing personal profiles to cloud browsers, use dedicated profiles for automation, and protect BROWSER_USE_API_KEY as a credential. <br>
Risk: Public tunnels can expose local development services beyond the local machine. <br>
Mitigation: Start tunnels only with explicit approval, limit them to intended ports, and stop tunnels when the task is complete. <br>
Risk: Raw browser internals and CDP access can perform actions beyond normal page interaction. <br>
Mitigation: Review proposed CDP or Python commands before execution and close browser sessions after sensitive work. <br>


## Reference(s): <br>
- [Browser Use ClawHub Skill Page](https://clawhub.ai/shawnpana/skills/browser-use) <br>
- [browser-use CLI README](https://github.com/browser-use/browser-use/blob/main/browser_use/skill_cli/README.md) <br>
- [Raw CDP & Python Session Reference](references/cdp-python.md) <br>
- [Multiple Browser Sessions](references/multi-session.md) <br>
- [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference browser session state, screenshots, cookies, cloud browser configuration, and API-key setup depending on the requested browser task.] <br>

## Skill Version(s): <br>
2.0.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
