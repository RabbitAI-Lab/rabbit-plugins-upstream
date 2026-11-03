## Description:

Produce an English CI Tools digest for a complete calendar month, with release evidence, migration notes and clearly separated open work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and CI Tools maintainers use this skill to produce an English digest for a complete UTC calendar month, including release evidence, migration notes, and separately dated open work. It prepares the report for review in a merge request in xrow-public/ci-tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: GitLab permissions and external review gates depend on the user's environment and were not verified.

Mitigation: Configure glab for the intended GitLab host with appropriately scoped credentials, review each digest merge request, and enable the monthly schedule only if desired.

## Reference(s):

- [CI Tools GitLab project](https://gitlab.com/xrow-public/ci-tools)

## Skill Output:

**Output Type(s):** [Markdown, Files]

**Output Format:** [English Markdown monthly digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A complete UTC calendar-month report with release and merged-merge-request counts, source links, themes, migration notes, and a separately dated open-work snapshot.]

## Skill Version(s):

4.231.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
