## Description:

Analyzes a specific tender using historical procurement data to estimate bidding prospects, assess competitors and buyer patterns, and recommend whether and how to bid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement and bid teams assess a specific tender's buyer history, likely competitors, pricing benchmarks, qualification risks, and whether participation is worthwhile.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Procurement queries and device-derived trial-registration data are shared with the vendor, and API credentials may be stored locally.

Mitigation: Use only with a trusted vendor; obtain consent before trial registration and protect locally stored API credentials.

Risk: Shareable HTML reports may include signed links that open records without normal login.

Mitigation: Treat reports and their links as sensitive; share them only with intended recipients.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/bid-win-rate-analyzer)
- [Analysis workflow](artifact/references/workflow.md)
- [Report template](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Markdown, HTML report, Guidance]

**Output Format:** [Tender decision report in Markdown; shareable HTML file in full mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a recommendation, confidence level, supporting records, pricing guidance, and data gaps; report links may grant access without login.]

## Skill Version(s):

1.0.8 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
