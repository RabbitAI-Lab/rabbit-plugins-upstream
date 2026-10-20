## Description:

Routes Cargo CLI tasks to the appropriate skill and explains how to coordinate cross-domain workflows, resources, and asynchronous operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market teams use this router to choose the right Cargo skill, set up the CLI, and coordinate tasks spanning multiple Cargo domains.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refreshing installed skills without a version pin can change agent instructions unexpectedly.

Mitigation: Review the target version and approve skill refreshes before running them.

Risk: Some workspace commands, including context runtime execution, can modify or commit tracked files.

Mitigation: Treat execution as a live write; review the intended changes and repository state first.

Risk: CLI installation and commands can affect local or workspace data, and token outputs may expose credentials.

Mitigation: Install the CLI only with user approval, check command scope, and keep token output secret.

Risk: Reports and session shares may disclose workspace information.

Mitigation: Review their contents before sending or sharing them.

## Reference(s):

- [Cargo skill release](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage (listed in metadata)](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [Cargo skill interaction conventions](references/interaction.md)
- [Cargo end-to-end use cases](references/use-cases.md)
- [Cargo UUID flow](references/uuid-flow.md)
- [Cargo common gotchas](references/gotchas.md)
- [Cargo glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes tasks to specialized Cargo skills.]

## Skill Version(s):

1.29.1 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
