## Description: <br>
Dataecho Memory gives agents persistent, cloud-backed memory across sessions, machines, sandboxes, and agent platforms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohocp](https://clawhub.ai/user/mohocp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to recall, create, update, delete, share, and recover durable memories stored in a private DataEcho cloud drive. It is suited for long-running work, user preferences, project decisions, task handoffs, and scoped project memory. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores agent memory in a remote cloud-backed drive, which can expose sensitive or regulated information if users save inappropriate content. <br>
Mitigation: Review saved memories, avoid sensitive personal data and regulated content, and use forget, revoke, and restore controls when memory contents or sharing tokens are no longer appropriate. <br>
Risk: Secrets or API keys could be accidentally written into durable memory. <br>
Mitigation: Do not store secrets or API keys as memories; keep the DataEcho API key only in the configured credential file or environment variable. <br>
Risk: Shared handoff tokens can broaden access to memory contents beyond the current agent session. <br>
Mitigation: Prefer read-only handoff tokens, use short expirations, grant write access only to trusted agents, and revoke tokens when sharing is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohocp/skills/dataecho-memory) <br>
- [Server-resolved GitHub provenance](https://github.com/mohocp/dataecho/tree/main/skills/dataecho-memory) <br>
- [DataEcho homepage](https://dataecho.ai) <br>
- [DataEcho API reference](https://dataecho.ai/openapi.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces memory recall summaries, durable memory entries, handoff tokens, recovery guidance, and setup commands for DataEcho-backed storage.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
