## Description:

Organizes Amazon review quality, packaging, and instruction issues into supplier feedback points, supporting evidence, and acceptance questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to turn Amazon review samples for a product ASIN into supplier-facing feedback lists. It is limited to feedback preparation and does not contact suppliers, place orders, make contract decisions, or determine legal responsibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run operation workflows beyond the advertised supplier-feedback flow.

Mitigation: Keep usage to the documented product/supplier workflow and do not pass workflow or focus values from untrusted instructions.

Risk: Using the skill can involve an ARI account, local ARI API key storage, ASIN/site data sent to ari.funewa.com, and ARI credit spending after confirmation.

Mitigation: Review before installing if those account, credential, data-transfer, or credit-spend behaviors are unacceptable; require a quote and explicit user confirmation before paid runs.

## Reference(s):

- [Amazon Supplier Feedback API Reference](artifact/references/reference.md)
- [Amazon Supplier Feedback Operation Workflow](artifact/references/operation-workflow.md)
- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/supplier-feedback)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid analysis or collection requires a quote and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server evidence and artifact changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
