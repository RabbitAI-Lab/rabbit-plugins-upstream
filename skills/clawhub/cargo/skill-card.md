## Description:

Cargo is a router skill for the Cargo CLI skill bundle that helps agents choose the right Cargo capability, distinguish declarative CDK workflows from imperative CLI tasks, and follow Cargo UUID, async polling, and operational gotcha conventions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GTM operators, and agents use this skill to route Cargo CLI work across setup, workspace-as-code, GTM workflows, storage, orchestration, analytics, billing, observability, hosting, mailbox, and workspace management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to operate a Cargo workspace through broad Cargo CLI authority.

Mitigation: Install it only when Cargo workspace operations are intended, confirm the active workspace before writes, and keep explicit approval for credentials, token creation, deployments, destructive changes, reports, and paid batches.

Risk: Plugin or hook behavior may auto-refresh local tools, register session activity, and auto-approve many ordinary Cargo commands.

Mitigation: Review plugin and hook behavior before installation, use one install channel to avoid duplicate skills, and leave protected prompts in place for sensitive operations.

Risk: Cargo workflows may consume credits, especially broad batches or phone lookup actions.

Mitigation: Start with small samples, quote record counts and credit estimates before expanding work, and report credits spent and remaining balance after paid actions.

Risk: Session sharing and GitHub starring flows can disclose activity or use the user's GitHub account if approved.

Mitigation: Ask for explicit consent before report egress or starring, avoid secrets and record-level data in reports, and never star the repository without the user's approval.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and concise procedural guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands that operate on a user's Cargo workspace and may trigger paid batches, token creation, deployment, reporting, or account actions when the user approves them.]

## Skill Version(s):

1.21.0 (source: frontmatter, artifact metadata, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
