## Description:

When a symptom has several plausible causes, rank falsifiable hypotheses and run the cheapest discriminating observation first; prefer least-assumptive survivors only after evidence fit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to investigate bugs, incidents, or anomalies with multiple plausible causes by comparing falsifiable hypotheses and running cheap discriminating checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The method can be over-applied when a single cause is already directly evidenced.

Mitigation: Use it only when multiple serious hypotheses remain; otherwise test or fix the directly evidenced cause.

Risk: A debugging investigation may require the agent to inspect relevant project files or logs.

Mitigation: Limit inspection to task-relevant files and log excerpts, and follow the deployment environment's data-handling rules.

Risk: The agent may preserve a simpler explanation after new evidence contradicts it.

Mitigation: Drop falsified hypotheses after each observation and apply parsimony only among explanations that still fit the evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-scientific-method)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text structured as a hypothesis differential investigation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents the symptom, competing hypotheses, test order, observations, surviving explanations, localized fault, and ruled-out causes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
