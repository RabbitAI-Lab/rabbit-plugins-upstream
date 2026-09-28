## Description:

Supports deep research and citation checking by searching across sources, checking references against scholarly registries, and preparing sourced reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check bibliographies for fabricated or retracted references, and produce evidence-graded reports or verified citation exports. Medical research is supported but requires careful review of the underlying sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference titles, identifiers, URLs, and possibly claim excerpts may be sent to external academic services; network activity is broader than the skill's declaration.

Mitigation: Avoid sensitive internal bibliographies unless using --offline or restricted egress; review permitted outbound services before running.

Risk: User-supplied citation URLs or redirects may contact arbitrary destinations, and custom judge or proxy endpoints may receive research content.

Mitigation: Run in a sandbox and use --judge-url or proxy settings only with trusted endpoints.

Risk: Private references may remain in the local verdict cache after a run.

Mitigation: Use --no-cache for private work.

Risk: A verified reference does not prove the claim it is used to support, especially for clinical decisions.

Mitigation: Read the source and independently review claim support; use --profile medical for clinical research and treat uncertain verdicts as requiring human review.

## Reference(s):

- [Cite Holmes release on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Citation verification details](artifact/references/verification-details.md)
- [Medical research mode](artifact/references/medical-mode.md)
- [Report template and reference schema](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, BibTeX, CSV]

**Output Format:** [Markdown research and verification reports; optional JSON workpapers, BibTeX bibliographies, and CSV audit exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference verdicts distinguish verified, partial, unverified, unreachable, and invalid citations.]

## Skill Version(s):

3.2.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
