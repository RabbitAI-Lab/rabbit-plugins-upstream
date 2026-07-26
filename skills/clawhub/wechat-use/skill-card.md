## Description: <br>
Wechat Use guides agents in using a macOS WeChat CLI, local HTTP bridge, and Wechaty Puppet gRPC gateway to send messages, query contacts and chat history, retrieve media, and integrate WeChat with automation platforms. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[leeguooooo](https://clawhub.ai/user/leeguooooo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and advanced users can use this skill to automate their own macOS WeChat account, including sending messages, resolving recipients, reading local chat data, exporting history, and wiring a local bridge into agent or workflow tools. It is intended for personal research and automation, not authorized WeChat API use or commercial messaging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool can access local WeChat databases, the database decryption key, contacts, chat history, media, and message sending capability. <br>
Mitigation: Install only if this access is acceptable, keep cached key files protected like passwords, and limit use to the user's own account and lawful personal automation. <br>
Risk: Tunnel, orchestration, AI assistant, and webhook modes can share WeChat data or message-send capability outside the local machine. <br>
Mitigation: Avoid those modes unless strong authentication is configured, allowed chats and message types are tightly limited, and every destination receiving data is trusted. <br>
Risk: The artifact says this is not an authorized WeChat API and may create account, policy, or legal risk if misused. <br>
Mitigation: Use it only for research or personal learning on the user's own WeChat account, avoid spam or third-party automation, and comply with applicable laws and Tencent policies. <br>
Risk: The documented install path uses a remote shell script. <br>
Mitigation: Inspect or pin the installer before running it instead of blindly executing the remote script. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/leeguooooo/wechat-use) <br>
- [ClawHub skill page](https://clawhub.ai/leeguooooo/skills/wechat-use) <br>
- [SSE payload schema](https://github.com/leeguooooo/wechat-use/blob/main/wx/schema/sse-payload-v1.10.28.schema.json) <br>
- [WeChat AI agent integration notes](https://github.com/leeguooooo/wechat-use#接-ai-agent) <br>
- [Release notes](https://github.com/leeguooooo/wechat-use/releases) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON/YAML response contracts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May instruct local CLI or HTTP bridge actions and parse command outputs; exported reports or media are produced by the underlying tool, not by the skill text itself.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata; artifact metadata reports 1.12.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
