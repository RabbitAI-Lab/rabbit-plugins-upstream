## Description:

Refreshes one skill in a skills repository by researching usage, upstream changes, and documentation, then proposing gated edits, version updates, changelog changes, validation, commit, and CI checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to check and refresh a single agent skill in a skills repository, with human approval before edits and before commit or push.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can prepare repository edits that change a skill's behavior.

Mitigation: Review the Phase 3 proposed edits before approving the edit gate.

Risk: External research sources can introduce incorrect, stale, or private information into proposed changes.

Mitigation: Require primary-source verification and run the privacy scan before commit.

Risk: Approved commits or pushes can publish repository changes.

Mitigation: Review the Phase 6 diff carefully before approving the commit and push gate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tenequm/skills/update-skill)
- [Project Homepage](https://github.com/tenequm/skills/tree/main/skills/update-skill)
- [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/)
- [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports with proposed edits, changelog entries, diffs, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires human approval before applying edits and before commit or push.]

## Skill Version(s):

0.8.3 (source: frontmatter, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
