## Description: <br>
Detects friction signals during agent sessions and graduates recurring patterns into reviewed rules for future guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill for session retrospectives, local friction logging, and review-driven promotion of recurring agent workflow issues into durable guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Session-derived friction logs can persist local project context under ~/.claude/friction. <br>
Mitigation: Use only where local logging is acceptable, review or purge friction logs as needed, and avoid highly sensitive projects without additional redaction or encryption controls. <br>
Risk: Recurring patterns may influence future agent behavior through LEARNINGS.md entries or rule proposals. <br>
Mitigation: Review proposed graduations before relying on them, and require explicit approval before any permanent CLAUDE.md or skill update. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-abstract-friction-detector) <br>
- [claude-night-market abstract plugin](https://github.com/athola/claude-night-market/tree/master/plugins/abstract) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown reports, JSON session-capture records, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local friction session logs under ~/.claude/friction and add reviewed recurring patterns to LEARNINGS.md.] <br>

## Skill Version(s): <br>
1.9.16 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
