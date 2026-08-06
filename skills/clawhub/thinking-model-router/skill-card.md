## Description:

When unsure which thinking skill fits, map domain and problem type, then return NONE or one primary skill by default (at most three complementary).

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill when the best thinking skill is unclear and they need a concise route to NONE, one primary skill, or a small set of distinct complementary skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The router may influence an agent to choose an unsuitable thinking skill for a task.

Mitigation: Use the built-in stop and falsification checks; return NONE when no candidate clearly improves the work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-model-router)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Structured plain text routing recommendation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns outcome, route identifiers, domain, problem type, constraints, rationale, blind spots, and exit guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
