## Description:

Generates evidence-based portfolio audits, candidate scorecards, privacy classifications, consolidation plans, and a persistent execution queue for Skill portfolio management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Skill maintainers use this skill to inventory Skill portfolios, identify duplication or version drift, classify sharing suitability, and turn recommendations into a dependency-linked task queue.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Audits may inspect Skill files, workflow materials, work logs, long-term memory, and historical conversations.

Mitigation: Set a clear scan range before use and review the generated task ledger before acting on recommendations.

Risk: Portfolio recommendations may involve private, company, or publish-sensitive data.

Mitigation: Use the skill's sharing classifications and block publication when credentials, internal information, customer data, or other sensitive material is found.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/skill-portfolio-audit)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Configuration, Guidance]

**Output Format:** [Markdown audit report with scorecards, classifications, roadmap, risks, evidence boundaries, and task queue guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only against audited Skills; writes only a separate persistent task ledger when recommendations are confirmed.]

## Skill Version(s):

1.1.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
