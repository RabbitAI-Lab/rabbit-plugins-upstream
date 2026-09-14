## Description:

Checks Amazon listing structure, terminology, repeated wording, and review-backed comprehension barriers, then suggests readability improvements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, operators, and listing reviewers use this skill to diagnose listing readability issues from product fields and collected review samples. It is scoped to readability guidance, not advertising, legal certification, translation certification, or automatic listing publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires trust in the ARI service and uses an API key with account, credit, and paid analysis authority.

Mitigation: Install only when the ARI service is trusted, keep the API key in the supported user configuration or environment variable, and review quoted credits before confirming a paid run.

Risk: Security evidence reports that the CLI can run paid product-operation workflows beyond the fixed listing-readability scope described to users.

Mitigation: Before confirming a run, verify the quoted request is specifically for listing/readability and avoid workflow or focus overrides unless a different ARI operation is intentional.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/listing-readability)
- [Amazon Listing Readability API Reference](artifact/references/reference.md)
- [Amazon Listing Readability Operation Workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-readable diagnostic guidance with JSON CLI status and quote responses when commands are shown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis requires a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release evidence, _meta.json, scripts/ari.py, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
