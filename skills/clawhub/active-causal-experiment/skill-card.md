## Description:

Active Causal Experiment helps an agent choose information-rich interventions across competing causal hypotheses, update beliefs with Bayesian inference, and identify a likely causal structure with fewer experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to prototype active intervention selection for causal hypothesis testing, A/B-style intervention planning, and Bayesian comparison of competing causal structures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included learner module can keep local memory about usage history, errors, notes, and preferences without clear opt-in or retention controls.

Mitigation: Disable or remove the learner module unless persistent local memory is desired, or make it explicit opt-in with documented controls to inspect and delete learned_patterns.json.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with Python API references and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included scripts produce terminal traces, posterior summaries, and local JSON learning records when the learner module is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
