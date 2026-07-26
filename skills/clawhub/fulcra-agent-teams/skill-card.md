## Description: <br>
Enable agents to collaborate using shared memory, team inboxes, and user artifacts via Fulcra's versioned file storage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fulcra](https://clawhub.ai/user/fulcra) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to create persistent Fulcra team workspaces, coordinate work through shared inboxes, and store user-approved artifacts in versioned file storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent shared state can retain team context, inbox messages, and generated artifacts across sessions. <br>
Mitigation: Install only when durable Fulcra workspaces are desired, and review workspace contents and ownership boundaries before enabling team coordination. <br>
Risk: Optional HEARTBEAT.md entries, cron jobs, and MEMORY.md edits can cause future automated processing of team inbox data. <br>
Mitigation: Require explicit user consent before enabling automation or local memory updates, and review the exact background task or memory directive before approval. <br>
Risk: Uploading private artifacts or transferring context between agents can expose user data to unintended team members. <br>
Mitigation: Require explicit user approval for artifact uploads and cross-agent data transfer, and verify the target team, member, and path before running Fulcra CLI commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/fulcra/skills/fulcra-agent-teams) <br>
- [Fulcra Agent Teams CLI Reference](references/fulcra-agent-teams-cli.md) <br>
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-onboarding/references/fulcra-cli.md) <br>
- [Open Knowledge Format Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and path conventions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes consent gates for artifact uploads, automation, and local memory updates.] <br>

## Skill Version(s): <br>
0.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
