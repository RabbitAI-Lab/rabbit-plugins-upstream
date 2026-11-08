## Description:

Routes Cargo CLI requests to the right skill and guides agents through setup, execution, and common workflow pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this router to identify the appropriate Cargo skill and follow consistent workflows for managing go-to-market data, integrations, and automation through the Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or refreshing the skill can replace agent instructions and change behavior.

Mitigation: Pin the CLI, installer, and skills revision, and review instruction updates before installing.

Risk: Credentials and detailed support reports may expose sensitive information.

Mitigation: Use narrowly scoped credentials and inspect redacted support reports before sending them.

Risk: Runtime-command guidance may conflict before a command modifies tracked files.

Mitigation: Resolve the documentation conflict before tracked-file changes and retain approval for consequential workflows.

## Reference(s):

- [Cargo skills project homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](artifact/references/prerequisites.md)
- [End-to-end use cases](artifact/references/use-cases.md)
- [Common gotchas](artifact/references/gotchas.md)
- [Interaction conventions](artifact/references/interaction.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by task; may include command sequences and workflow guidance.]

## Skill Version(s):

1.36.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
