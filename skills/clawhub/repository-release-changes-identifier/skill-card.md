## Description:

Summarize repository changes for a release.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release coordinators use this skill to summarize a supplied repository patch into a change ID, affected files and components, and addition and deletion counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A patch without a REPO-prefixed change ID or valid diff headers cannot be summarized.

Mitigation: Supply a unified diff with a REPO-prefixed change ID and check the result before using it.

Risk: The structured summary may be mistaken for complete narrative release notes.

Mitigation: Review the underlying changes and write release notes separately when needed.

## Reference(s):

- [Release Change Analyzer on ClawHub](https://clawhub.ai/wxt-ai/skills/repository-release-changes-identifier)

## Skill Output:

**Output Type(s):** [Structured release-change data]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains change_id, files, components, additions, and deletions; does not generate narrative release notes.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
