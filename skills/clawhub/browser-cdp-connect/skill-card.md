## Description: <br>
Connects an agent browser tool to a user's everyday Chrome session through a CDP WebSocket so the agent can work with authorized sites that block headless browsers or require existing session state. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yuancaoyaohw](https://clawhub.ai/user/yuancaoyaohw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to switch browser automation from a headless browser to a logged-in local Chrome profile when authorized sites block headless browsing or require existing session state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent automation can act through a logged-in Chrome profile and expose account state, cookies, open tabs, or personal browsing context. <br>
Mitigation: Use a separate Chrome profile with no personal accounts, keep sensitive tabs closed, and connect only for authorized sites. <br>
Risk: The CDP URL can remain configured after the task, causing later automation to continue using the real browser. <br>
Mitigation: Clear browser.cdp_url after the task and reset or restart the session before returning to headless browsing. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May update local browser.cdp_url configuration when the shell script is executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
