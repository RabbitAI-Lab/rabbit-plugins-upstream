## Description: <br>
Harden Paperless cloud-folder intake with staging, provider gates, read checks, and safe retries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[talonpoint](https://clawhub.ai/user/talonpoint) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to design, review, or repair Paperless document intake workflows where files arrive through cloud-synced folders or unreliable filesystem event paths. It guides agents toward staged reads, provider-aware hydration, duplicate handling, atomic delivery, and Paperless-side ingestion verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Guidance may lead an agent to read, stage, move, or verify files from cloud-synced Paperless intake folders. <br>
Mitigation: Keep helper automation scoped to the intake folder, validate readable bytes before delivery, and require explicit approval before cleanup or deletion. <br>
Risk: Broad macOS privacy permissions for generic runtimes can expand the security surface of hydration automation. <br>
Mitigation: Use a trusted helper application or narrow approved user-context host for privacy-gated actions, and avoid broad Accessibility, Screen Recording, or Full Disk Access grants. <br>
Risk: Cloud provider placeholders can appear as normal files while remaining unreadable or incomplete. <br>
Mitigation: Classify the provider, perform bounded read and content validation, leave unreadable files pending, and retry only after hydration evidence succeeds. <br>
Risk: Moving a file into Paperless consume may not prove successful ingestion. <br>
Mitigation: Verify ingestion through a native Paperless signal such as a task, API record, database record, log entry, or equivalent deployment-specific success signal. <br>


## Reference(s): <br>
- [Release Notes - 2.1.0](references/release-notes-2.1.0.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with checklists and inline shell-command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Advisory guidance; proposed file operations and cleanup should be reviewed before execution.] <br>

## Skill Version(s): <br>
2.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
