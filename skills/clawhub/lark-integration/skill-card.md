## Description: <br>
Connect Lark (Feishu) messaging to OpenClaw via webhook bridge, with bidirectional text, rich text, and image support for Lark International and China Feishu. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[boyangwang](https://clawhub.ai/user/boyangwang) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to set up and troubleshoot a Lark or Feishu messaging bridge for OpenClaw agents, including webhook setup, message formatting, image handling, and optional document access. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public chat messages can trigger an OpenClaw agent pathway with broad local operator authority. <br>
Mitigation: Restrict the bridge to approved chats or explicit bot mentions before enabling it. <br>
Risk: Webhook exposure and request validation gaps can allow unwanted traffic into the bridge. <br>
Mitigation: Put the webhook behind HTTPS and enable request verification before deployment. <br>
Risk: A long-lived bridge service can expose local secrets or run with excessive privileges. <br>
Mitigation: Avoid running the service as root, protect the app secret file, and confirm the service points to the intended bridge file. <br>
Risk: Chat messages and images may be forwarded into OpenClaw. <br>
Mitigation: Use only approved chats and review data sensitivity before sending messages or image attachments through the bridge. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/boyangwang/skills/lark-integration) <br>
- [Lark API Message Formats](references/api-formats.md) <br>
- [Lark Integration Setup Guide](references/setup-guide.md) <br>
- [Lark Developer Console](https://open.larksuite.com/) <br>
- [Feishu Developer Console](https://open.feishu.cn/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration examples, and API payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include webhook setup steps, Lark/Feishu permission guidance, service commands, and troubleshooting notes] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and scripts/package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
