## Description:

Tender Generator Pro collects project and bidder details through conversation or JSON input, fills tender document templates, validates missing fields, and packages generated bid documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mama1234421](https://clawhub.ai/user/mama1234421)

### License/Terms of Use:

MIT-0

## Use Case:

External business users and agent operators use this skill to collect tender information, generate bid document packages, extract fields from source documents, and check generated files before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive tender, company, pricing, and bank-account data may be read from inputs and written into generated local files.

Mitigation: Run the skill in a trusted local workspace, restrict access to input and output folders, and remove generated files when they are no longer needed.

Risk: Generated bid documents may contain incomplete fields, incorrect extracted values, or placeholders that were not filled.

Mitigation: Use the skill's validation and compliance checks, then manually review every generated bid document before submission.

Risk: Tender source documents or templates may contain outdated, untrusted, or legally sensitive requirements.

Mitigation: Use trusted templates and source documents, and verify technical parameters, signatures, stamps, and required attachments against the official tender materials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mama1234421/skills/tender-generator)
- [README.md](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated DOCX files, JSON information files, and ZIP packages on disk]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes user-provided tender, company, pricing, and bank-account fields locally and writes generated documents to the selected output directory.]

## Skill Version(s):

3.0.0 (source: server release metadata, artifact _meta.json, and script VERSION)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
