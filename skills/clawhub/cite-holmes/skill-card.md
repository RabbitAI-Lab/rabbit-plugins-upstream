## Description:

Cite Holmes is a deep research skill that calibrates scope, searches iteratively, verifies citations before final reporting, supports medical evidence checks, and exports verified bibliographies and audit ledgers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, analysts, and writers use this skill to produce source-grounded research reports, fact checks, literature reviews, and citation-audit outputs before relying on references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verifier may send citation URLs, DOIs, and PMIDs to external sites during checks.

Mitigation: Use an outbound-network policy or sandbox for sensitive reference lists, and avoid submitting confidential identifiers to external services.

Risk: A mechanically verified reference is not proof that the source is truthful or that it supports the cited claim.

Mitigation: Require semantic source review and keep unsupported, unreachable, or unverified references out of final conclusions.

Risk: Running verification on untrusted reference lists can trigger network access and local report generation.

Mitigation: Review inputs before execution, prefer the packaged scripts/verify_refs.py path, and run strict or offline checks when network access is inappropriate.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search Strategies](artifact/references/search-strategies.md)
- [Report Template and Reference Schema](artifact/references/report-template.md)
- [Medical Evidence Mode](artifact/references/medical-mode.md)
- [Nature analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [NeurIPS 2025 hallucinated citation report](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with citation tables, optional BibTeX and CSV exports, and shell commands for verification workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include CiteScore grades, verified-only bibliography exports, and full audit CSV ledgers when requested.]

## Skill Version(s):

1.4.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
