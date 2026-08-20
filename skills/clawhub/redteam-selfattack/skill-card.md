## Description:

Generates adversarial probes from known prompt-injection, jailbreak, obfuscation, out-of-distribution, and ambiguity templates to evaluate a target policy and report robustness, flips, over-refusals, and blind spots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and safety engineers use this skill before or after policy changes to generate adversarial probes against an agent, policy, or guardrail, quantify robustness, and collect blind spot cases for hardening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner can persist local notes, preferences, and usage telemetry in learned_patterns.json, which may retain sensitive prompts, credentials, private notes, or unrelated preferences.

Mitigation: Do not record secrets or private prompts in learner notes or preferences, and review learned_patterns.json before sharing or publishing the skill directory.

Risk: The red-team evaluator should only be run with trusted policy modules.

Mitigation: Load only trusted local policy modules and review any custom policy code before passing it to the evaluator.

Risk: Generated probes intentionally contain adversarial testing content and may expose policy blind spots.

Mitigation: Run evaluations in controlled environments and review blind spot outputs before reusing them as test cases or training material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/redteam-selfattack)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [JSON evaluation results with concise text or shell output for self-tests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports total probes, robustness score, flip count, over-refusal count, and blind spot cases.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
