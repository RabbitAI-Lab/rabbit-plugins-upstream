## Description: <br>
Deploys a Chromium browser extension and local CodeBuddy AI backend so users can select or copy webpage text and chat with that page context through streaming responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[noaheleven](https://clawhub.ai/user/noaheleven) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to deploy a webpage-assistant extension for Chromium browsers. It helps send selected or copied page content to a local backend as context for CodeBuddy AI chat, summarization, translation, and explanation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The extension can handle webpage text, clipboard contents, and retained chat context that may include sensitive information. <br>
Mitigation: Review the extension's privacy behavior before installing, avoid using it on sensitive pages, and confirm how clipboard capture, context preview, and stored history clearing work. <br>


## Reference(s): <br>
- [Source repository](https://github.com/NoahEleven/webchat-extension) <br>
- [ClawHub skill page](https://clawhub.ai/noaheleven/skills/webchat-extension) <br>
- [CodeBuddy console](https://copilot.tencent.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, configuration values, and deployment steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces instructions for deploying a Chromium extension and local Express/SSE backend; users should review privacy behavior before installation.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
