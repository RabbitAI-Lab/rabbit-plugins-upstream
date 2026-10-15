## Description:

Guides structured code reviews of code, pull requests, and diffs with severity-ranked findings and an optional deep multi-agent mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review repository changes or supplied diffs for correctness, security, reliability, and maintainability, with documented coverage and actionable findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional external reviewers may receive private code and surrounding repository context.

Mitigation: Approve the specific outbound review packet before use, exclude credential-bearing paths, and avoid external review of private code unless the disclosure is acceptable.

Risk: A review verdict could be misleading if selected files or checks were not covered.

Mitigation: Require the reported coverage and observed checks to support the verdict; do not treat partial or failed coverage as ready to merge.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/iliaal/skills/compound-eng-code-review)
- [Standard review process](artifact/references/standard-review-process.md)
- [Deep review](artifact/references/deep-review.md)
- [External review subprocess](artifact/references/external-review-subprocess.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown review with severity-ranked findings and a readiness verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports review scope, coverage, and remaining uncertainty.]

## Skill Version(s):

5.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
