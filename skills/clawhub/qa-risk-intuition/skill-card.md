## Description:

Identifies QA areas that may look simple but carry high testing risk, helping teams prioritize limited testing effort across change, business, data, integration, and technical risk signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers and developers use this skill to assess feature or release risk, rank high-risk modules, and choose focused test coverage when time or staffing is limited.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read project files when asked to assess testing risk.

Mitigation: Limit inputs to relevant project materials and avoid unnecessary sensitive data in the files provided for review.

Risk: The artifact contains inconsistent risk formulas and broad trigger wording, which can make scores or coverage targets appear more precise than the evidence supports.

Mitigation: Review scoring, coverage recommendations, and trigger matches against project context before using them to allocate testing effort.

## Reference(s):

- [Risk Signals Reference](references/risk-signals.md)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-risk-intuition)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown risk assessment report and test-case table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes risk IDs, probability and impact levels, a risk matrix, high-risk areas, and mitigation suggestions.]

## Skill Version(s):

1.7.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
