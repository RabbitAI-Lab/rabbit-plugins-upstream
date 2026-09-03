## Description:

Detects time and space complexity hotspots with static AST analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and code reviewers use this skill to scan changed files or a specified path for likely time and space complexity hotspots before performance-sensitive merges or optimization work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate on broad performance-related phrasing and inspect changed repository files when no explicit path is provided.

Mitigation: Use an explicit file or directory path when the review should be scoped tightly.

Risk: Optional gauntlet and kuva integrations may read local code graphs or benchmark outputs.

Mitigation: Review local graph and benchmark inputs before using optional integrations, and treat the generated findings as advisory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-pensive-performance-review)
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report grouped by severity with file, line, message, suggestion, and tier coverage.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are informational and should be confirmed with profiling or benchmark evidence before fixes are treated as complete.]

## Skill Version(s):

1.9.19 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
