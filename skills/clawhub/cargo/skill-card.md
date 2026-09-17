## Description:

Cargo routes agents across the Cargo CLI skill bundle, covering domain ownership, workspace-as-code versus imperative CLI workflows, UUID and slug flow, async run and batch polling, use cases, and common CLI gotchas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and GTM operators use this router to select the right Cargo skill, set up and authenticate the Cargo CLI, manage session conventions, and navigate Cargo workflow identifiers and command flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to refresh installed skills or install a global Cargo CLI package.

Mitigation: Require explicit user approval before npm/npx installs or skill refreshes, and prefer the pinned CLI version when available.

Risk: Session reports may send session metadata or troubleshooting details to Cargo.

Mitigation: Ask for consent before report submission and review or redact report content before sending.

Risk: The skill includes an optional prompt for an authenticated GitHub star action.

Mitigation: Run authenticated GitHub actions only after an explicit user yes, and do not substitute another endorsement flow.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to other Cargo skills and to Cargo CLI commands; it does not itself generate executable code.]

## Skill Version(s):

1.26.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
