## Description:

Agent self-awareness of cognitive states - context fatigue, attention drift, memory debt, confidence erosion, and skill staleness - to detect, report, and mitigate degrading conditions before they cause failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to help agents monitor long-running sessions for cognitive-state degradation, report actionable state changes, and choose mitigations such as memory persistence, task re-anchoring, session splitting, or retry-loop recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill guides agents to save session summaries, decisions, TODOs, and state logs, which can expose sensitive, secret, or regulated information if written without boundaries.

Mitigation: Require explicit approval for memory or file writes, exclude secrets and regulated data, and review saved summaries before persistence.

Risk: The optional guardian cron workflow can create background logs and alerts without enough clarity about where data is stored or how long it is retained.

Mitigation: Enable the guardian only after configuring log location, retention, access controls, and deletion behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/agent-cognitive-states)
- [Server-resolved source repository](https://github.com/voronindenis5/agent-cognitive-states)
- [Detection heuristics](references/detection-heuristics.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Human-readable text, Markdown, and JSON reports with optional Python CLI commands and YAML cron configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The self-check script can return non-zero exit codes when medium or high severity states are detected.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
