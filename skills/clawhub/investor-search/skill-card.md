## Description:

Builds sourced investor lists for a country or market, separates investors from advisers, preserves evidence, and delivers one Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chainleo](https://clawhub.ai/user/chainleo)

### License/Terms of Use:

MIT-0

## Use Case:

Investor researchers, fundraisers, deal teams, and operators use this skill to build sourced prospect lists for family offices, venture capital firms, private equity firms, angels, and related investment groups in a target market. It is useful when the reader needs evidence links, duplicate handling, and a clear statement of what remains partial or unresolved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Investor research files may persist in a shared agent workspace and could be resumed or read by the wrong audience.

Mitigation: Use a separate agent workspace per user or team, or require a stable platform channel or team identifier before resuming stored data.

Risk: The final workbook may be posted into a group channel where more people can access it than intended.

Mitigation: Require explicit confirmation before posting the final workbook into a group channel.

Risk: The skill depends on web research, Python execution, and persistent local files.

Mitigation: Enable it only in environments where those capabilities and local research files are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chainleo/skills/investor-search)
- [README](README.md)
- [Environment](references/environment.md)
- [Lists](references/lists.md)
- [Why each rule exists](references/why.md)

## Skill Output:

**Output Type(s):** [Files, Text, Shell commands, Guidance]

**Output Format:** [Excel workbook with concise text status and delivery notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workbook includes investor rows, source links, pending items, round history, and ledger data; the skill also emits progress and resume guidance.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
