## Description:

Router for the Cargo CLI skill bundle that helps an agent choose the right Cargo skill, understand declarative versus imperative workflows, follow UUID and slug handoffs, poll asynchronous runs and batches, and avoid common Cargo CLI pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this router skill when working with Cargo so an agent can install or invoke the Cargo CLI, choose the correct domain skill, manage workspace setup, run GTM and enrichment workflows, and handle asynchronous run, batch, and reporting flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to refresh skills, install or update the Cargo CLI globally, and use lifecycle hooks.

Mitigation: Confirm the user's intent before global installs or hook-driven updates, and respect pinned versions or opt-outs.

Risk: The skill can guide workspace-reporting and session-sharing flows that may send session context to Cargo.

Mitigation: Ask for explicit user consent before report egress and avoid including secrets or record-level data.

Risk: The skill can lead to admin-token creation, workspace changes, report sharing, optional GitHub starring, and paid batch or enrichment runs.

Mitigation: Confirm workspace identity, token scope, invite lists, paid operations, and GitHub account actions before running commands.

Risk: The security review verdict is suspicious because the skill grants broad update, workspace-reporting, and optional account-action guidance.

Mitigation: Review the skill and commands before deployment, disable or decline lifecycle hooks when automatic tracking or environment updates are not desired, and install only when Cargo workspace management is intended.

## Reference(s):

- [Cargo ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo MCP endpoint](https://mcp.getcargo.io/mcp)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON command-output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Cargo CLI commands that install or update global packages, authenticate users, create workspace resources, run paid Cargo operations, create reports, or share session context when the user approves.]

## Skill Version(s):

1.23.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
