## Description:

Self-improving DRT/ICT trading agent that journals trades, analyzes win/loss patterns, and builds a local trading memory over time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading analysts use this skill to record DRT/ICT trade outcomes locally and review pattern-based summaries that can inform future trading discipline. Its analysis should be treated as informational support, not automated financial advice or account control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local trade history is stored in the skill directory.

Mitigation: Review whether storing trade history locally is acceptable before using the journal workflow.

Risk: Trading suggestions or pattern summaries could be mistaken for automated financial advice.

Mitigation: Treat outputs as informational analysis only and do not connect the skill to account control or automated trading execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/northcap-group/skills/drt-self-improving-agent)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with command-line examples and local analysis text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes trade history to a local JSON file in the skill data directory.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
