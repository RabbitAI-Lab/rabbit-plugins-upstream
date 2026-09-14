## Description:

Checks trade-document text for mechanical inconsistencies across invoice, packing list, bill of lading, and related documents, including key identifiers, amounts, quantities, weights, ports, vessel names, marks, and unresolved placeholders, with source evidence for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External trade-operations users can use this skill before document submission to compare supplied trade documents and identify mechanical inconsistencies that may need correction. It supports local pre-checking only and does not decide whether a bank, carrier, or legal reviewer will accept the documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The checker performs mechanical consistency checks only, so a clean result can still miss banking, legal, or letter-of-credit acceptance issues outside its stated scope.

Mitigation: Use the findings as a pre-check and have qualified trade-document reviewers confirm compliance before submission.

Risk: Using the optional web checker with confidential trade documents may have separate privacy implications from local execution.

Mitigation: Run the local script for confidential materials and review the external service terms before uploading documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trade-doc-consistency-free)
- [Free web checker](https://www.tokendidi.cn/check)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON check results with cited source evidence and suggested corrections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can run locally with Node.js; exits with a distinct insufficient-input status instead of producing a false consistency conclusion.]

## Skill Version(s):

1.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
