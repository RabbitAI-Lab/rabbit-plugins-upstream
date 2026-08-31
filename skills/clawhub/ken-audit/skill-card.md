## Description:

Audits the whole repository for Thompson-mode violations and returns a ranked list of what to rewrite, delete, or take back into the trusted base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rajnandan1](https://clawhub.ai/user/rajnandan1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review an entire repository for code simplification opportunities, focusing on ranked Thompson-mode findings and the likely rewrite, deletion, or trusted-base reduction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-wide audit guidance may recommend rewrites, deletions, or dependency reductions that need human review before implementation.

Mitigation: Review each ranked finding manually before changing code, and treat the output as guidance rather than an automatic patch plan.

Risk: The skill is scoped to Thompson-mode method violations and does not cover correctness bugs, security holes, or performance issues.

Mitigation: Route correctness, security, and performance concerns to a normal review pass outside this skill's output.

Risk: The skill should inspect only the current repository and its git history.

Mitigation: Do not permit it to modify files or access unrelated systems when running the audit.

## Reference(s):

- [Project homepage](https://github.com/rajnandan1/ken)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with ranked one-line findings and a final net summary.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only audit output; the skill lists findings and applies no changes.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
