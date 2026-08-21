## Description:

Generate a daily standup report from git commit history, grouping commits by author with recent work, planned work prompts, and blockers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineering managers, and remote teams use this skill to turn recent repository commits into standup talking points for daily or weekly status updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads recent commit subjects from the repository path supplied by the user.

Mitigation: Review the repository path before running the command, especially in automation or shared environments.

Risk: JSON output may include unusual commit text without escaping.

Mitigation: Inspect or sanitize JSON-mode output before piping it into downstream automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/git-standup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain-text standup report or JSON summary generated from git commit subjects.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires git and a local repository with commit history; optional filters include lookback hours, author, repository path, and text or JSON output.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
