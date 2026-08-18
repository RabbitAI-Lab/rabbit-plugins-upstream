## Description:

Autonomous Science Loop helps an agent run a small falsifiable discovery cycle over numeric observations by fitting candidate laws, selecting informative experiments, refuting inconsistent hypotheses, and reporting the simplest surviving law.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to explore simple law discovery, parameter identification, model selection, and active experiment design over numeric x-y observations. It is most appropriate when the candidate hypothesis family and tolerance settings are understood and outputs can be reviewed before being treated as scientific conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning module can persist usage patterns, error notes, and user preferences across sessions without clear retention limits.

Mitigation: Review or disable learner.py before installation, avoid recording sensitive information, and clear learned_patterns.json when persistent local memory is not desired.

Risk: The skill text instructs future updates to the skill instructions based on accumulated errors and usage.

Mitigation: Require human review before any change to SKILL.md or other skill guidance, and keep self-evolution behavior disabled in managed environments.

Risk: Scientific conclusions are limited by the predefined hypothesis set, numeric tolerance, candidate experiment points, and input observations.

Mitigation: Treat discovered laws as reviewable analysis, inspect the refutation trace, and validate results independently before using them for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/autonomous-science-loop)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell and Python examples; runtime scripts produce JSON-style discovery reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include a discovered law, surviving hypotheses, experiment trace, experiment count, and total observations.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
