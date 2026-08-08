## Description:

Use under time pressure when the situation is still changing and you must act before certainty - cycle Observe, Orient, Decide, Act on about 70% confidence, then re-observe.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill during incidents, outages, intermittent failures, live traffic shifts, and other moving situations where waiting for full certainty costs more than a reversible action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may apply the 70% confidence rule to irreversible, high-impact, or poorly scoped actions.

Mitigation: Use the skill only for reversible actions with a clear rollback or degrade path; escalate or gather more evidence when the next step is irreversible.

Risk: Users may keep cycling without re-observing or without a near-term observation that can refute the action.

Mitigation: Require each action to include a predicted effect, a time box, and an immediate re-observation; stop looping when those cannot be named.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-ooda)
- [Publisher profile](https://clawhub.ai/user/tjboudreaux)

## Skill Output:

**Output Type(s):** [guidance, markdown]

**Output Format:** [Markdown cycle record]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces repeated OODA loop records with observed signals, hypotheses, action, confidence, predicted effect, result, and loop status.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
