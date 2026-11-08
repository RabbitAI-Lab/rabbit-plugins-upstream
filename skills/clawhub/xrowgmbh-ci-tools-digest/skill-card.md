## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use the skill to prepare an evidence-based English CI Tools report for a complete UTC calendar month, including release and merged merge-request activity, migration notes, and a separately dated open-work snapshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The collector accesses GitLab through the glab command, while runtime permissions are unknown and the security evidence is incomplete.

Mitigation: Use a narrowly scoped GitLab token and review the collected period, counts, source links, and claims before opening a merge request.

Risk: The generated digest is English-only and may not fit every audience.

Mitigation: Confirm English is appropriate for the intended readers before publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-digest)
- [CI Tools GitLab project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Analysis]

**Output Format:** [English Markdown with release and merge counts, substantive themes, migration notes, open work, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one complete UTC calendar month; month-to-date previews must be labeled clearly.]

## Skill Version(s):

4.233.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
