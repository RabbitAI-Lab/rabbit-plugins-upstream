## Description:

Analyzes brand visibility, sentiment, citations, and competitor mentions across six AI search platforms and produces an interactive report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[redfox-data](https://clawhub.ai/user/redfox-data)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketers, product managers, and content teams use this skill to compare a brand's visibility and reputation across AI search platforms, identify cited sources, and benchmark competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Brand names, categories, and custom questions are sent to RedFox-backed AI search services; raw answers are saved locally.

Mitigation: Use only approved, non-confidential questions and protect or delete local output files according to your organization's data policy.

Risk: A small question sample and changing AI answers can give an incomplete view of brand visibility.

Mitigation: Use representative questions, review individual answers, and repeat measurements before making decisions.

## Reference(s):

- [GEO metrics definitions](references/geo-metrics.md)
- [ClawHub skill listing](https://clawhub.ai/redfox-data/skills/geo-analyzer)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Markdown findings summary, JSON analysis files, and interactive HTML report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores raw AI answers locally; identifies incomplete search results.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
