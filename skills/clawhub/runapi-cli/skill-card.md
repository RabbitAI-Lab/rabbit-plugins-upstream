## Description: <br>
Install and use the RunAPI CLI as the universal execution layer for RunAPI models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[runapi-ai](https://clawhub.ai/user/runapi-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and agent operators use this skill to install, authenticate, inspect, and automate RunAPI CLI workflows from terminals, servers, CI jobs, and agent runtimes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installer scripts and binary installation flows can affect the local system if sourced from the wrong place or tampered with. <br>
Mitigation: Prefer the Homebrew install path or a verified installer flow, and rely on the documented checksum verification before using the installed runapi binary. <br>
Risk: RunAPI API keys, saved credentials, and listener signing secrets could be exposed through shared environments, process arguments, logs, or committed config files. <br>
Mitigation: Use RUNAPI_API_KEY or stdin token import instead of command-line token arguments, keep credentials out of project config and repositories, and rotate listener signing secrets if exposed. <br>
Risk: Local files passed to RunAPI upload fields may contain sensitive or unintended content. <br>
Mitigation: Review local files before passing paths to upload fields and treat returned temporary URLs as short-lived transfer artifacts rather than durable storage. <br>
Risk: Local callback listener failures can be missed because each valid event is acknowledged before the local HTTP forward attempt and forwarded locally once. <br>
Mitigation: Monitor non-2xx responses or connection errors, check CLI exit status, and debug local webhook handling without assuming a listener replay will occur. <br>


## Reference(s): <br>
- [RunAPI model and CLI service catalog](https://runapi.ai/models.md) <br>
- [RunAPI model browser](https://runapi.ai/models) <br>
- [ClawHub runapi-cli skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli) <br>
- [ClawHub runapi-ai publisher profile](https://clawhub.ai/user/runapi-ai) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code, JSON] <br>
**Output Format:** [Markdown guidance with shell commands, JSON examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance covers RunAPI CLI installation, authentication, model execution, pricing, callback listeners, temporary file uploads, and agent-runtime skill installation.] <br>

## Skill Version(s): <br>
0.2.13 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
