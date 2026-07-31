## Description: <br>
Send explicitly authorized LINE Official Account Chat messages through a persistent Chromium session; user-operated LINE login or reauthentication may use a temporary remote noVNC handoff that grants interactive browser control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mosluce](https://clawhub.ai/user/mosluce) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and operators use this skill when they need an agent to send an exact, explicitly authorized message to a named LINE Official Account Chat recipient through an already authenticated browser session. It supports login or reauthentication through a temporary user-operated noVNC handoff when the user requests that route. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send authorized LINE Official Account messages from an authenticated browser session. <br>
Mitigation: Require explicit authorization for the exact recipient and message, use the default no-send dry run before sending, and avoid automatic retries after post-send verification failures. <br>
Risk: The optional noVNC handoff grants interactive browser control to whoever has the printed URL. <br>
Mitigation: Use the handoff only for user login or reauthentication, share the URL only in a private channel, revoke it immediately after login, and stop the browser session when finished. <br>
Risk: Credentials, OTPs, MFA prompts, or security challenges may appear during LINE authentication. <br>
Mitigation: Let the user complete all authentication steps through the handoff and never request, type, record, relay, or log credentials or verification codes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mosluce/skills/line-oa-chat-send) <br>
- [LINE Official Account Chat](https://chat.line.biz/) <br>
- [Skill instructions](SKILL.md) <br>
- [Handoff operations](references/handoff-operations.md) <br>
- [LINE OA Chat UI selector notes](references/line-oa-ui-selectors.md) <br>
- [Container test environment](containers/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and concise status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger an external message send only when the exact recipient and message are authorized and the send command is invoked with --send.] <br>

## Skill Version(s): <br>
0.1.6 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
