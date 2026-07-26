## Description: <br>
Use when LINE Official Account access requires a user-operated temporary VNC/noVNC login, MFA/QR completion, session verification, and secure teardown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mosluce](https://clawhub.ai/user/mosluce) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to bootstrap a LINE Official Account Manager browser session through temporary, user-operated VNC/noVNC access. It helps verify the correct OA account and conversation, send only an approved message when needed, and tear down remote-access artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Temporary noVNC and Cloudflare tunnel access can expose the browser session if the URL or VNC password is shared too broadly or left running. <br>
Mitigation: Treat the noVNC URL and VNC password as sensitive, use a short-lived high-entropy VNC password, bind VNC/noVNC to loopback, and close the tunnel and services after use. <br>
Risk: LINE credentials, MFA codes, QR login data, cookies, or private chat screenshots could be exposed through chat, logs, commands, or retained temporary files. <br>
Mitigation: Have the user enter secrets only inside the remote browser, never request or store those secrets in chat or terminal output, and delete password files, screenshots, QR artifacts, and temporary access files after the task. <br>
Risk: An agent could send a message to the wrong LINE OA conversation or overstate delivery status. <br>
Mitigation: Verify the current OA account, recipient name, exact approved message text, and latest outgoing message bubble in the UI; stop when the recipient is ambiguous and report only what the UI shows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mosluce/skills/line-oa-vnc-auth) <br>
- [Publisher profile](https://clawhub.ai/user/mosluce) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup steps, login verification, message-sending guardrails, screenshot fallback guidance, and teardown checks.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
