## Description:

Deploys a Chrome MV3-compatible browser extension for selected-text web chat, with a draggable page overlay that sends webpage context to CodeBuddy AI for streaming answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[noaheleven](https://clawhub.ai/user/noaheleven)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill to deploy a Chromium browser extension that lets a user select or copy webpage text, add it as context, and ask CodeBuddy AI questions from an in-page chat panel. It also provides deployment, packaging, and troubleshooting guidance for the local extension and service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The extension can collect selected webpage text and system clipboard contents on arbitrary pages and persist that context locally.

Mitigation: Use it only on non-sensitive pages, clear stored context when it is no longer needed, and disable or avoid clipboard capture where practical.

Risk: Page metadata, selected context, clipboard-derived context, and chat history can be sent to a local service that may call CodeBuddy AI using local credentials or an API key.

Mitigation: Run only a trusted localhost service, keep API keys in the backend environment file, and set a strict allowed origin before broader deployment.

Risk: The optional webchat:// protocol handler can launch the local service from the browser.

Mitigation: Skip or remove the protocol handler unless one-click launch is required, and verify the registered handler path before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/noaheleven/skills/webchat-extension)
- [Deployment and Troubleshooting Guide](references/deploy-guide.md)
- [Packaged README](assets/root/README.md)
- [CodeBuddy](https://www.codebuddy.cn)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with inline shell commands and generated deployment files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces instructions and local files for deploying a browser extension, configuring CodeBuddy authentication, and packaging a shareable release.]

## Skill Version(s):

0.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
