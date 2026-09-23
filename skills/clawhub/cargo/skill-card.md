## Description:

Router for the Cargo CLI skill bundle: it helps agents choose the right Cargo skill or CLI domain, understand declarative versus imperative Cargo workflows, handle UUID and slug handoffs, poll runs and batches, and avoid common Cargo command gotchas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill as the entry point for Cargo CLI work: selecting the correct Cargo capability skill, setting up authentication, routing GTM and workspace tasks, and interpreting command patterns, run identifiers, and operational gotchas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to install or update the global Cargo npm CLI and refresh locally installed Cargo skill instructions.

Mitigation: Require user confirmation before global npm installs, skill refreshes, or version changes; honor pinned versions when present.

Risk: Cargo commands may use account credentials, workspace-scoped API tokens, and session or report data.

Mitigation: Keep login, token creation, report sharing, and session-sharing prompts explicit, and avoid placing secrets or record-level data in reports.

Risk: Some Cargo workflows can perform destructive, deployment, provisioning, or full batch actions.

Mitigation: Use plan gates and approval prompts before destructive actions, deploys, mailbox provisioning, full batch runs, or paid operations.

Risk: Remote skill refreshes and command routing can change the local execution surface during a session.

Mitigation: Review the refreshed instructions and observed CLI help when behavior changes, and do not silently proceed after repeated command failures.

## Reference(s):

- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [Glossary](references/glossary.md)
- [Interaction conventions - plan gates, choices, and presenting](references/interaction.md)
- [Common gotchas](references/gotchas.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and Cargo CLI command patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May route the agent to other Cargo skills and may recommend Cargo CLI commands that operate on a user's Cargo workspace.]

## Skill Version(s):

1.26.1 (source: SKILL.md frontmatter, skill-metadata.json, and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
