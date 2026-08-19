## Description:

Supports biopharma patent retrieval, patent-family consolidation, legal-status checks, applicant ownership review, and portfolio landscape research for companies, targets, drugs, or technology themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, and biopharma researchers use this skill to build traceable patent portfolios and landscape reports for companies, targets, drugs, or technology themes. It emphasizes applicant-scope confirmation, pagination reconciliation, de-duplication, legal-status checks, and workbook-safe delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A legacy reference contains conflicting Excel instructions that could unexpectedly change workbook structure.

Mitigation: Use strict-template mode for user-provided templates, keep a backup before use, and explicitly instruct the agent not to load or apply legacy Step 11 formatting.

## Reference(s):

- [Legacy company patent workflow](references/legacy-company-patent-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured lists, JSON-like records, and workbook output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation or editing of Excel workbooks; strict-template mode preserves user-provided columns and sheets.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
