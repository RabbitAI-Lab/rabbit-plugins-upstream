## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to prepare a monthly CI Tools release digest with migration notes and a separately dated view of open work, then submit it through the project's review process.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses GitLab network and shell capabilities, including a `glab` subprocess call.

Mitigation: Review the requested GitLab access and `glab` authentication scope before running it.

Risk: The security scan is partial because a referenced local path was missing.

Mitigation: Review the complete installed skill and its referenced files before deployment.

## Reference(s):

- [CI Tools Monthly Digest on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-digest)
- [xrow-public/ci-tools project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [English Markdown calendar-month digest with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the reporting period and counts, release and merged-change themes, migration notes, and a separately dated snapshot of open work.]

## Skill Version(s):

4.235.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
