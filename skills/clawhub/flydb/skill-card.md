## Description:

Routes Flydb database-migration requests to the appropriate companion skills for CLI execution, migration-script authoring, multi-environment automation, and Flydb error-code triage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill as the entry point for Flydb adoption and operations. It classifies requests about Flydb CLI usage, migration scripts, CI or multi-environment rollout, and error handling, then routes the agent to the relevant subskill workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Related Flydb subskills may help perform real database migrations that can affect production data.

Mitigation: Review the companion subskills separately and require dry-run review plus explicit environment approval before write operations.

Risk: Database passwords or connection secrets could be exposed during migration setup or execution.

Mitigation: Keep passwords out of commands, logs, and version control; use environment-appropriate secret injection.

## Reference(s):

- [Flydb project](https://github.com/zzxCoding/Flydb)
- [zzxCoding skills repository](https://github.com/zzxCoding/skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and routing decisions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill is a router and should delegate detailed command parameters, migration naming rules, and environment layouts to the companion Flydb skills.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
