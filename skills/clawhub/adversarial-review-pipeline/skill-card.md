## Description:

Reviews code changes for correctness, security issues, edge cases, and unnecessary complexity through a severity-graded workflow with optional multi-agent review and browser verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[djc00p](https://clawhub.ai/user/djc00p)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to review a diff, branch, or pull request before merge and identify concrete correctness, security, testing, and scope issues. It offers single-agent review by default, with optional multi-agent pipelines for larger or user-facing changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but coverage is partial because two local path-like references could not be resolved.

Mitigation: Review the referenced guidance and generated findings before relying on them; the assessment is not a guarantee of safety.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/djc00p/skills/adversarial-review-pipeline)
- [Review Checklists](references/review-checklists.md)
- [Three-Agent Pipeline](references/three-agent-pipeline.md)
- [Five-Agent Pipeline](references/five-agent-pipeline.md)
- [Rails Review Checks](references/rails-review-checks.md)
- [Rails System Spec Review](references/rails-system-spec-review.md)
- [Rails Turbo and Controller Traps](references/rails-turbo-and-controller-traps.md)
- [Rails Money and State Checks](references/rails-money-and-state-checks.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Test specifications, Shell commands, Guidance]

**Output Format:** [Markdown review reports, with optional code fixes, test specifications, and browser verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tiered workflow; multi-agent stages and browser verification are optional.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
