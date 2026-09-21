## Description:

The Literature Review Paper Screener helps a local agent search medical-science literature, collect per-paper evidence, submit one evidence record per paid LoomLoom cloud task for screening, audit the returned results, and render Excel Paper Sheet and Reading List outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ez-hq](https://clawhub.ai/user/ez-hq)

### License/Terms of Use:

MIT

## Use Case:

External users and agent operators use this skill to conduct medical-science literature review screening, from search and evidence collection through cloud-assisted screening and local Excel delivery. It is not intended for general citation management, non-literature-review work, or disciplines outside its configured medical-science focus.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Per-paper evidence records are sent to a selected third-party cloud platform for screening.

Mitigation: Send only the minimized evidence fields needed for screening, remove personal details and credentials, and obtain explicit consent before data transfer.

Risk: Cloud runs are paid per paper and can create unexpected cost if submitted without a locked task count.

Mitigation: Require fresh confirmation of platform, fee, paper count, and estimated total cost before every paid run.

Risk: Screening quality depends on the evidence available in each record, especially for records with limited abstracts or metadata only.

Mitigation: Assign evidence availability levels, preserve missing-evidence notes, block mismatched metadata before handoff, and flag evidence-limited papers in the delivery summary.

## Reference(s):

- [Architecture reference](references/architecture.md)
- [Evidence package schema](references/evidence-package-schema.md)
- [Metadata validation gate](references/metadata-validation-gate.md)
- [Release homepage](https://github.com/ez-hq/literature-review-paper-screener/releases)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown workflow guidance with shell commands, JSON evidence records, audit JSON, and Excel workbook outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and loomloom; cloud screening runs one paper per task and local scripts validate results before rendering PaperSheet.xlsx and ReadingList.xlsx.]

## Skill Version(s):

1.4.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
