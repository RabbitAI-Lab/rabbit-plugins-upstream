## Description:

Identifies product quality issue signals, supporting review evidence, and priorities from Amazon low-star reviews and product fields; it is not a substitute for inspection, certification, recall decisions, or supplier execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, product teams, and developers use this skill to review Amazon low-star feedback for quality improvement leads, evidence, and prioritization. It first checks product data and quotes paid ARI operations, then runs only after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires storing an ari_live API key locally and using the ARI service.

Mitigation: Install only when the publisher and ARI service are trusted, and use the documented setup and check commands before paid operations.

Risk: Paid collection or analysis can spend ARI credits.

Mitigation: Run quote/profile first and proceed only after an explicit user confirmation tied to the returned requestId.

Risk: Workflow or focus overrides could broaden behavior beyond the fixed quality-review entry point.

Mitigation: Use the documented product/quality workflow and avoid --workflow or --focus overrides unless broader product-operations behavior is intentional.

Risk: Quality findings may be mistaken for certification, recall, supplier, inventory, advertising, or financial conclusions.

Mitigation: Limit conclusions to the collected review and product-field evidence, and state gaps instead of filling missing business data.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/funewa/skills/quality-issue)
- [Amazon product quality issue API reference](artifact/references/reference.md)
- [Amazon product quality issue operations workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and quality-review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite the data range, main findings, review evidence, conclusions, and evidence gaps without inventing unavailable business data.]

## Skill Version(s):

1.4.13 (source: server release evidence, _meta.json, scripts/ari.py, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
