## Description:

Cargo Diagnostics helps agents explain Cargo workflow behavior after the fact by tracing individual runs, grouping batch failures by root cause, and attributing credit spend to workflows, nodes, and providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to investigate failed, wrong, empty, slow, or unexpectedly expensive Cargo runs and batches. It guides agents through read-oriented Cargo CLI evidence collection, compact diagnosis, and approval-gated follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to inspect Cargo workspace run and billing data, which may expose operational details if raw outputs are pasted into chat.

Mitigation: Confirm the active workspace before use and summarize only the relevant evidence instead of sharing full run outputs.

Risk: Follow-up fixes, batch creation, workflow edits, or re-runs may consume credits.

Mitigation: Require explicit user approval before any paid re-run, batch creation, workflow edit, or support report, and quote the record count and estimated credits first.

Risk: Billing attribution steps require admin access and may not work with a standard token.

Mitigation: Use standard tokens for non-billing diagnostics and request an admin-scoped token only when credit attribution is necessary.

## Reference(s):

- [Cargo Diagnostics Skill](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics)
- [Cargo Skills Repository](https://github.com/getcargohq/cargo-skills)
- [Cargo CLI - Diagnostics](SKILL.md)
- [Batch error sweep - group failures by root cause](references/batch-error-sweep.md)
- [Play cost profile - where credits go, and how to cut them](references/play-optimize-credits.md)
- [Run trace - explain one run end-to-end](references/run-trace.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with concise findings, evidence tables, and inline Cargo CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference workspace-scoped Cargo run, orchestration, and billing data; billing metrics require admin access.]

## Skill Version(s):

1.2.0 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
