## Description: <br>
Use when LINE Official Account access requires a user-operated temporary VNC/noVNC login, MFA/QR completion, session verification, and secure teardown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mosluce](https://clawhub.ai/user/mosluce) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to provide a temporary, password-protected noVNC browser session for LINE Official Account login or MFA. After login, the agent verifies the LINE OA session, confirms the target conversation and approved message, reports only UI-supported status, and tears down temporary remote-access resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The noVNC URL and VNC password can grant temporary access to the remote browser session. <br>
Mitigation: Treat both as sensitive, use a short-lived high-entropy VNC password, and close the Cloudflare tunnel and VNC/noVNC services after the task. <br>
Risk: A retained isolated browser profile may preserve a LINE session after the immediate task. <br>
Mitigation: Decide explicitly whether the profile should retain the LINE session, and always tear down public remote-access services and temporary credentials. <br>
Risk: LINE UI evidence may show an outgoing message without proving delivery or read status. <br>
Mitigation: Report only the status visible in the UI and avoid claiming delivery or read confirmation unless LINE explicitly displays it. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/mosluce/line-oa-vnc-auth) <br>
- [ClawHub skill page](https://clawhub.ai/mosluce/skills/line-oa-vnc-auth) <br>
- [Artifact README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and operational checklist guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-operated browser login, explicit message approval, UI verification, and teardown of temporary remote-access resources.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
