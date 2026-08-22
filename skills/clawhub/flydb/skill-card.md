## Description:

Flydb routes agent requests about Flydb database migrations to the appropriate companion skill for CLI execution, migration script work, or multi-environment automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zzxcoding](https://clawhub.ai/user/zzxcoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill to route Flydb-related migration requests to the right helper workflow, including CLI setup and execution, migration script authoring, and multi-environment CI automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database migration commands can change or delete data.

Mitigation: Use dry-run first, require explicit authorization for production, and keep destructive operations out of automation unless separately approved.

Risk: Database passwords could be exposed through commands, logs, or version control.

Mitigation: Keep passwords out of command lines, logs, and repositories; use an approved secret injection mechanism.

## Reference(s):

- [Flydb project](https://github.com/zzxCoding/Flydb)
- [zzxCoding skills repository](https://github.com/zzxCoding/skills)
- [ClawHub skill page](https://clawhub.ai/zzxcoding/skills/flydb)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with routing recommendations and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests to companion Flydb skills; the router skill does not contain executable code.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
