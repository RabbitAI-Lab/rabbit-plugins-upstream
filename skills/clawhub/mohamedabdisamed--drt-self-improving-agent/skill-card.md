## Description:

Self-improving DRT/ICT trading agent that journals trades, analyzes win/loss patterns, and builds a local trading memory for future analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External traders and agent users use this skill to record DRT/ICT trade details locally, review performance patterns, and receive data-based reminders or rule suggestions. Its analysis is informational and should not be treated as financial advice or automated trading authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trade history is stored locally inside the skill directory.

Mitigation: Install and run the skill only where local storage of trade details is acceptable, and handle data/trades.json according to the user's data-retention needs.

Risk: Pattern analysis and rule suggestions may be mistaken for trading advice.

Mitigation: Treat the output as informational performance review only; keep human decision-making and trading risk controls outside the skill.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Shell commands, Files, Guidance]

**Output Format:** [CLI text output and local JSON trade journal entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3; stores trade history locally in data/trades.json and does not require API keys.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
