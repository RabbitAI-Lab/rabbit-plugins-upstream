## Description:

Applies lexical adversarial perturbations to text decision systems, reports robustness scores and flipped decisions, and suggests normalization-based hardening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill before deploying text classifiers, moderation systems, or routing decisions to test how small character-level perturbations affect outcomes. It can also support red-team reviews by locating minimal text changes that flip a decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner module can keep local plain-text evaluation history, notes, and preferences.

Mitigation: Avoid recording sensitive inputs, review the stored learning file, or disable learner.py usage when stateless runs are required.

Risk: The artifact describes a flow where accumulated results may lead to updates to SKILL.md.

Mitigation: Require human review before any automatic or agent-proposed changes to skill instructions are accepted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/adversarial-robustness)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON robustness results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, dependency-free Python scripts generate perturbation results and learner insights.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
