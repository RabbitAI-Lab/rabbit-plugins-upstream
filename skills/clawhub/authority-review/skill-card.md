## Description:

Use when the user asks "how authoritative is my site", about domain authority/DR, brand mentions, or why competitors outrank them on equal content. Reviews entity clarity, independent references, author credibility, and reputation signals from observable and imported evidence. Authority is broader than links; link operations live in backlink-opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[trustgrowth](https://clawhub.ai/user/trustgrowth)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site owners use this skill to review a site's authority signals from observable or imported evidence, including entity clarity, independent references, author credibility, first-party proof, and comparative standing when a peer cohort is provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected mode can involve local MCPs, paid SEO accounts, or credentials.

Mitigation: Confirm which connectors are already configured before use, do not enter new credentials unless the provider is trusted, and avoid printing keys.

Risk: The package references references/provider-selection.md, but that helper file is not included.

Mitigation: Use the included connector tier guidance and clearly state any source-selection limits when reporting authority findings.

Risk: Authority conclusions can be misleading when evidence coverage is thin or competitor data is not collected consistently.

Mitigation: Report insufficient evidence instead of a score, label vendor metrics by provider and date, and require a named peer cohort before comparative claims.

## Reference(s):

- [Connectors and categories](references/connectors.md)
- [Reporting contract](references/reporting.md)
- [ClawHub skill page](https://clawhub.ai/trustgrowth/skills/authority-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report or concise text guidance with evidence labels and limitations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include verdicts, measured observations, missing-evidence notes, and up to three next actions when report-shaped output is warranted.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
