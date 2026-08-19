## Description:

Long Horizon Planner decomposes high-level goals into milestone dependency DAGs and provides topological sorting, critical-path analysis, next-action recommendations, progress updates, and Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and operators use this skill to turn large multi-step goals into auditable milestone plans with dependencies, estimated durations, critical paths, and immediately actionable next steps. It is useful when long-running work needs a stable plan anchor and iterative progress reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can keep persistent local memory about usage, errors, notes, and user preferences.

Mitigation: Avoid recording sensitive goals, notes, or preferences, and clear learned_patterns.json when retained memory is no longer needed.

Risk: The skill encourages updating installed skill instructions based on accumulated experience.

Mitigation: Require manual review before allowing updates to SKILL.md or other installed skill instruction files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/long-horizon-planner)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with bash commands; the planner CLI can create JSON plan files and Markdown progress reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic planning output with optional persistent local learning state in learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
