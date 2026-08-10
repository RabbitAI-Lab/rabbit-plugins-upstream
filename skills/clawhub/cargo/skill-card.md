## Description:

Cargo is a router and overview skill that helps agents choose and coordinate Cargo CLI skills for workspace setup, GTM workflows, diagnostics, observability, and Cargo CLI command patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and go-to-market operators use this skill to route an agent to the right Cargo CLI sub-skill, plan safe workspace changes, and run or diagnose Cargo workflows with the required setup, UUID, and polling conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install or refresh Cargo tooling and may interact with Cargo plugin or lifecycle hooks.

Mitigation: Install only trusted Cargo CLI/plugin distributions, prefer the documented npm or plugin path, and avoid curl-to-shell installation unless explicitly reviewed.

Risk: Cargo commands can write workspace state, deploy resources, delete resources, create tokens, or send reports with session context.

Mitigation: Verify the active workspace before writes, use least-privilege workspace tokens, and require explicit review for credentials, token creation, report egress, deploys, deletes, and paid or bulk workflow runs.

Risk: Bulk runs and connector actions may spend credits or trigger third-party rate limits at scale.

Mitigation: Run small samples first, report observed cost and hit rate, then ask for approval with the target record count and estimated credits before full enrollment.

Risk: Cargo CLI command mistakes such as wrong UUID type, filter spelling, or table naming can silently return empty or misleading results.

Mitigation: Follow the documented discovery sequence, validate UUID sources, inspect preview rows, and use the gotchas reference before diagnosing empty results.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI prerequisites](references/prerequisites.md)
- [Interaction conventions](references/interaction.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)
- [Common gotchas](references/gotchas.md)
- [Glossary](references/glossary.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cargo CLI commands normally return JSON to stdout; the skill directs agents to summarize results and avoid dumping large raw outputs.]

## Skill Version(s):

1.17.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
