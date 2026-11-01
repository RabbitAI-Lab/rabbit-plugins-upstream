## Description:

Automatically assess task complexity and adjust reasoning level. Triggers on every user message to evaluate whether extended thinking (reasoning mode) would improve response quality. Use this as a pre-processing step before answering complex questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seairteng](https://clawhub.ai/user/seairteng)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to assess request complexity and select a suitable reasoning effort before answering, while avoiding escalation for routine or time-sensitive requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Increasing reasoning effort can increase response time and usage cost.

Mitigation: Escalate only when the expected quality benefit justifies the added time and cost.

Risk: An appended reasoning icon can interfere with strict output formats.

Mitigation: Omit the icon when the requested format requires exact output.

Risk: Reasoning-control commands may not be supported by every agent.

Mitigation: Confirm the target agent supports the referenced controls before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/seairteng/skills/adaptive-reasoning)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Natural-language response, optionally including a reasoning-mode indicator or control suggestion]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include an optional reasoning icon; omit it when strict output formatting requires exact content.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
