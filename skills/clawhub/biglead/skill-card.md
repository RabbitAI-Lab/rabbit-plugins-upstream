## Description:

BigLead helps agents find and manage B2B sales prospects by searching public company sources, extracting public business contact details, validating leads across sources, and maintaining a local lead database.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kobenfang](https://clawhub.ai/user/kobenfang)

### License/Terms of Use:

MIT-0

## Use Case:

Sales, business development, and market research users can use this skill to build targeted B2B lead lists from public company information, track follow-up status, and export prospect records. The skill is most useful when the user provides an industry, product category, or region to guide search and deduplication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local lead records and CSV exports may contain business contact details.

Mitigation: Limit access to memory/lead-data/ and exported CSV files, and delete those records when they are no longer needed.

Risk: Public prospect information may be stale, incomplete, or unsuitable for outreach without review.

Mitigation: Verify important leads against official company sources before using the data for sales or research decisions.

Risk: Broad or repeated searches can create duplicate records or unnecessary collection of prospect data.

Mitigation: Use the existing and duplicate-check workflows before adding new leads, and keep search batches limited.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kobenfang/skills/biglead)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown lead reports with inline shell commands and JSON/CSV-backed lead records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores local lead data under memory/lead-data/ and can export CSV files.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
