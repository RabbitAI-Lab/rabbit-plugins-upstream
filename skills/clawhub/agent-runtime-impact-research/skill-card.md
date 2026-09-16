## Description:

Researches major agent harness, runtime, coding-agent, skills, subagent, and plugin releases, producing verified fact tables, runtime flow explanations, layered impact analysis, and source registers with judgment separated from evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, platform engineers, and agent ecosystem analysts use this skill to evaluate what a major agent runtime or harness release changes across architecture, extensibility, governance, evaluation, and enterprise adoption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on current public sources, so release facts can become stale or remain unverified when primary sources are missing.

Mitigation: Use current searches, prefer official sources, mark unsupported fields as unknown, and separate facts from judgments.

Risk: Research outputs may introduce incorrect or misleading conclusions if analytical judgment is read as confirmed fact.

Mitigation: Keep facts, observations, judgments, hypotheses, counterarguments, and failure modes visibly separated.

Risk: The skill biases responses toward concise Chinese unless the agent or user overrides that preference.

Mitigation: Override the response language or style when the task requires another audience, locale, or documentation standard.

## Reference(s):

- [Fact Table Schema](references/fact-table-schema.md)
- [Impact Layers Analysis](references/impact-layers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research report with fact tables, layered analysis, platform comparisons, counterarguments, and a source register]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates facts, observations, judgments, uncertainty, and source tiers; defaults to concise Chinese unless overridden.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
