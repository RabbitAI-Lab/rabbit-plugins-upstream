## Description:

This skill helps an agent analyze Amazon review data through ARI to identify buyer personas, usage scenarios, purchase motivations, pain points, trends, competitor differences, and reportable product guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and marketers use this skill to turn collected Amazon review samples into buyer persona insights, VOC reports, keyword ideas, trend summaries, competitor comparisons, and exportable review or report artifacts. It is intended for ARI account holders who can authorize the local CLI and review paid actions before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects to an ARI account and stores an ARI API key locally.

Mitigation: Use the browser authorization flow or environment variable support; do not paste the API key into chat, reports, or examples, and revoke or recreate the key if it may have been exposed.

Risk: Paid ARI operations can spend credits, and some flows may execute under account auto-confirm rules.

Mitigation: Use quote-only requests or turn auto-confirm off when every paid action should be reviewed, and only run confirmed paid commands after the user has accepted the quoted cost.

Risk: Recurring review collection and monitoring can create ongoing costs.

Mitigation: State the schedule and cost returned by ARI before enabling monitoring, and require explicit user confirmation for schedule changes.

Risk: Exported review data and reports may contain business-sensitive customer feedback.

Mitigation: Export only when requested, keep files in the intended local directory, and handle exported CSV, Markdown, or HTML according to the user's data handling requirements.

Risk: Analysis is limited to ARI-collected review samples and may not cover every Amazon review or product variant.

Mitigation: Report the sample range and data limitations, avoid unsupported trend claims, and mark small samples or incomplete windows as directional.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/user-persona)
- [Publisher Profile](https://clawhub.ai/user/funewa)
- [ARI CLI and API Reference](artifact/references/reference.md)
- [ARI Usage Guide](artifact/使用说明.md)
- [ARI Account and Authorization](https://ari.funewa.com/zh/account?ui=d47626f#api-keys)
- [ARI Billing](https://ari.funewa.com/zh/billing)
- [ARI Reports](https://ari.funewa.com/zh/reports)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown and plain text responses with inline shell commands; exports may produce CSV, Markdown, or HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include ARI report links, sample ranges, credit usage notes, and local export paths when export commands are used.]

## Skill Version(s):

1.4.11 (source: frontmatter, _meta.json, release evidence, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
