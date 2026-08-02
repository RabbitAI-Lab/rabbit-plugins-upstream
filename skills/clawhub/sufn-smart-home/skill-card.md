## Description: <br>
三峰智能 lets an agent log in to the smart-home platform, switch homes, sync devices, query status, control supported switches, lights, curtains, and air conditioners, and execute existing scenes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lingguyuan](https://clawhub.ai/user/lingguyuan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
End users with 三峰 smart-home accounts use this skill to operate supported home devices and run already configured scenes through natural language. It is intended for device control after successful login, not for creating or modifying scenes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can control real smart-home devices and execute existing scenes after login. <br>
Mitigation: Use it only with the intended 三峰 smart-home account, require successful platform responses before confirming actions, and ask the user to choose when device or scene names are ambiguous. <br>
Risk: The skill stores local access state for future device-control requests. <br>
Mitigation: Keep token storage encrypted, use logout or delete the skill state when access should be removed, and do not expose credentials, tokens, device IDs, or raw platform responses to users. <br>


## Reference(s): <br>
- [三峰智能 ClawHub skill page](https://clawhub.ai/lingguyuan/skills/sufn-smart-home) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Natural-language responses with internal PowerShell command execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Controls real smart-home devices after login and stores local access state encrypted with Windows DPAPI.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
