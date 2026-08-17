## Description:

Router for the Cargo CLI skill bundle that helps agents choose the right Cargo skill, distinguish declarative workspace-as-code from imperative CLI work, follow UUID and slug flows, poll asynchronous runs and batches, and avoid common command pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agent users use this skill as the entry point for Cargo CLI work: selecting the right Cargo capability skill, setting up and authenticating the CLI, running workspace workflows, and understanding cross-skill identifiers, polling, cost, and reporting conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo CLI access can modify workspace state, perform admin-scoped operations, deploy or delete resources, and run paid or bulk workflows.

Mitigation: Confirm the active workspace, require explicit user approval before paid runs, bulk batches, default-branch writes, deploys, deletes, token changes, or user and role changes, and start with small samples before full enrollment.

Risk: The skill supports session reporting and session sharing, which can send session context outside the local workspace.

Mitigation: Review report content before sending and decline session sharing unless the user explicitly consents.

Risk: API tokens and login codes can grant workspace access and may be shown only once.

Mitigation: Keep tokens in a secrets manager, avoid exposing codes in shell history, and use workspace-scoped tokens with the least privilege needed.

Risk: The artifact includes a request flow for starring the publisher's GitHub repository.

Mitigation: Treat repository starring as a user endorsement and perform it only after explicit user approval.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [Interaction conventions](references/interaction.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)
- [Common gotchas](references/gotchas.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell command examples and routing tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include Cargo CLI commands, skill routing decisions, workflow sequencing, polling steps, cost checkpoints, and safety gates.]

## Skill Version(s):

1.20.1 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
