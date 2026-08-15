## Description:

Helps developers and database operations teams organize Flydb migrations across multiple database families and environments with per-environment configuration, externalized secrets, CI command gates, baseline onboarding, and offline driver handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, database administrators, and DevOps engineers use this skill to plan and document Flydb migration automation across test, staging, and production environments. It helps produce environment matrices, deployment configuration layouts, CI command sequences, baseline guidance, and risk-aware operational checklists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CI steps may lead to production database changes.

Mitigation: Use reviewed dry-run output, a production approval gate, and explicit authorization before running migration commands.

Risk: Database credentials can be exposed if teams place passwords in commands, logs, or committed configuration.

Mitigation: Use external secret storage, dedicated migration accounts, and password injection through environment variables or restricted password files.

Risk: Existing databases can be misrepresented if baseline versions are chosen without reconciliation.

Mitigation: Manually reconcile applied versions, rehearse baseline onboarding in a test environment, and avoid automated repair in deployment pipelines.

## Reference(s):

- [Multi-environment reference](artifact/references/multi-environment.md)
- [ClawHub skill page](https://clawhub.ai/zzxcoding/skills/flydb-multi-environment)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database environment matrices, deployment checklists, and human approval gates.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
