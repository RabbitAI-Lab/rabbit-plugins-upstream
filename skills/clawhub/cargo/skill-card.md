## Description:

Routes agents to the right Cargo CLI skill for setup, workspace management, GTM workflows, orchestration, storage, analytics, billing, diagnostics, CDK, MCP, and cross-domain Cargo operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GTM operators, and agent builders use this router to decide which Cargo skill to load and how to operate Cargo resources through the CLI or MCP. It supports onboarding, workspace setup, GTM execution, workflow runs and batches, analytics, diagnostics, billing checks, hosting, CDK deployments, and related Cargo workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill describes automatic refreshes that can update the Cargo CLI and skill bundle on the user's machine.

Mitigation: Confirm the user's preference before refresh actions, use the pinned CLI version when available, and skip refreshes when the user has pinned a version or asks not to update.

Risk: Workspace session registration and diagnostic reports can create workspace-side records or send session details to Cargo.

Mitigation: Review report contents before sending and require explicit user consent for diagnostic reports or session sharing.

Risk: Some workflows, batches, connector calls, mailbox operations, and agent actions consume Cargo credits or can repeat charges at scale.

Mitigation: Start with small samples, quote record counts and credit estimates before full execution, and report actual credits spent after paid actions.

Risk: Admin tokens and GitHub account actions can have broad side effects.

Mitigation: Avoid admin tokens unless the command requires them, store API tokens in a secrets manager, and only perform GitHub star actions after explicit user approval.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI commands emit JSON to stdout; async runs, batches, and messages require polling or --wait-until-finished.]

## Skill Version(s):

1.25.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
