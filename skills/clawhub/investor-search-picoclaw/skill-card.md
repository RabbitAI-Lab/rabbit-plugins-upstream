## Description:

Investor Search for PicoClaw guides an agent through sourced investor research for a country or market, separating real investors from advisers and delivering a sourced Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainleo](https://clawhub.ai/user/chainleo)

### License/Terms of Use:

MIT-0

## Use Case:

External users, fundraising teams, deal-sourcing teams, and analysts use this skill to build sourced lists of family offices, VCs, PE firms, angels, and investment groups for a named country, region, or market. It is intended for investor research, prospect list building, CRM enrichment, LP research, and follow-up list completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Investor research runs can create workspace files and a delivered Excel workbook that may be visible to other users of a shared agent or chat channel.

Mitigation: Use a private chat or per-team PicoClaw workspace for confidential prospecting, and warn users before resuming or delivering files in shared contexts.

Risk: The workflow depends on web search and page fetches, so incomplete or failed fetches can limit what the report can prove.

Mitigation: Keep source links for every field, leave unsupported fields empty, report partial results when persistence or fetch requirements are not met, and avoid claiming completeness without the documented stop conditions.

Risk: Local memory files are part of the workflow and can be lost or unavailable in environments without durable workspace storage.

Mitigation: Use the generated Excel workbook as the handoff artifact and import it on a later run when the workspace folder cannot be kept.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chainleo/skills/investor-search-picoclaw)
- [README](README.md)
- [Environment reference](references/environment.md)
- [Lists reference](references/lists.md)
- [Rule rationale](references/why.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, files]

**Output Format:** [Markdown guidance with shell command examples and an Excel workbook deliverable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one <market>-investors.xlsx file with source links, plus local workspace files used to resume and deduplicate later runs.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
