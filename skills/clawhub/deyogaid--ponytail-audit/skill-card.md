## Description:

Audit the whole repo for over-engineering. A ranked list of what to delete, simplify, or replace with stdlib or native features.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deyogaid](https://clawhub.ai/user/deyogaid)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scan an entire repository and get a ranked list of complexity reductions, such as deletions, simpler implementations, and standard library or native replacements. It reports suggestions only and does not make changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Complexity findings do not assess correctness, security, or performance, and suggestions may be unsuitable without review.

Mitigation: Review suggestions before implementation and use a normal review pass for correctness, security, and performance concerns.

## Reference(s):

- [Ponytail project homepage](https://github.com/DietrichGebert/ponytail)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Ranked one-line Markdown findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists findings only; makes no changes.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
