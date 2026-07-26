## Description: <br>
Complete Omi.me integration for memories, action items (tasks), and conversations. Full CRUD + sync capabilities for OpenClaw. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[caioiscoding](https://clawhub.ai/user/caioiscoding) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to configure Omi.me access and manage memories, action items, conversations, and sync operations from a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Omi API tokens can be exposed through local token storage or terminal output. <br>
Mitigation: Use a limited or disposable Omi API token, keep ~/.config/omi-me/token restricted to chmod 600, and avoid running omi-token.sh get in logged or shared terminals. <br>
Risk: Update and delete commands make live changes to the connected Omi.me account. <br>
Mitigation: Review commands before execution and test with low-risk data or a disposable account before using the skill with important data. <br>
Risk: An inherited API_URL environment variable could affect where API requests are sent. <br>
Mitigation: Clear any API_URL environment variable before use unless the endpoint has been deliberately reviewed. <br>


## Reference(s): <br>
- [Omi.me](https://omi.me) <br>
- [Omi Developer API Overview](https://docs.omi.me/doc/developer/api/overview) <br>
- [ClawHub Skill Page](https://clawhub.ai/caioiscoding/skills/omi-me) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an OMI_API_TOKEN and the omi and omi-token command wrappers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
