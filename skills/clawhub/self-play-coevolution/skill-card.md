## Description:

Self-play coevolution helps an agent alternate between proposer and critic roles to iteratively generate candidates, find flaws, raise the difficulty level, and improve outputs through a closed feedback loop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to run a self-play proposer/critic loop that generates candidates, critiques them against escalating checks, and records convergence, scoring, and regression-detection traces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learning module can persist usage, errors, notes, and preferences across runs.

Mitigation: Review the skill before installation, avoid recording sensitive information, and disable learner.py usage or clear learned_patterns.json in shared or sensitive environments.

Risk: Persistent local learning lacks clear consent and retention controls in the release evidence.

Mitigation: Set explicit local retention practices before use and remove stored learning data when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/self-play-coevolution)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON-style coevolution traces]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The coevolution script returns round-by-round levels, candidates, scores, flaws, critic escalations, convergence status, and regression detection state.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
