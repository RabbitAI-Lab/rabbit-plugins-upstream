## Description: <br>
Manage VK.com (Vkontakte) communities by posting text, photos, and videos and handling messages through the VK API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruslanlanket](https://clawhub.ai/user/ruslanlanket) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External community managers and developers use this skill to automate VK community publishing, media uploads, message handling, and Long Poll monitoring through VK API commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can rely on broad, long-lived VK user tokens with wall, group, media, message, and offline permissions. <br>
Mitigation: Use the narrowest VK token that supports the intended workflow, avoid full offline user tokens when possible, and keep tokens out of shared terminals, logs, and transcripts. <br>
Risk: Commands can publish public posts, upload media, send messages, mark conversations as read, and call VK API methods. <br>
Mitigation: Require manual approval before public posts, message actions, automatic mark-as-read behavior, deletion-related actions, or raw VK API calls. <br>
Risk: Long Poll monitoring can run continuously and process incoming messages in real time. <br>
Mitigation: Set explicit polling time limits and leave automatic mark-as-read disabled unless that behavior is intentional. <br>


## Reference(s): <br>
- [VK API & CLI Guide](references/api.md) <br>
- [VK Host token tool](https://vkhost.github.io/) <br>
- [VK developer documentation](https://dev.vk.com) <br>
- [ClawHub skill page](https://clawhub.ai/ruslanlanket/skills/vk) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline Node.js shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a VK access token and a Node.js runtime.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
