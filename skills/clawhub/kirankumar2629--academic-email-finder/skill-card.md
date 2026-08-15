## Description:

Finds public academic email addresses in batches from a user-provided spreadsheet of names and institutions, then writes the results to an Excel file.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kirankumar2629](https://clawhub.ai/user/kirankumar2629)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enrich a spreadsheet of academic contacts by searching public sources for likely institutional email addresses. It is suited to one-shot batch lookup tasks where the user can verify the source spreadsheet, row scope, and output column before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill collects academic contact email addresses, which may be privacy-sensitive even when found in public sources.

Mitigation: Install and run it only for a legitimate contact-collection purpose, and confirm the spreadsheet source and row scope before searching.

Risk: Writing results directly to the spreadsheet can overwrite or misplace data if the wrong file or output column is selected.

Mitigation: Confirm the target file and output column before execution, and save results to a new file rather than overwriting the original.

Risk: Same-name academics or sparse public profiles can produce incorrect email matches.

Mitigation: Review a sample of matches after completion and manually verify ambiguous records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kirankumar2629/skills/academic-email-finder)
- [Publisher profile](https://clawhub.ai/user/kirankumar2629)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python snippets and file path output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes discovered email addresses into an Excel file and reports lookup progress.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
