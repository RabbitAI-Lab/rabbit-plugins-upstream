## Description:

flydb routes Flydb database-migration requests to the appropriate companion skill for CLI use, migration scripts, multi-environment CI, Web workflows, JSON/Plan output, MCP use, or FLYDB error triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill as the entry router for Flydb migration work, choosing the right companion skill for installation, script authoring, execution, Web/MCP workflows, CI rollout, and migration-error triage.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installation commands can pull mutable skill sources.

Mitigation: Review the repository or SkillHub source before installation and confirm the exact skill being installed.

Risk: Flydb workflows can lead to database writes when companion execution skills are used.

Mitigation: Use dry-run first, require explicit approval before writes, and keep passwords out of commands, logs, and version control.

Risk: Routing can point to companion skills or CLI features that are missing or version-mismatched.

Mitigation: Verify the required companion skill is installed and confirm the target Flydb CLI version before relying on routed instructions.

## Reference(s):

- [ClawHub flydb skill page](https://clawhub.ai/zzxcoding/skills/flydb)
- [Flydb project on GitHub](https://github.com/zzxCoding/Flydb)
- [Flydb mirror on Gitee](https://gitee.com/zzhenxuan/Flydb)
- [zzxCoding skills repository](https://github.com/zzxCoding/skills)
- [SkillHub](https://skillhub.cn)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes users to companion Flydb skills and keeps database-write safeguards explicit.]

## Skill Version(s):

1.0.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
