## Description: <br>
Detect friction signals, track recurring patterns, and propose durable learning rules for agent session retrospectives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill after or during agent sessions to identify repeated friction, summarize recurring patterns, and propose user-reviewed guidance updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local friction logs and learning records may contain sensitive details from agent sessions. <br>
Mitigation: Use the skill only when local persistence under ~/.claude is acceptable, and periodically review or delete those records if sessions include sensitive work. <br>
Risk: Graduated guidance proposals could encode misleading patterns if friction signals are noisy or context-specific. <br>
Mitigation: Review proposed Tier 2 and Tier 3 updates before accepting them, and keep the documented constraint that CLAUDE.md is not modified automatically. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-friction-detector) <br>
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown reports with JSON session records and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local friction session logs and update local learning records under ~/.claude when used as described.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
