## Description:

Monitors an agent's confidence, uncertainty, novelty, scope fit, and task necessity to recommend whether to proceed, degrade, seek help, defer, or flag overconfidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to add a local metacognitive gate before or during longer-running tasks. It converts numeric self-assessment signals into conservative meta-decisions and calibration checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learning feature can retain local history about decisions, errors, notes, and preferences.

Mitigation: Inspect learned_patterns.json before use, avoid recording sensitive notes or preferences, and clear the file when persistent local history is not desired.

Risk: The artifact describes adaptive rewriting of SKILL.md after repeated calibration alerts or usage thresholds.

Mitigation: Require manual review before any skill file rewrite and do not allow unattended updates to operational skill instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/metacognitive-monitoring)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [JSON decision objects, plain text command output, and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local standard-library scripts can emit verdicts, actions, calibration status, and learning insights.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
