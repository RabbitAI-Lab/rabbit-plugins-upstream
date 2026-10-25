## Description:

Helps hospital facilities teams inspect isolation-room pressure, medical-gas supply, operating-room conditions, and equipment alarms across building and plant systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Hospital facilities engineers and operators use this skill to review building-system readings, identify pressure or ventilation exceptions, assess medical-gas source conditions, and investigate equipment alarms. Its checks support human review rather than replacing on-site alarms or infection-control decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An incorrect or stale assessment of isolation-room pressure, operating-room conditions, or medical-gas pressure could affect patient safety.

Mitigation: Have qualified facilities and clinical staff verify readings and thresholds against site policy, on-site alarms, and infection-control procedures before acting.

Risk: A BACnet property write could change safety-critical building or gas-system behavior despite the skill's read-first positioning.

Mitigation: Restrict activation to authorized facilities tasks; require site change-control approval and explicit confirmation before any write, especially on life-safety equipment.

Risk: Exports and stream publishing can distribute sensitive facility data outside the intended environment.

Mitigation: Disable or tightly scope exports and publishing until site policy approves destinations, permissions, and data handling.

## Reference(s):

- [iaiops-clinical on ClawHub](https://clawhub.ai/zw008/skills/iaiops-clinical)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration guidance, Shell commands]

**Output Format:** [Human-readable assessments and operational guidance, with cited readings and severity classifications when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prioritized exceptions, diagnostic findings, configuration drafts, and suggested next steps.]

## Skill Version(s):

0.32.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
