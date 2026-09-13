## Description:

Cite Holmes guides an agent through calibrated deep research, iterative search, citation verification, and confidence-graded reporting for fact checks, literature reviews, and source audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and researchers use Cite Holmes to run deep research, fact-checking, literature review, medical evidence lookup, and reference-audit workflows. The skill helps agents produce source-backed reports where claims are graded and citations are checked before inclusion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The verifier can contact arbitrary URLs when checking references.

Mitigation: Run verification in a restricted network environment and avoid processing untrusted or attacker-supplied reference lists.

Risk: Citation verification can be overstated in some modes.

Mitigation: Treat offline output as structural checking only and keep semantic support review in the research workflow before using citations in conclusions.

Risk: Medical citation checks may need additional human review.

Mitigation: Manually review medical citations and source tiers before relying on the report for clinical or health-related claims.

## Reference(s):

- [Search strategies](references/search-strategies.md)
- [Report template and citation schema](references/report-template.md)
- [Medical research mode](references/medical-mode.md)
- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Nature analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)
- [GPTZero report on hallucinated citations](https://medium.com/@ljingshan6/100-fake-citations-just-slipped-through-neurips-2025-peer-review-5f34f4436560)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with citation tables, JSON reference manifests, and optional BibTeX and CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes five-state citation verdicts and CiteScore grades; offline checks are structural only.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
