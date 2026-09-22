## Description:

Sourced investor list for any country. Find family offices, VCs, PE firms and angels, with a source for every field and an honest word on how complete the list is.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainleo](https://clawhub.ai/user/chainleo)

### License/Terms of Use:

MIT No Attribution

## Use Case:

Developers, researchers, and business teams use this skill to build sourced investor prospect lists for a country, region, or market, including family offices, venture capital firms, private equity firms, angels, and related investment groups. It is suited for investor research, deal sourcing, fundraising lists, CRM enrichment, and filling gaps in an existing investor database.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared-channel storage and automatic delivery rules can expose one team's investor research to another.

Mitigation: Use separate agent workspaces per team or immutable channel and team identifiers with ownership checks before reading existing files.

Risk: Automatically posting generated XLSX files into a channel can disclose investor research to unintended recipients.

Mitigation: Require confirmation before posting XLSX files in shared channels and restrict delivery to the intended workspace or recipient.

## Reference(s):

- [README](README.md)
- [Environment](references/environment.md)
- [Lists](references/lists.md)
- [Why each rule exists](references/why.md)
- [ClawHub skill page](https://clawhub.ai/chainleo/skills/investor-search)

## Skill Output:

**Output Type(s):** [Files, Text, Markdown, Shell commands, Guidance]

**Output Format:** [XLSX file with sourced investor data, plus status text or Markdown and shell commands used to manage the local store]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one market investor workbook and maintains local CSV, ledger, pending, rejected, and round-history files for continuation.]

## Skill Version(s):

1.2.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
