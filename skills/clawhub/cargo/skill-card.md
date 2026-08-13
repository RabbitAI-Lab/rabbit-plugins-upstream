## Description:

Routes agents across the Cargo CLI skill bundle, including setup, domain selection, workspace-as-code versus one-off CLI workflows, UUID flow, async polling, use cases, and common Cargo CLI pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill as the entry point for Cargo work: choosing the right Cargo capability skill, installing or authenticating the CLI, running or designing workspace workflows, and avoiding known command, UUID, polling, and billing mistakes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to refresh skills and install or update a global npm CLI.

Mitigation: Confirm the user wants Cargo tooling installed or refreshed, prefer the pinned CLI version when available, and do not change the pin unless explicitly asked.

Risk: Cargo runs and batches can consume paid credits, especially when a batch fans out across many records.

Mitigation: Use the documented plan and sample gates: run a small sample first, report observed cost and hit rate, and ask for explicit approval with record count and credit estimate before full scope.

Risk: Workspace admin operations and token creation can change access or expose credentials.

Mitigation: Confirm the active workspace before writes, keep token scopes narrow, and direct token values to a secrets manager instead of files, commits, or transcripts.

Risk: The optional installer pipes a network-fetched script into a shell.

Mitigation: Do not run the remote installer without explicit user approval; when inspection is needed, download it once, review the saved file, and run that reviewed file.

Risk: Plugin or hook installation may auto-approve ordinary Cargo commands.

Mitigation: Review hook behavior before use and preserve prompts for credentials, token minting, report egress, destructive operations, and deploys.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands that return JSON and may require authentication, workspace selection, or explicit approval before paid or destructive operations.]

## Skill Version(s):

1.19.0 (source: frontmatter and server release metadata; CLI pin 1.0.47)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
