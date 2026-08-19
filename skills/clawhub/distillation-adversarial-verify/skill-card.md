## Description:

Validates distilled decision rules or student skills against adversarial cases, scoring per-rule robustness and overall distillation quality while flagging weak rules for retraining.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before releasing distilled skills or extracted decision rules to test whether those rules still hold under adversarial cases and identify rules that need rework.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running verification against an untrusted target skill can execute that skill's Python rule file.

Mitigation: Review before installing and run verification against untrusted skills only inside a sandbox.

Risk: The bundled learning subsystem stores local usage history, error patterns, and preferences.

Mitigation: Remove or disable the learner and memory files unless local history storage is explicitly desired, and inspect or delete learned_patterns.json regularly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/distillation-adversarial-verify)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON report with command-line usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports per-rule robustness, flips, weighted overall quality, verdict, and weak rules.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
