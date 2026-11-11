## Description:

Reviews finished AI video ads against platform and advertising rules, then produces a pass, fix, or block report with cited rules, suggested edits, and disclosure guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers and marketing teams use this skill to review a finished AI product ad before publishing, identify claims and visuals that may need changes, and prepare platform disclosure labels. It is not legal advice; the skill recommends legal review for regulated categories.

### Deployment Geography for Use:

Global; documented checks cover the US, New York, EU, and UK.

## Known Risks and Mitigations:

Risk: The workflow sends ad footage or video URLs to Varg for analysis, and the supplied evidence does not clarify how that material is handled.

Mitigation: Review Varg's handling terms and avoid submitting confidential or identifiable material unless the disclosure is acceptable.

Risk: Setup instructions include a broader plugin installation option than the skill's focused ad-review purpose.

Mitigation: Review the install scope and select only the compliance skill when that is all the task requires.

Risk: The documented npx installation command does not pin a reviewed version.

Mitigation: Review the package contents before installation and use a version-pinned source when one is available.

Risk: Compliance rules can change, and the report is not legal advice.

Mitigation: Recheck source rules before relying on the report and seek legal review for regulated categories or consequential decisions.

## Reference(s):

- [AI ad compliance rules](artifact/references/rules.json)
- [Example compliance report](artifact/references/example-report.md)
- [Varg help and account setup](https://varg.ai/how-to)
- [Varg MCP connection](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown compliance report with timestamped findings, rule citations, suggested edits, platform labels, and an overall verdict]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings use pass, fix, block, or warn levels where applicable; the skill states that its output is not legal advice.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
