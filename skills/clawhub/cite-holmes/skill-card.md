## Description:

Helps researchers investigate questions, verify bibliographic references against academic registries, and produce research reports with traceable citation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check citations before publication, and generate auditable bibliographies; medical-evidence lookups are also supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference titles, identifiers, URLs, and optionally claim or evidence text may be shared with external academic services or configured judge/NLI endpoints.

Mitigation: For confidential or unpublished work, use --offline and --no-cache, and do not configure judge or NLI URLs.

Risk: A bibliography URL checker can follow redirects toward internal services when processing untrusted references.

Mitigation: Do not expose the MCP verifier as a network service or process untrusted bibliographies until redirect validation is fixed.

Risk: A verified bibliographic record does not establish that the cited source supports a claim or remains unretracted.

Mitigation: Read primary sources and review semantic support and retraction status before relying on consequential conclusions.

## Reference(s):

- [Cite Holmes ClawHub release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](references/verification-details.md)
- [Medical evidence mode](references/medical-mode.md)
- [Report and citation format](references/report-template.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, JSON, BibTeX, CSV, HTML]

**Output Format:** [Research reports and citation-verification reports in Markdown; optional HTML reports and BibTeX, CSV, or JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verdicts and audit details; offline checks cannot establish online source validity.]

## Skill Version(s):

3.4.1 (source: server-resolved ClawHub release; skill frontmatter lists 3.3.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
