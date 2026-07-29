## Description: <br>
Send explicitly authorized LINE Official Account Chat messages through a persistent Chromium session; user-operated LINE login or reauthentication may use a temporary remote noVNC handoff that grants interactive browser control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mosluce](https://clawhub.ai/user/mosluce) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to send a specifically authorized message to a named LINE Official Account Chat recipient from an already authenticated Chromium session. It also guides a user-operated, temporary login or reauthentication handoff when the session needs renewed access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A temporary noVNC login handoff grants browser control to anyone holding its URL. <br>
Mitigation: Share any handoff URL only with the intended user in a private channel and revoke it immediately after login rather than relying only on TTL expiry. <br>
Risk: A message sent to the wrong or ambiguous LINE OA conversation could reach an unintended recipient. <br>
Mitigation: Confirm the exact recipient and message before using --send, and stop for user clarification when recipient search is ambiguous. <br>
Risk: A failed post-send verification can make delivery uncertain and an automatic retry could duplicate the message. <br>
Mitigation: Do not retry automatically after verification failure; inspect the browser state first and report what was found. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mosluce/skills/line-oa-chat-send) <br>
- [LINE Official Account Chat](https://chat.line.biz/) <br>
- [README](README.md) <br>
- [Handoff operations](references/handoff-operations.md) <br>
- [LINE OA Chat: UI selector notes](references/line-oa-ui-selectors.md) <br>
- [Container test environment](containers/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Text] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local command execution and can produce an external LINE message only when the exact recipient and message are explicitly authorized.] <br>

## Skill Version(s): <br>
0.1.4 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
