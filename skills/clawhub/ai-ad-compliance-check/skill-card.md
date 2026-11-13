## Description:

Reviews AI video ads against advertising and platform rules, then produces a pass, fix, or block report with cited rules, suggested revisions, and disclosure labels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Ad sellers and marketers use this skill to review a finished AI product ad before publishing, checking claims, product depictions, synthetic people, and required disclosures across relevant platforms and markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review workflow sends submitted videos or URLs to Varg, and the security evidence reports no explicit notice or authorization step.

Mitigation: Tell the user what will be shared and get their authorization before submitting media; avoid sending material they cannot share.

Risk: The security evidence flags an unpinned installation source, which can make the installed content change over time.

Mitigation: Verify the publisher and release, and pin or otherwise record the reviewed version before installation.

Risk: Some compliance rules may have verification labels that do not match their cited sources, and the scan was incomplete.

Mitigation: Check cited platform or regulator sources directly before relying on a rule or report, especially for high-impact or regulated ads.

Risk: A compliance report may be mistaken for definitive legal advice.

Mitigation: Use the report as a review aid and have qualified counsel assess ads in regulated categories.

## Reference(s):

- [Compliance rules](references/rules.json)
- [Example compliance report](references/example-report.md)
- [Varg how-to guide](https://varg.ai/how-to)
- [Varg MCP connection](https://mcp.varg.ai/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown compliance report with timed findings, rule citations, suggested fixes, verdict, and platform disclosure checklist]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Based on the supplied video, caption, platform, market, product category, and seller evidence.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
