## Description:

Guides deep research, checks citations against reference registries, and produces evidence-graded reports and reference audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and agents use this skill to investigate questions, verify bibliographies and in-text citations, and flag references needing human review before publication. It also supports medical evidence searches with explicit source checking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference verification makes outbound requests and may contact more destinations than the skill's network description suggests.

Mitigation: Review requested destinations and avoid checking untrusted arbitrary URLs.

Risk: An MCP server exposed to untrusted users or networks could be used for unsafe URL or DNS-based requests.

Mitigation: Keep the MCP server local or on stdio until redirect and DNS-based SSRF protections are tightened.

Risk: Optional judge endpoints can receive citation or draft content, and local caching can retain sensitive work.

Mitigation: Disable or carefully choose judge/NLI/fast-judge endpoints; use --no-cache for sensitive drafts.

Risk: A reference can be genuine without supporting the cited claim.

Mitigation: Read the source, check claim-level support, and review flagged or unreachable citations before relying on them.

## Reference(s):

- [Cite Holmes ClawHub release](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)
- [Report template](artifact/references/report-template.md)
- [Best practices](artifact/docs/best-practices.md)

## Skill Output:

**Output Type(s):** [Research reports, Citation-verification results, Bibliography exports, Guidance]

**Output Format:** [Markdown, HTML, JSON, CSV, BibTeX, or RIS]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference verdicts and human-review flags; a verified reference does not establish that it supports a particular claim.]

## Skill Version(s):

3.7.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
