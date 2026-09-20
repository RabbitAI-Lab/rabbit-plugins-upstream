## Description:

Generates an evidence-based weekly comparison report for a primary Amazon ASIN and authorized competitor products after quote review and explicit user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and agents use this skill to prepare weekly evidence reports comparing a primary ASIN with authorized competitor ASINs. It checks product data and costs first, then runs the paid ARI report only after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run broader paid ARI product-operation workflows than the fixed weekly competitor report promises.

Mitigation: Run only the fixed weekly/competitor flow and avoid workflow or focus overrides.

Risk: The skill uses an ARI API key and paid credits.

Mitigation: Use it only if the ARI service is trusted with the API key and billing credits, and confirm charges only after reviewing the quote and ASIN scope.

## Reference(s):

- [Amazon Competitor Weekly Operation Workflow](references/operation-workflow.md)
- [Amazon Competitor Weekly API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with concise text summaries and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit confirmation before paid report execution.]

## Skill Version(s):

1.4.13 (source: server release evidence and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
