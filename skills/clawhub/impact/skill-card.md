## Description:

Analyze code-change blast radius with the impact CLI. Use when reviewing diffs, assessing merge or deployment risk, finding affected tests, diffing public contracts, visualizing callers, detecting orphan code, or writing PR/MR impact summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[albert-lv](https://clawhub.ai/user/albert-lv)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code changes, find affected tests and callers, compare public contracts, and prepare impact summaries for pull requests or merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The executable is built from upstream source that is not included in this package for inspection.

Mitigation: Review and pin the upstream source before building.

Risk: Repository caches and analysis reports may contain sensitive project information.

Mitigation: Analyze only intended repositories, keep cached analysis appropriately private, and review results before sharing reports.

Risk: Impact classifications and orphan candidates may be incomplete or misleading when treated as definitive.

Mitigation: Check results, run relevant tests, and use human review before deleting code or acting on a report.

## Reference(s):

- [Code Impact Analyzer project homepage](https://github.com/nano-harness/impact-analyzer)
- [ClawHub release page](https://clawhub.ai/albert-lv/skills/impact)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Guidance]

**Output Format:** [Concise text or Markdown summaries; JSON when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports depend on the available repository, Git history, and analysis results; the skill does not edit source code.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
