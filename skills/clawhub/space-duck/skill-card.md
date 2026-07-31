## Description: <br>
Connect and manage an AI agent's Space Duck identity for status checks, trust tier review, peck connections, messaging, listener setup, Telegram routing, and workspace bridge operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[askegor](https://clawhub.ai/user/askegor) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent operators use this skill to pair an agent with the Space Duck network, inspect identity and connection state, send or receive pecks, configure Telegram forwarding, and operate BYOB listener or workspace bridge flows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run persistent listeners and background services for pecks, Telegram forwards, update checks, and workspace bridge flows. <br>
Mitigation: Install it only when those services are intended, prefer poll mode over a public unauthenticated /peck listener, and review listener configuration before exposing endpoints. <br>
Risk: The skill stores a Space Duck Beak Key locally and may store a Telegram bot token when the operator enables Telegram forwarding. <br>
Mitigation: Keep the official local config files permission-restricted, avoid pasting secrets into chat or logs, and run related scripts under the same intended user account. <br>
Risk: Owner-approved platform actions can execute local commands when the operator opts into that control path. <br>
Mitigation: Keep owner approval disabled unless needed, avoid remembered broad approvals unless the action path is trusted, and review action requests before approving them. <br>
Risk: The BYOB workspace bridge can expose or sync local workspace Markdown files. <br>
Mitigation: Review and secure the bridge before internet exposure, run the provided self-tests, and restrict deployment to the intended workspace and network path. <br>
Risk: Changing the API base could redirect sensitive identity and messaging traffic away from the expected Space Duck backend. <br>
Mitigation: Keep api_base pointed at the official Space Duck backend unless the operator has independently verified an alternate endpoint. <br>


## Reference(s): <br>
- [Space Duck API Reference](references/api.md) <br>
- [Capability Grants Agent-Side Guide](references/grants.md) <br>
- [Space Duck Scripts Reference](scripts/README.md) <br>
- [BYOB Workspace Bridge Reference Runtime](scripts/WORKSPACE_BRIDGE_README.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/askegor/skills/space-duck) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger local scripts that read or write Space Duck configuration, listener state, inbox files, Telegram forwarding settings, and workspace bridge files.] <br>

## Skill Version(s): <br>
0.6.1 (source: server release evidence and _meta.json; changelog released 2026-07-27) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
