## Description:

Chat Order OCR organizes pasted LINE/Facebook chat text or local OCR results into reviewable JSON or CSV order lists grouped and sorted by customer.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qpooqp777](https://clawhub.ai/user/qpooqp777)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, community commerce operators, and their agents use this skill to convert social chat order messages or OCR text into structured order drafts. It supports local parsing, optional local screenshot OCR through Tesseract, catalog matching, grouping, sorting, and human review before fulfillment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process customer names, order details, and screenshots, and can write parsed JSON or CSV files where directed.

Mitigation: Run it in an appropriate local workspace, limit access to generated files, and avoid storing unnecessary customer screenshots or order exports.

Risk: OCR text, unmatched catalog aliases, unclear names, prices, weights, or duplicate cross-image content can produce rows that are not ready for fulfillment.

Mitigation: Review rows marked with confidence check and confirm names, items, specifications, quantities, and duplicates before using the output for business decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/qpooqp777/skills/chat-order-ocr)
- [CLI Examples](references/cli_examples.md)
- [Catalog Example](references/catalog.example.json)
- [Complex Chat Fixture](references/complex_chat_fixture.txt)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands; generated order outputs are JSON or UTF-8 BOM CSV.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Rows include source and confidence fields; OCR and unmatched catalog entries are marked for checking.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
