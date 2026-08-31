## Description:

Reviews AI-generated test cases against quality dimensions such as completeness, correctness, executability, risk coverage, consistency, traceability, and redundancy, then produces a structured critique with scores and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, developers, and test leads use this skill after AI-generated test cases are produced to identify missing coverage, unclear steps, weak expected results, risk gaps, and low-value duplication before the test set is accepted.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Chinese trigger phrases may activate the skill during a general output check rather than a targeted test-case critique.

Mitigation: Confirm that the current task is reviewing AI-generated test cases before applying the full scoring rubric.

Risk: Chinese-model-specific heuristics may not apply equally to every model, language, product, or compliance context.

Mitigation: Treat these heuristics as contextual review prompts and validate findings against the product requirements and applicable domain rules.

## Reference(s):

- [Report Templates](references/report-templates.md)
- [Review Dimensions](references/review-dimensions.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown review report with scoring tables, issue lists, coverage gaps, quality score, and improvement suggestions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a full eight-dimension review when scenario tree and risk inputs are available, and falls back to a simplified review when upstream inputs are missing.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
