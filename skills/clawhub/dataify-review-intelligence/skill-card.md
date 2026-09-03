## Description:

Analyze reviews or public customer feedback across multiple sources and produce themes, sentiment signals, and product actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Product, support, marketing, and research teams use this skill to turn public customer reviews into traceable themes, sentiment signals, source-bounded evidence, and prioritized product actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends public review queries or supplied public review URLs to Dataify for collection.

Mitigation: Install and run it only when that data flow is acceptable for the subject being analyzed.

Risk: Generated raw evidence files may contain sensitive business context embedded in user queries or collected public review data.

Mitigation: Review generated raw evidence files before sharing reports and avoid including sensitive business context in query text.

Risk: Collection scope can affect API credit usage.

Mitigation: Use dry-run or max-actions controls to inspect and bound planned actions before larger runs.

## Reference(s):

- [Dataify Review Intelligence on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-review-intelligence)
- [dataify-server publisher profile](https://clawhub.ai/user/dataify-server)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with retained evidence identifiers and local raw evidence files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include sample-size metrics, positive and negative signal counts, top records, collection gaps, limitations, and resumable state.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
