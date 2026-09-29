## Description:

Helps researchers investigate questions, verify citations against scholarly registries, and produce research reports with auditable source checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and reviewers use the skill to investigate claims, check reference lists before submission, and prepare source-backed reports or bibliographies. Medical evidence lookups are supported, but source interpretation still needs human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: URL checking can reach more network destinations than the skill's security declaration suggests, including arbitrary URLs supplied through the MCP server.

Mitigation: Review before enabling the MCP server; do not accept untrusted URL checks on networks with exposed internal services.

Risk: Citation verification and optional judge or NLI endpoints may send sensitive manuscript content over the network.

Mitigation: Prefer offline and no-cache modes for confidential work; use judge and NLI endpoints only when you control them.

Risk: An existing citation or reachable page does not establish that it supports a claim.

Mitigation: Read the cited sources, check semantic support, and review unreachable or uncertain verdicts before relying on the report.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](references/search-strategies.md)
- [Verification details](references/verification-details.md)
- [Medical evidence mode](references/medical-mode.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Bibliography data, Guidance]

**Output Format:** [Markdown reports and citation verdicts; optional HTML, BibTeX, CSV, and JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish verified, partial, unverified, unreachable, and invalid references; optional audit trail.]

## Skill Version(s):

3.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
