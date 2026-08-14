## Description:

Trigger /devil to pressure-test a decision through a multi-model council, fact-check pass, peer review, and a mandatory devil's-advocate stress test.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiingsai](https://clawhub.ai/user/kiingsai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to pressure-test real decisions with meaningful tradeoffs. It gathers available context, runs a multi-agent council, checks factual claims, applies peer review and adversarial stress testing, then returns a confidence-rated recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can spawn many sub-agents and may use web or browser tools to gather facts.

Mitigation: Enable it only for decision-review workflows where that level of agent activity and external lookup is acceptable.

Risk: Broad natural-language triggers such as "what would you do" may activate the skill in agents with aggressive auto-routing.

Mitigation: Narrow or disable broad trigger phrases when installing in environments where unintentional activation would be disruptive.

Risk: Decision facts may be sent to sub-agents or alternate model providers during the multi-model council process.

Mitigation: Avoid using the skill with confidential or sensitive decisions unless the configured agent and model providers are approved for that data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiingsai/skills/devils-advocate)
- [GitHub repository](https://github.com/kiingsai/devils-advocate)
- [Imported commit](https://github.com/kiingsai/devils-advocate/commit/4c9e5ac899f3afb2e57bc615b0a404cd4aeab0eb)
- [Andrej Karpathy GitHub profile](https://github.com/karpathy)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown verdict with structured sections and inline fact-check notes when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs a direct response; optional transcript logging or scheduled follow-up occurs only when the user explicitly asks or opts in.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
