## Description:

Evaluates generated text against helpful, harmless, and honest principles using local heuristic checks, returning principle scores, issues, and a pass/fail result before publication or user-facing output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill as a local pre-publication alignment gate to flag harmful requests, overconfident claims, and low-actionability responses. It is also useful for red-team checks that test whether simple rule-based boundaries are being enforced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner can persist free-form notes and preferences in learned_patterns.json.

Mitigation: Do not record raw prompts, confidential text, or harmful-content examples; review or delete learned_patterns.json regularly.

Risk: Suggested rule updates could change future alignment evaluations.

Mitigation: Require human review before applying any suggested changes to SKILL.md or rule patterns.

Risk: The checker uses heuristic regular expressions and may miss nuanced harmful content or overstate alignment quality.

Mitigation: Use it as a first-pass gate and keep human or stronger policy review for high-risk outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/value-alignment)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON alignment report and command-line text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports helpful, harmless, honest, overall, pass, and issues fields; learner commands may update learned_patterns.json.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
