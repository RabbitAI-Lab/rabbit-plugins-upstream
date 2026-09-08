## Description:

Tracks and optimizes OpenClaw MEMORY.md long-term memory by recording usage, reporting hot and cold entries, and proposing promotion, archive, or cleanup actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smliences](https://clawhub.ai/user/smliences)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to inspect long-term memory usage patterns and decide which entries should stay prominent, move to archive, or be cleaned up after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead an agent to mark, archive, or clean persistent MEMORY.md content.

Mitigation: Run the default report mode first and require user review before applying archive, cleanup, or mark workflows.

Risk: Weekly automation or apply-style workflows may create ongoing tracking logs, archive moves, annotations, and backup-to-trash cleanup.

Mitigation: Enable automation only for users who explicitly want ongoing memory maintenance and review each generated change summary.

Risk: Memory usage tracking records local entry keys and access signals over time.

Mitigation: Keep tracking files in the local workspace and avoid recording sensitive content beyond the entry key needed for maintenance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smliences/skills/memory-tuner)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown report by default, optional JSON report, and concise guidance with shell commands or configuration when setup is requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default analysis is dry-run; optional mark and disposition workflows can annotate or change persistent memory files after user review.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
