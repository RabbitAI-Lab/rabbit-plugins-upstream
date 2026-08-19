## Description:

Self-Eval helps an agent score its own responses with a structured rubric, optional reference-answer comparison, JSON scoring output, and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to evaluate generated responses before delivery, compare candidate outputs, and capture repeated quality feedback as reusable rubric signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can save evaluation reports and local learning records, which may contain submitted task details, notes, preferences, or evaluation material.

Mitigation: Use report output and learner commands only for material that is appropriate to persist locally; avoid secrets, private user content, and sensitive evaluation details in notes, keys, values, and graded outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/self-eval)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The grading script can write a local JSON evaluation report; learner commands can update a local learned_patterns.json file.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
