## Description:

Router for the Cargo CLI skill bundle that helps agents choose the right Cargo skill, distinguish declarative CDK workflows from imperative CLI work, follow UUID and slug flow, poll runs and batches, and avoid common Cargo command mistakes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and GTM teams use this router to orient an agent within the Cargo skill bundle before setup, workspace automation, GTM workflows, or unfamiliar cargo-ai commands. It points the agent to the right domain skill and supporting references for install, authentication, routing, polling, and command pitfalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to install or refresh global Cargo CLI tooling and skill files.

Mitigation: Review hook and refresh behavior before use, pin versions where possible, and require user approval before changing global tooling.

Risk: Cargo CLI commands may affect workspace data, spend credits, mint tokens, send reports, deploy resources, delete resources, or star a GitHub repository.

Mitigation: Confirm the active workspace before writes and require explicit approval for paid batches, reports, token creation, context-repo pushes, deploys, deletes, and starring actions.

Risk: Automatic session registration or reporting can record session state in the Cargo workspace.

Mitigation: Install only when that workspace visibility is acceptable and keep report creation consent explicit.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [UUID flow between skills](references/uuid-flow.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands generally return JSON on stdout; the skill asks agents to confirm workspace context before writes and obtain explicit approval for paid or sensitive operations.]

## Skill Version(s):

1.24.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
