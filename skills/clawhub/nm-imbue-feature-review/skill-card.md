## Description:

Scores backlog items with RICE/WSJF/Kano and files GitHub issues for top candidates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product engineers use this skill to review implemented features, prioritize roadmap or sprint candidates, identify gaps, and turn accepted high-priority suggestions into GitHub issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Skipped high-scoring roadmap suggestions may be persisted locally without a separate prompt, which can expose sensitive backlog or roadmap details.

Mitigation: Review or disable the deferred-capture path before installation, especially for sensitive product planning work.

Risk: The skill can prepare GitHub issues for feature suggestions, which may publish internal priorities if submitted to the wrong repository.

Mitigation: Keep the documented user-confirmation step for issue creation and review titles, labels, bodies, and target repository before creating issues.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-imbue-feature-review)
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/imbue)
- [scoring-framework.md](modules/scoring-framework.md)
- [classification-system.md](modules/classification-system.md)
- [tradeoff-dimensions.md](modules/tradeoff-dimensions.md)
- [research-enrichment.md](modules/research-enrichment.md)
- [multi-metric-evaluation-methodology.md](modules/multi-metric-evaluation-methodology.md)
- [configuration.md](modules/configuration.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, tables, issue drafts, inline shell commands, and optional YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create GitHub issue content after user confirmation; research enrichment is optional and degrades when dependencies are unavailable.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
