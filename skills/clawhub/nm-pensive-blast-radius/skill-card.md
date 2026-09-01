## Description:

Analyzes code change impact with risk scoring and affected-node mapping before merge decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and code reviewers use this skill before merging changes to identify affected code paths, missing test coverage, and higher-risk nodes that need closer review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Impact results can be incomplete or noisy when graph tooling is unavailable and fallback search relies on repository text matching.

Mitigation: Review the affected-node table before acting and narrow rg/grep searches by language or path when the repository is large or mixed-language.

Risk: Optional gauntlet graph data may be missing, stale, or outside this skill's own security review scope.

Mitigation: Build or refresh the graph before relying on graph-based findings, and review the gauntlet dependency separately before use.

Risk: The skill runs local repository inspection commands and may surface sensitive filenames or code context in its response.

Mitigation: Run it only in intended repositories and review generated analysis before sharing it outside the project team.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-pensive-blast-radius)
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown analysis with a prioritized risk table, affected-node notes, and action recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local read-only command output from git diff, rg/grep, and optional graph tooling when available.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
