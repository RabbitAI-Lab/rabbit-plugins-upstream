## Description: <br>
Capability Evolver analyzes AI agent runtime logs to detect error patterns, regressions, and inefficiencies, then generates health scores and structured improvement proposals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kennyzir](https://clawhub.ai/user/kennyzir) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to analyze agent runtime logs, diagnose recurring failures, monitor system health, and generate prioritized reliability or improvement recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Runtime logs may contain credentials, personal data, or sensitive internal details. <br>
Mitigation: Redact credentials, tokens, personal data, and sensitive internal details before sending logs to the skill. <br>
Risk: Generated recommendations may be unsuitable for automatic tasks or long-lived records without review. <br>
Mitigation: Review recommendations before turning them into automated work items, persistent records, or production changes. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kennyzir/capability-evolver-pro) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, guidance] <br>
**Output Format:** [JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns analyze, evolve, or status results; analyze and evolve require structured log entries and can include health scores, detected patterns, recommendations, risk assessment, and execution metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
