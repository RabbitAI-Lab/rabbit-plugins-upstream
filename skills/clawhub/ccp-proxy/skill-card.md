## Description:

Provides a local OpenAI-compatible CCP API reverse proxy on 127.0.0.1:8257 for routing WorkBuddy qwen-3.5 traffic to China Mobile CCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wangyongjie](https://clawhub.ai/user/wangyongjie)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to start, stop, check, test, and configure a local reverse proxy that forwards OpenAI-compatible chat requests to China Mobile CCP. It is intended for users who want qwen-3.5 or another configured model to run through a local WorkBuddy model endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys are stored persistently in ~/.workbuddy/models.json.

Mitigation: Use an appropriate scoped key, protect local file access, and remove or rotate the key when the proxy is no longer needed.

Risk: The proxy daemon remains running until it is stopped.

Mitigation: Check the proxy status before use and run the stop command when the local CCP route is no longer intended.

Risk: Requests and Authorization headers are forwarded to China Mobile CCP through the configured upstream.

Mitigation: Install and use the skill only when routing WorkBuddy qwen-3.5 traffic through China Mobile CCP is expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wangyongjie/skills/ccp-proxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide users through starting a persistent local daemon and writing WorkBuddy model configuration.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
