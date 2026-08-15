## Description:

Helps QA practitioners identify testing areas that may look simple but carry high risk, prioritize limited testing resources, and attach probability, impact, and mitigation guidance to each risk point.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and release reviewers use this skill to assess feature or change risk, rank high-risk testing areas, and decide where to focus test depth and resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger wording may cause the skill to produce broader risk analysis than a narrow test-case request requires.

Mitigation: Scope the request to the feature, change set, or module under review, and review the resulting priorities before using them to allocate test effort.

Risk: Risk rankings can be misleading when requirements, scenario trees, or historical defect data are incomplete.

Mitigation: Provide current requirements and known defect history where available, then validate high-risk classifications with the QA or release owner.

## Reference(s):

- [risk-signals.md](references/risk-signals.md)
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-risk-intuition)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown risk assessment report with tables, risk matrix, prioritized areas, and mitigation suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk points are expected to include traceable IDs, requirement links, probability and impact ratings, and suggested testing depth.]

## Skill Version(s):

1.6.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
