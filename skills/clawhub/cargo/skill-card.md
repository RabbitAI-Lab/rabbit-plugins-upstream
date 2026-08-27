## Description:

Cargo routes agents across the Cargo CLI skill bundle, explaining which capability skill to load, when to use declarative workspace-as-code versus imperative CLI commands, how UUIDs flow between skills, and how to handle async runs, batches, use cases, and common pitfalls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this router to choose the right Cargo capability skill, set up and authenticate the Cargo CLI, route workspace tasks, and follow cross-skill conventions for runs, batches, UUIDs, cost checks, and troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents to globally update Cargo tooling and skill files.

Mitigation: Confirm the pinned version and get user approval before global installs or refreshes; decline or disable automatic refresh/session hooks if background state changes are not desired.

Risk: Cargo workflows can write workspace state, create reports, deploy resources, mint tokens, launch paid batches, and push Git-backed context changes.

Mitigation: Confirm the active workspace and require explicit approval before writes, reports, deploys, token creation, paid batches, and context pushes.

Risk: The skill may ask to star the publisher's GitHub repository using the user's GitHub account.

Mitigation: Avoid granting GitHub starring through the agent unless the user intentionally wants that endorsement.

## Reference(s):

- [Cargo Skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo MCP server](https://mcp.getcargo.io/mcp)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Cargo CLI commands, routing guidance, workspace setup steps, and summaries; Cargo CLI command output is JSON.]

## Skill Version(s):

1.22.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
