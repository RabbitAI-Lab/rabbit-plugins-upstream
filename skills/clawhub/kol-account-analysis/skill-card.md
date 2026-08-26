## Description:

Provides public-data-based KOL account analysis for content stability, audience reception, product-entry fit, collaboration-form recommendations, and risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qomob](https://clawhub.ai/user/qomob)

### License/Terms of Use:

MIT

## Use Case:

Marketing, brand, and creator-operations teams use this skill to analyze a single public KOL or creator account before collaboration. It structures evidence from posts and visible comments into reusable account understanding, collaboration recommendations, risk checks, and evidence-boundary statements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may collect public posts and visible comments, which can create privacy, platform-policy, or retention risks if used on private, login-gated, or over-collected data.

Mitigation: Use it only for a clearly identified public creator/account and platform; confirm collection is allowed, avoid private or login-gated data, de-identify comment exports, and retain them only as long as needed.

Risk: Optional third-party collection tools or browser automation can introduce platform terms, account-safety, or dependency risks.

Mitigation: Vet optional third-party tools before installation, prefer official or authorized data sources where available, and follow the documented public-only, rate-limited collection posture.

Risk: Public post and comment evidence can be incomplete or biased, leading to overconfident collaboration or lifecycle conclusions.

Mitigation: State evidence gaps, use the documented evidence-quality tiers, downgrade unsupported conclusions to directional judgments, and do not infer campaign results or data authenticity from public signals alone.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qomob/skills/kol-account-analysis)
- [Task Definition](references/task-definition.md)
- [Platform Context](references/platform-context.md)
- [Data Sources](references/data-sources.md)
- [Data Collection](references/data-collection.md)
- [Collection Playbook](references/collection-playbook.md)
- [Works Analysis](references/works-analysis.md)
- [Comments Analysis](references/comments-analysis.md)
- [Collaboration Judgment](references/collaboration-judgment.md)
- [Honest Boundaries](references/honest-boundaries.md)
- [Report Template](templates/report-template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown report with structured tables, evidence notes, optional CSV collection outputs, and inline shell commands for public-page collection setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public creator/account and platform must be specified; conclusions are bounded by available public or user-provided evidence.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
