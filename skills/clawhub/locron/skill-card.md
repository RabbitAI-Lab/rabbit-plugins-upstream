## Description:

Locron helps agents safely create, inspect, run, update, diagnose, import, export, and manage dashboard state for schedules in the Locron local-first job scheduler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whitekiwi](https://clawhub.ai/user/whitekiwi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to operate Locron jobs, runs, policies, daemon health, service state, and local dashboard state while preserving Locron's validation and authorization boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scheduler changes can run shell commands, make HTTP requests, alter local services, or change dashboard state.

Mitigation: Review proposed changes carefully, use supported dry-runs before applying mutations, and require explicit authorization for operations without dry-run support.

Risk: Dashboard tokens, imported plaintext values, exported values, headers, or command environments can expose secrets.

Mitigation: Avoid displaying or storing secrets, use status checks instead of token disclosure when possible, and require explicit acknowledgement before plaintext import or export.

Risk: Imported job definitions can introduce executable scheduler configuration.

Mitigation: Inspect import dry-run plans, targets, enabled state, policies, and value handling before applying any imported configuration.

## Reference(s):

- [Locron skill page](https://clawhub.ai/whitekiwi/skills/locron)
- [Locron 0.5-0.8 safety model](references/safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prefers Locron JSON command output for reads and decisions; reports warnings, unknowns, dry-run outcomes, and verified durable state.]

## Skill Version(s):

0.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
