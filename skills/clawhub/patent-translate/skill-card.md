## Description:

Fetches US, European, Japanese, or Korean patent titles, abstracts, and claims and translates them into Chinese with consistent patent terminology and a glossary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent researchers, engineers, and other external users translate foreign patent abstracts and claims into Chinese for understanding and technical review, with an accompanying terminology glossary. Professional verification is needed for formal filings or litigation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent numbers, search terms, and API credentials may be sent to the external PatentMax service.

Mitigation: Confirm the service and data-sharing policy before use; avoid submitting confidential patent material or credentials unless approved.

Risk: Patent data requests and broader search or analytics actions can incur charges.

Mitigation: Check applicable pricing and free quotas, tell users about expected costs, and authorize paid requests before running them.

Risk: The bundled client persists trial keys and task or patent caches under ~/.patentmax.

Mitigation: Review local credential and cache retention, restrict access to these files, and remove them when no longer needed.

Risk: Changing PATENTMAX_BASE_URL could route patent data and credentials to another destination.

Mitigation: Leave the default service URL unchanged unless the replacement endpoint is trusted and approved.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-translate)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](references/api-reference.md)
- [PatentMax troubleshooting](references/faq.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, CSV glossary]

**Output Format:** [Chinese patent translation in Markdown and UTF-8 CSV terminology table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the original claims alongside their translations; machine-assisted translations are for reference, not formal use.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
