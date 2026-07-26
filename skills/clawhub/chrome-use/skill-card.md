## Description: <br>
Chrome Use provides CLI-guided browser automation workflows for agents that need live web access, real Chrome sessions, web search, page interaction, screenshots, and specialized automation guides. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and AI-agent users use this skill to route live web, authenticated browser, QA, Electron, Slack, and cloud-browser tasks through the chrome-use CLI workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct an agent to control a real logged-in Chrome browser and interact with authenticated sites. <br>
Mitigation: Require explicit confirmation before logins, form submissions, purchases, account changes, private-page scraping, Slack actions, or Electron app actions. <br>
Risk: The skill installs and relies on remote CLI-provided workflow content. <br>
Mitigation: Review the installer and CLI-provided skill content before use, and install only when broad browser automation authority is intended. <br>


## Reference(s): <br>
- [Chrome Use on ClawHub](https://clawhub.ai/leeguooooo/skills/chrome-use) <br>
- [chrome-use install script](https://raw.githubusercontent.com/leeguooooo/chrome-use/main/install.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and routing tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill primarily tells the agent which chrome-use CLI guide or command to run; the CLI may control real logged-in browser sessions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
