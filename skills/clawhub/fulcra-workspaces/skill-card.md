## Description:

Enable agents to collaborate using shared memory, team inboxes, and user artifacts via Fulcra's versioned file storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fulcra](https://clawhub.ai/user/fulcra)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to create Fulcra-backed shared workspaces, coordinate team inboxes, store user-approved artifacts, and maintain durable team progress records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent team state and shared inboxes may expose private workspace context if agents transfer data without authorization.

Mitigation: Require explicit user authorization before cross-agent data transfer, artifact upload, or sharing private workspace data.

Risk: Optional background checks or cron jobs may continue processing team inboxes after the user expects manual operation.

Mitigation: Enable background checks or cron jobs only for specific teams and agents after user consent, and document the context each automated run must read.

Risk: Local MEMORY.md or HEARTBEAT.md changes can alter future agent behavior.

Mitigation: Ask for user approval before modifying local memory or heartbeat files and limit changes to the named team workflow.

## Reference(s):

- [Fulcra Workspaces CLI Reference](references/fulcra-workspaces-cli.md)
- [ClawHub Skill Page](https://clawhub.ai/fulcra/skills/fulcra-workspaces)
- [Fulcra CLI Documentation](https://raw.githubusercontent.com/fulcradynamics/agent-skills/main/skills/fulcra-get-started/references/fulcra-cli.md)
- [Open Knowledge Format Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

## Skill Output:

**Output Type(s):** [markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and file path conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Fulcra CLI command guidance and OKF-compatible workspace file conventions.]

## Skill Version(s):

0.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
