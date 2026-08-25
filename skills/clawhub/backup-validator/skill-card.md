## Description:

Validates OpenClaw backup artifacts before push by checking skill structure, secret leaks, Termux compatibility, and repository status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to validate local OpenClaw backup folders before committing or pushing changes. It helps identify missing backup structure, malformed skill files, possible secret exposure, Termux compatibility issues, and repository readiness problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Suggested git cleanup commands could discard local work if followed without review.

Mitigation: Review any suggested git cleanup command before allowing it, and prefer non-destructive recovery steps unless destructive cleanup is explicitly intended.

Risk: A PASS result can be mistaken for proof of complete backup integrity.

Mitigation: Treat PASS as a local validation result only, and separately run hash, permission, and restore checks when full backup integrity matters.

## Reference(s):


## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown validation report with status, details, and recovery actions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces PASS, FAIL, or WARNING summaries for local backup validation.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter lists 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
