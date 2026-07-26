## Description: <br>
Control real Android and iOS devices, run apps, take screenshots, and execute on-device inference via Ghost in the Droid MCP server (62 tools). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[c-k-loan](https://clawhub.ai/user/c-k-loan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and agent builders use this skill to connect an LLM agent to Android or iOS devices for app testing, screen interaction, workflow automation, and on-device inference. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent using this skill can operate connected mobile devices, including sensitive screens, clipboard contents, app installation, app-data clearing, login flows, and replayed or batched actions. <br>
Mitigation: Use test devices or emulators where possible, avoid sensitive screens and clipboard contents, and require explicit confirmation before installs, app-data clearing, login flows, or replayed and batched actions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/c-k-loan/skills/ghost-in-the-droid) <br>
- [iOS setup guide](https://github.com/ghost-in-the-droid/android-agent/blob/main/docs/ios/SETUP.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, JSON configuration snippets, and tool-use guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to operate mobile device screens, clipboard, app installation, app-data clearing, batched actions, and on-device inference through an MCP server.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
