## Description:

Helps agents research questions and check citations against scholarly registries before presenting sourced reports or bibliographies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, audit references for fabricated or retracted sources, and prepare cited reports and bibliography exports. Unreachable sources and claims not supported by a source still require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional external judging endpoints can receive research text, including confidential drafts.

Mitigation: Use external judging only with trusted endpoints and avoid submitting confidential drafts to unapproved services.

Risk: Networked verification and the optional MCP server may expose research data or accept unintended callers.

Mitigation: Keep MCP transports bound to localhost unless callers are controlled; use offline mode to avoid network access and no-cache mode to avoid storing verification results.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Citation verification details](references/verification-details.md)
- [Security and behavior declaration](references/security.md)
- [Medical research guidance](references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Bibliography data, Guidance]

**Output Format:** [Cited research reports, citation-verification reports, structured audit data, and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts and evidence grades; exports may include BibTeX, RIS, CSV, and GB/T 7714.]

## Skill Version(s):

4.3.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
