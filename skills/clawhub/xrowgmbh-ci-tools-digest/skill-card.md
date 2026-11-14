## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

CI Tools maintainers and developers use this skill to collect release and merge request evidence for a UTC calendar month, write a linked English digest, and submit it through a merge request for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reported medium confidence and partial Skillspector coverage because a referenced local path could not be matched to a bundled artifact.

Mitigation: Review the skill files and confirm the referenced collector path before installation; the scan is not a guarantee of safety.

Risk: Collecting and submitting a digest uses shell tools and GitLab access.

Mitigation: Use a trusted GitLab token, then review the collected evidence, source links, and merge request before approval.

## Reference(s):

- [CI Tools GitLab project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [English Markdown monthly digest with source links and a merge request status summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one UTC calendar month and separates releases, merged merge requests, and the current snapshot of open work.]

## Skill Version(s):

4.236.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
