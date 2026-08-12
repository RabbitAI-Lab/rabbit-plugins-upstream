## Description:

Diagnoses Cargo workflow runs, batches, and credit spend by guiding an agent through run traces, error sweeps, and cost attribution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to investigate failed or suspicious Cargo workflow runs, group batch failures by root cause, and identify where workflow credits are spent before proposing fixes or paid re-runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses the user's Cargo CLI session to inspect workflow runs and may access billing data for cost analysis.

Mitigation: Install it only for agents intended to diagnose Cargo workspaces; verify the active session with cargo-ai whoami and reserve admin tokens for billing commands.

Risk: Proposed fixes, workflow edits, or re-runs can spend credits.

Mitigation: Review commands before execution and use the documented pilot gate with a small record sample before broader paid re-runs.

Risk: Raw run details and query results can contain more workspace data than a diagnosis needs.

Mitigation: Present conclusions and compact evidence tables instead of pasting full run get JSON or full query output.

## Reference(s):

- [Run trace](artifact/references/run-trace.md)
- [Batch error sweep](artifact/references/batch-error-sweep.md)
- [Play cost profile](artifact/references/play-optimize-credits.md)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with Cargo CLI command examples and compact diagnostic tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces conclusions, evidence summaries, and recommended next steps; avoids dumping raw run JSON or full query results.]

## Skill Version(s):

1.0.2 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
