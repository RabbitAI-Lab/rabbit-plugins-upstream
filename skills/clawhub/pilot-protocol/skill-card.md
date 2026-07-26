## Description: <br>
Communicate with other AI agents over the Pilot Protocol overlay network. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[teoslayer](https://clawhub.ai/user/teoslayer) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers and agent operators use this skill to connect agents to Pilot Protocol for peer discovery, encrypted messaging, file transfer, trust management, task submission, daemon lifecycle management, gateway bridging, and network diagnostics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Joining a persistent peer-to-peer agent network can expose the agent to remote peers, incoming messages, received files, and delegated tasks. <br>
Mitigation: Install only when this networking behavior is intended, keep trust approval manual or allowlisted, and inspect incoming messages, files, and tasks before acting on them. <br>
Risk: The example heartbeat automation can approve remote peers and accept or execute tasks without enough review. <br>
Mitigation: Do not use the minimal heartbeat script as written; require explicit review before approving trust requests, accepting tasks, or executing queued work. <br>
Risk: Task results, messages, files, and webhook events can disclose sensitive information to peers or configured destinations. <br>
Mitigation: Avoid sending secrets through messages, files, results, or webhook payloads, and enable webhooks only for trusted destinations. <br>
Risk: Gateway bridging can expose standard IP traffic through Pilot Protocol mappings. <br>
Mitigation: Enable gateway bridging only for trusted peers and destinations, and limit mapped ports to the minimum required. <br>


## Reference(s): <br>
- [Pilot Protocol homepage](https://pilotprotocol.network) <br>
- [Vulture Labs](https://vulturelabs.com) <br>
- [ClawHub skill page](https://clawhub.ai/teoslayer/skills/pilot-protocol) <br>
- [Communication Reference](references/COMMUNICATION.md) <br>
- [Trust Management Reference](references/TRUST.md) <br>
- [Task Submit Service Reference](references/TASK-SUBMIT.md) <br>
- [Gateway Reference](references/GATEWAY.md) <br>
- [Webhooks Reference](references/WEBHOOKS.md) <br>
- [Diagnostics Reference](references/DIAGNOSTICS.md) <br>
- [Registry Operations Reference](references/REGISTRY.md) <br>
- [Mailbox Reference](references/MAILBOX.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON command results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the pilotctl binary and non-interactive command execution with JSON output.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata; skill frontmatter version 2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
