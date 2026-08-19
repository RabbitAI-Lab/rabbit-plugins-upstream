## Description:

Provides a vault data governance standard for daily auditing, cleanup, deduplication, and archiving of collected, reviewed, and research data across agent workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[managernet](https://clawhub.ai/user/managernet)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and workspace maintainers use this skill to standardize vault maintenance: auditing collected data, moving outdated or invalid files into archives, deduplicating records, and reporting cleanup results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad authority to move files across team workspaces during cleanup.

Mitigation: Run only in explicit maintenance windows with path allowlists, dry-run output, and diff review before any file move.

Risk: The skill includes repository commit and push steps that could publish unintended cleanup changes.

Mitigation: Require operator approval before git commit or push, and review the staged diff before publishing.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and a cleanup report template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to guide operator-reviewed maintenance actions; the skill text includes file move, archive, commit, and push steps.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
