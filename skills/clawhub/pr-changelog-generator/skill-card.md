## Description:

Generates pull request descriptions, changelog entries, release notes, and version-bump guidance from git history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heroinyan-stack](https://clawhub.ai/user/heroinyan-stack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release managers use this skill to summarize branch diffs and commits into PR descriptions, changelog entries, release notes, and semantic version recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may summarize more repository history or diff content than intended if the branch, base branch, or commit range is ambiguous.

Mitigation: Specify the exact branch, base branch, or commit range before asking the agent to generate PR or release documentation.

Risk: Generated release documentation can be incomplete or misleading if reviewed without checking the underlying commits and diffs.

Mitigation: Review generated PR descriptions, changelog entries, release notes, and version-bump recommendations against the actual code changes before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heroinyan-stack/skills/pr-changelog-generator)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown and plain text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [PR descriptions are intended to stay concise; changelog and release-note output follows existing project formatting when available.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
