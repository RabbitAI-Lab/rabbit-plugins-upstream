## Description:

Refreshes a skill in a skills repository by researching current usage and documentation, proposing changes for approval, updating its version and changelog, validating changes, and monitoring the release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and skill maintainers use this skill to check a repository skill for stale guidance, review proposed updates, and release approved changes with a version bump and changelog entry.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checkout cleanup may delete newly appearing files outside the selected skill directory without separate explicit approval.

Mitigation: Review the exact paths and diffs and require explicit approval before any cleanup outside the selected skill directory, especially for files created after the run starts.

Risk: Approved updates can be committed and pushed to a public repository.

Mitigation: Review the full diff and privacy scan findings before approving the commit and push.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/tenequm/skills/update-skill)
- [Skill homepage (author-declared; import provenance unavailable)](https://github.com/tenequm/skills/tree/main/skills/update-skill)
- [Keep a Changelog 2.0.0](https://keepachangelog.com/en/2.0.0/)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands]

**Output Format:** [Markdown report and proposed or approved repository file changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Approval gates before edits and before commit or push; validates changes and monitors CI when available.]

## Skill Version(s):

0.8.5 (source: SKILL.md metadata, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
