## Description: <br>
Send explicitly authorized LINE Official Account Chat messages through a persistent Chromium session; user-operated LINE login or reauthentication may use a temporary remote noVNC handoff that grants interactive browser control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mosluce](https://clawhub.ai/user/mosluce) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill when a user has provided or opened a LINE Official Account Chat URL and explicitly authorizes sending a specific message to a named chat recipient. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A noVNC handoff URL grants interactive control of the authenticated browser while it is armed. <br>
Mitigation: Use handoff only for user-driven login or reauthentication, share the URL only in a private channel with the intended user, and revoke it immediately after login. <br>
Risk: An incorrect recipient or unintended message could be sent from the LINE Official Account. <br>
Mitigation: Use the default no-send dry run first, require an exact recipient and message, stop on ambiguous recipient matches, and use --send only after explicit authorization. <br>
Risk: Credentials, OTPs, MFA prompts, or QR confirmations could be exposed if the agent handles authentication. <br>
Mitigation: The user completes authentication through the browser handoff; the agent should not request, type, store, transmit, or log credentials or verification codes. <br>
Risk: Retrying after post-send verification fails could duplicate a message that LINE already accepted. <br>
Mitigation: Do not retry automatically; inspect the browser state first and report what was found. <br>


## Reference(s): <br>
- [LINE Official Account Chat](https://chat.line.biz/) <br>
- [SKILL.md](SKILL.md) <br>
- [README.md](README.md) <br>
- [Handoff operations](references/handoff-operations.md) <br>
- [LINE OA UI selectors](references/line-oa-ui-selectors.md) <br>
- [Container test environment](containers/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform an external message-send side effect only when invoked with an exact authorized recipient, exact authorized message, and explicit send mode.] <br>

## Skill Version(s): <br>
0.1.5 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
