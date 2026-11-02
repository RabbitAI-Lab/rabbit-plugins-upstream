## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work. Use for monthly reporting or an explicitly requested month.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers of CI Tools use this skill to prepare evidence-based monthly release and merge request digests, including migration notes and a clearly separated snapshot of open work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A digest or proposed changes could be inaccurate or misleading if source evidence is incomplete or interpreted incorrectly.

Mitigation: Stop when collection encounters API, pagination, or timestamp errors; verify report claims and source links, then review the merge request before merging.

Risk: GitLab access or scheduled publishing could affect a broader scope than intended.

Mitigation: Use an account scoped to the intended project and enable the monthly schedule only when wanted.

## Reference(s):

- [CI Tools Monthly Digest on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-ci-tools-digest)
- [CI Tools GitLab project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown monthly digest and merge request link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers one UTC calendar month; labels incomplete previews as month to date and separates open merge requests from shipped work.]

## Skill Version(s):

4.230.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
