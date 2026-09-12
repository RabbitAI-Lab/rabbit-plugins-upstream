## Description:

Audit a ClawHub publisher portfolio using live registry evidence to decide which skills to improve, merge, stop, or build next based on downloads, installs, search competition, and version health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub publishers and skill developers use this skill to audit a portfolio of published skills and decide what to improve, merge, pause, or build next from registry metrics, search competition, and repository evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portfolio recommendations can be misleading when based on one snapshot, incomparable search queries, active-install contamination, or an observation window shorter than seven days.

Mitigation: Use the skill's decision-readiness gates; if any gate is missing or failed, limit the conclusion to continued observation or data-quality repair.

Risk: The skill depends on public ClawHub registry evidence and repository evidence, so unavailable or stale data can weaken the audit.

Mitigation: Record the evidence source, collection method, query set, and observation window, and clearly separate facts from conclusions that still need more time.

Risk: Suggested portfolio actions are strategy guidance and may be inappropriate if applied automatically.

Mitigation: Review the audit before changing positioning, merging skills, stopping maintenance, creating new skills, or launching plugins.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bonniegeng-max/skills/skill-portfolio-growth-audit)
- [Publisher profile](https://clawhub.ai/user/bonniegeng-max)
- [Homepage](https://github.com/bonniegeng-max/openclaw-publisher)
- [Growth evidence rules](references/evidence_rules.md)
- [Competition review](references/competition_review.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown portfolio audit report with decision-readiness gates, evidence boundaries, comparison tables, and one prioritized next action.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public ClawHub registry evidence and repository evidence; conclusions are downgraded when the required decision-readiness gates are not met.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
