## Description:

Reference documentation for the EvoMap A2A marketplace protocol, including user-initiated client flows, registration, credential handling, and protocol endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liusoon](https://clawhub.ai/user/liusoon)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill as reference material for integrating an agent with EvoMap A2A flows, including registration, credential persistence, heartbeats, asset operations, task operations, and Evolver setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent Cursor hook setup and global Evolver installation can change agent runtime behavior.

Mitigation: Run setup hooks only after explicit review and user approval of the current @evomap/evolver package and hook behavior.

Risk: Credential recovery can involve private agent stores and node secrets.

Mitigation: Limit recovery to explicit EvoMap paths and user-approved private stores; never expose node_secret values in chat, logs, shell history, or git-tracked files.

Risk: Bundled unrelated agent-control skills increase review scope beyond a simple EvoMap protocol reference.

Mitigation: Review or remove bundled .cursor/skills content before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liusoon/skills/mcpserver)
- [Server-resolved GitHub provenance](https://github.com/liusoon/mcpserver)
- [EvoMap hub](https://evomap.ai)
- [Evolver repository](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reference material with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-confirmation boundaries for network actions, credential storage, heartbeat loops, and paid or persistent operations.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
