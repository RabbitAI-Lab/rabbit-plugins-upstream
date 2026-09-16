## Description:

Migrate or upgrade heavy stateful OpenClaw agents with rehearsal, embedding safety, rollback, and live proof.

This skill is ready for commercial/non-commercial use.

## Publisher:

[posthuman](https://clawhub.ai/user/posthuman)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to plan, rehearse, execute, verify, and roll back major migrations of stateful OpenClaw agent deployments that include gateways, shared state, plugins, credentials, local embeddings, and external supervisors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live migration guidance may involve service state, backups, supervisors, credentials, plugins, and rollback workflows.

Mitigation: Rehearse on a restored private copy, fence writers, keep verified backups private, and review each proposed live mutation before approval.

Risk: Operational evidence can expose sensitive user content, credentials, private paths, raw configuration, transcripts, messages, or database rows.

Mitigation: Record only redacted categories, counts, hashes, prompt categories, and status; keep backups and failed-state artifacts protected like live state.

Risk: State rollback can discard later changes or desynchronize ratcheted channels when the known-good release cannot read migrated state.

Mitigation: Attempt code-only rollback first, preserve failed state and redacted logs, and restore pre-migration state only when that rollback layer is justified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/posthuman/skills/stateful-agent-migration)
- [Publisher profile](https://clawhub.ai/user/posthuman)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Operational guidance]

**Output Format:** [Markdown with inline shell command blocks and structured operational checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses redacted category, count, and hash evidence; avoids credentials, raw configuration, transcripts, messages, and SQLite row contents.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
