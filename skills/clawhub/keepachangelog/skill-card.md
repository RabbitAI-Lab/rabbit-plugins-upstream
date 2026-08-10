## Description:

Maintain CHANGELOG.md in Keep a Changelog 1.1.0 format.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nanookai](https://clawhub.ai/user/nanookai)

### License/Terms of Use:

MIT

## Use Case:

Developers and release maintainers use this skill to create, update, release, and audit CHANGELOG.md files that follow Keep a Changelog 1.1.0 and Semantic Versioning conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated changelog entries can misstate user-visible impact when commit messages are ambiguous or overly technical.

Mitigation: Review generated entries against the actual changes before publishing a release.

Risk: Cutting a release changes headings, dates, and compare links in CHANGELOG.md.

Mitigation: Inspect the resulting diff and confirm the release version, ISO date, and link references before tagging or publishing.

Risk: Backfilling history from tags can omit or merge changes if the selected tag range is too broad.

Mitigation: Confirm the backfill range and compare changelog sections against the repository tag list.

## Reference(s):

- [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)
- [Changelog template](references/template.md)
- [ClawHub skill page](https://clawhub.ai/nanookai/skills/keepachangelog)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown guidance and CHANGELOG.md edits with inline shell commands when repository history is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply changelog entries, release headings, dates, and compare links based on repository tags and commit history.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
