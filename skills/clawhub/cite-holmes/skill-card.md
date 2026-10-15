## Description:

Helps agents research questions, verify references against academic registries, and produce evidence-graded reports or citation-check results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check whether citations are authentic, and prepare sourced reports or bibliographies for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Network requests may extend beyond the limits described in the skill's security documentation.

Mitigation: Review network behavior before use; for sensitive work, prefer offline mode and disable caching if needed.

Risk: An exposed HTTP/SSE server could accept requests from untrusted clients.

Mitigation: Keep the MCP server on stdio or localhost; do not expose HTTP/SSE mode to untrusted clients.

Risk: External judging endpoints could receive private manuscript content.

Mitigation: Do not use external judge or NLI endpoints with private manuscripts unless the endpoint is trusted.

Risk: Unverified or human-check references could be mistaken for confirmed citations.

Mitigation: Manually review all non-verified and human-check items before citing them.

## Reference(s):

- [Cite Holmes release on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Citation verification details](references/verification-details.md)
- [Research report and reference format](references/report-template.md)
- [Security and behavior declaration](references/security.md)

## Skill Output:

**Output Type(s):** [Research guidance, Markdown reports, Citation verification results, Bibliography exports]

**Output Format:** [Markdown reports and structured citation results; optional BibTeX, RIS, CSV, and JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes citation verdicts and evidence grades; unresolved references require human review.]

## Skill Version(s):

3.17.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
