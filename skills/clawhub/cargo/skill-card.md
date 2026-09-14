## Description:

Cargo routes agents across the Cargo CLI skill bundle, explaining which skill owns each Cargo domain, when to use declarative workspace-as-code versus imperative CLI commands, and how to handle UUIDs, async runs, end-to-end use cases, and common CLI gotchas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this router skill to choose the right Cargo skill for setup, GTM workflows, workspace-as-code, CLI operations, async polling, diagnostics, and cross-skill UUID handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can refresh or install global npm packages and update installed skill state.

Mitigation: Prefer the pinned CLI version from cli-version, review update commands before running them, and skip refresh when the user has pinned a version or opted out.

Risk: Cargo session registration, reports, and diagnostics can send session or report metadata to Cargo.

Mitigation: Opt out of session registration when telemetry is not wanted, redact reports before approval, and send report data only after explicit consent.

Risk: Cargo commands can launch paid runs or batches and some batch mistakes can affect many records.

Mitigation: Preview workflow plans, start with small samples, report observed cost and hit rate, and ask before enrolling the remaining records.

Risk: Some Cargo operations use credentials, API tokens, destructive changes, deployment, lifecycle hooks, or GitHub starring.

Mitigation: Keep token values out of files and transcripts, require user approval for credential and destructive actions, inspect lifecycle hooks before installing them, and star repositories only after the user's explicit endorsement.

## Reference(s):

- [Cargo skill on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - Skills Overview](SKILL.md)
- [Glossary](references/glossary.md)
- [Common gotchas](references/gotchas.md)
- [Interaction conventions](references/interaction.md)
- [Cargo CLI - prerequisites](references/prerequisites.md)
- [End-to-end use cases](references/use-cases.md)
- [UUID flow between skills](references/uuid-flow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output expectations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include Cargo CLI commands that read, create, update, or run workspace resources; paid, credential, report, destructive, and deploy actions require explicit user approval.]

## Skill Version(s):

1.25.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
