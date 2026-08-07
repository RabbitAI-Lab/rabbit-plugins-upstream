## Description:

When a claim, doc, test, metric, or assumption conflicts with observed behavior, stop theorizing from the map and verify the live code or data; let territory overrule.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and reviewers use this skill when documentation, tests, metrics, assumptions, or other models conflict with observed code or data. It guides the agent to verify current sources, record the observed delta, and update its understanding before deciding what to change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may suggest reading files, running checks, querying data, or reproducing behavior to resolve a model-versus-observation conflict.

Mitigation: Limit checks to sources relevant to the current task and avoid privileged or sensitive access unless the user has authorized it.

Risk: The skill can be over-applied when the mismatch cannot affect the next decision or when the map is itself the task artifact.

Mitigation: Use the documented over-application guard and stop once the contradiction is resolved or irrelevant.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tjboudreaux/skills/thinking-map-territory)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Structured text or Markdown using Map, Territory check, Observation, Delta, Updated model, Action, and Uncovered fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
