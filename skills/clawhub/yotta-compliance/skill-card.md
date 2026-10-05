## Description:

Reviews text and Markdown against deterministic PIPL and data-export rules, producing evidence-linked findings and Markdown or JSON reports for human review and CI gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and compliance reviewers use this skill to identify potential gaps in privacy notices and data-export clauses, trace findings to source text and rules, and route reports for professional review. It does not provide legal advice or certify compliance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automated findings may be mistaken for a legal opinion or proof of compliance.

Mitigation: Treat reports as review aids and have a qualified professional verify consequential conclusions.

Risk: A broad installation may copy the skill into multiple agent environments.

Mitigation: Install a pinned version or reviewed archive; target a specific agent directory unless a global installation is intended.

## Reference(s):

- [Coverage and rule inventory](references/coverage.md)
- [Report format](references/report-format.md)
- [Rule authoring](references/rule-authoring.md)
- [Project homepage](https://github.com/YottaMeta/yotta-compliance)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-compliance)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON reports with source-text evidence, rule citations, coverage labels, and review items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional severity-based CI exit gate; writes to stdout unless an output file is requested]

## Skill Version(s):

0.1.1 (source: frontmatter, package.json, changelog, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
