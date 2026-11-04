## Description:

Router for the Cargo CLI skill bundle — load first for anything Cargo, and whenever a task spans two Cargo domains. Explains what each skill owns, declarative GTM as Code projects (cargo-project) vs the imperative CLI, the UUID and slug flow between skills, async polling of runs and batches, end-to-end use cases, and the gotchas that fail silently (inputs in a top-level action's `config` stripped without an error, run vs batch, model-uuid vs segment-uuid). Triggers: "set up Cargo", "what can Cargo do", "which Cargo skill", "bootstrap my workspace", "I have a Cargo account", "cargo-ai …", or any `cargo-ai` command whose domain you are unsure of. Skip when: the task obviously belongs to one skill — load that skill directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Cargo CLI users and their agents use this router to choose the right Cargo skill for a GTM or workspace task, understand how the capability skills fit together, and follow documented setup, command, and workflow guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring software updates and diagnostic sharing may proceed without consistent approval.

Mitigation: Review the update and support-report policies, pin reviewed software and skill revisions, and approve sanitized diagnostic reports before submission.

Risk: Broad Cargo permissions or skipped documented design and batch gates can increase the impact of actions.

Mitigation: Use the narrowest required permissions and retain the documented design and batch approval gates.

Risk: Context runtime writes may persist beyond the current operation.

Mitigation: Confirm the persistence behavior before relying on a runtime write; verify any separately installed approval hooks.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Prerequisites and authentication](references/prerequisites.md)
- [Interaction conventions](references/interaction.md)
- [UUID flow between skills](references/uuid-flow.md)
- [End-to-end use cases](references/use-cases.md)
- [Common gotchas](references/gotchas.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, Configuration, Code]

**Output Format:** [Markdown guidance with shell command examples and structured configuration or code when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill routes users to the appropriate Cargo capability documentation and explains relevant workflow constraints.]

## Skill Version(s):

1.34.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
