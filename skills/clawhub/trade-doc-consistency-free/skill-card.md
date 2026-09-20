## Description:

This skill checks trade documents for cross-document mismatches in identifiers, amounts, quantities, weights, ports, vessel names, shipping marks, and unresolved template placeholders, with source-text evidence for each finding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Trade operators, exporters, and documentation teams use this skill before document submission to compare invoices, packing lists, bills of lading, and related trade documents for mechanical consistency issues and placeholder text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat mechanical consistency output as a guarantee of bank acceptance or trade compliance.

Mitigation: Treat results as a consistency aid only and have qualified staff review documents against bank, letter-of-credit, and compliance requirements.

Risk: The inspected release has documentation drift around anonymous statistics behavior.

Mitigation: Review the installed release and its security evidence before use, especially when processing sensitive trade documents.

Risk: The free version omits several checks such as line arithmetic, date order, and credit limit tolerance.

Mitigation: Use the output scope and omitted-check list to decide whether additional manual review or another tool is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/trade-doc-consistency-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [Skill documentation](artifact/SKILL.md)
- [Sample input](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and optional JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can emit human-readable findings or structured JSON; exit codes distinguish missing input, insufficient materials, parse failures, and unexpected errors.]

## Skill Version(s):

1.0.48 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
