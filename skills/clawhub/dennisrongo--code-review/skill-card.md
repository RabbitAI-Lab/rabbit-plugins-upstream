## Description:

Code Review helps agents inspect working-tree or branch changes, run detected tests and builds, and report production-readiness findings without editing code unless fixes are approved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dennisrongo](https://clawhub.ai/user/dennisrongo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review uncommitted changes, pull requests, or branches for correctness, DRY/design issues, test coverage, security, and production readiness. It is intended to produce an evidence-backed review report before any optional fixes are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may run detected local tests and builds during reviews.

Mitigation: Install only when local command execution during code review is acceptable, and inspect reported commands and outputs.

Risk: Review recommendations could be incorrect or incomplete if repository context is misunderstood.

Mitigation: Require findings to cite opened code context, searches, and command output, and have a human review recommendations before applying changes.

Risk: Optional fixes can modify repository files after the review.

Mitigation: Apply edits only after explicit user approval, limited to the selected findings.

## Reference(s):

- [Branch Scope Review](references/branch-review.md)
- [ClawHub Skill Page](https://clawhub.ai/dennisrongo/skills/code-review)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown review report with categorized findings and quoted command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected test/build command status, file and line citations, branch task verdicts, and recommended fixes awaiting user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
