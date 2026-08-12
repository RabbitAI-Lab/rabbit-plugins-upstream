## Description:

Cargo is a router and overview skill that helps agents choose and use Cargo CLI skills for GTM workflows, workspace setup, diagnostics, observability, and related CLI operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GTM operators, and agent users use this skill to route Cargo CLI work to the right Cargo capability skill, understand setup and authentication conventions, and coordinate tasks such as enrichment, CRM sync, AI lead scoring, monitoring, and workspace bootstrap.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill directs automatic code refreshes and session metadata updates through persistent hooks.

Mitigation: Review before installing in sensitive environments, pin versions where possible, and opt out of session registration or checkpointing when session metadata should not be written to Cargo.

Risk: Installation paths may involve shell-based installers or global CLI updates.

Mitigation: Avoid blind curl-to-shell installation, review installer behavior first, and prefer pinned package versions when repeatability matters.

Risk: Cargo commands can write to a workspace, mint tokens, deploy resources, delete resources, or trigger paid work.

Mitigation: Verify the active workspace before write, paid batch, deploy, token, or destructive commands; use approval gates and small samples before full batch execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash commands and JSON command-output conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance depends on an authenticated Cargo CLI workspace and may include paid or write-capable CLI operations.]

## Skill Version(s):

1.17.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
