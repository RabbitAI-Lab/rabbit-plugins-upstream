## Description:

Analyzes changesets with risk scoring, categorization by type and impact, and release note preparation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to analyze diffs, migrations, configuration changes, schema updates, and document revisions before review, release-note preparation, or planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may activate for broad requests involving changes, impact, summaries, or release notes.

Mitigation: Use it when diff, migration, release-note, or impact analysis is intended; use the alternate workflows named in the skill for quick context catchup or full pull-request review.

Risk: Generated risk assessments and release summaries can be incomplete if the comparison baseline or change scope is unclear.

Mitigation: Confirm the baseline, changed files, and comparison boundary before relying on the analysis for review or release decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-diff-analysis)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)
- [sem entity-level diff tool](https://github.com/Ataraxy-Labs/sem)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces categorized change summaries, risk assessments, review focus areas, dependencies, and release-note or changelog-ready summaries.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
