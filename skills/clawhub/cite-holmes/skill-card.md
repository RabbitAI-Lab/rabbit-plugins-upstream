## Description:

Deep research that calibrates scope, searches iteratively, and verifies every citation against official registries to identify hallucinated references, fabricated identifiers, unreachable sources, and citations needing human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, students, analysts, and developers use this skill to produce sourced research reports and to audit bibliographies before submission or publication. It is also useful as a standalone citation checker for DOI, PMID, arXiv, URL, BibTeX, and medical-reference verification workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation verification can perform broad outbound network checks and has an SSRF-style risk when processing arbitrary user-supplied URLs.

Mitigation: Avoid feeding untrusted third-party URL lists into the CLI or MCP tool on machines with internal network access; run explicit citation-audit tasks in a constrained network environment.

Risk: Sensitive draft titles, identifiers, and reference metadata may be sent to external registries during online verification or retained in the local cache.

Mitigation: Use --offline for structure-only checks on sensitive drafts and --no-cache when local persistence is not appropriate.

Risk: A mechanically verified citation is not proof that the cited source supports the claim.

Mitigation: Keep the semantic support check and human-review workflow in place, and treat partial, unreachable, unverified, or contradicted references as review items rather than publishable support.

## Reference(s):

- [Cite Holmes ClawHub release page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](references/search-strategies.md)
- [Report template and reference schema](references/report-template.md)
- [Verification details](references/verification-details.md)
- [Medical research mode](references/medical-mode.md)
- [FAQ](references/faq.md)
- [Nature analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [GPTZero hallucinated-citation report](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown research reports and verification reports, plus optional BibTeX, CSV, JSON audit workpapers, HTML reports, and MCP tool JSON responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include per-reference verdicts, CiteScore summaries, evidence-grade markers, human-review sections for unresolved references, and optional verified-only bibliography exports.]

## Skill Version(s):

1.13.0 (source: server release evidence and _meta.json; SKILL.md frontmatter says 1.12.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
