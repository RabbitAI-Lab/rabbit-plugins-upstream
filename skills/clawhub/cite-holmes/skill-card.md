## Description:

Deep research that interrogates its own sources: it calibrates scope, plans sub-questions, searches iteratively across sources and languages, and verifies each citation before producing a confidence-graded report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, researchers, students, clinicians, editors, and developers use this skill to perform deep research, fact-check claims, verify reference lists, and produce reports or bibliography exports whose citations have explicit verification verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online verification of attacker-supplied reference lists can cause the user's machine to contact internal or sensitive network services.

Mitigation: Run online checks only on trusted reference lists, or use --offline and a restricted network environment until redirect and DNS-based SSRF protections are reviewed.

Risk: Citation verification sends URLs, identifiers, and bibliographic metadata to public citation services.

Mitigation: Avoid online verification for confidential bibliographies in sensitive environments; use offline structural checks or approved egress controls.

Risk: A verified citation can still be misread as proof that the cited source supports the claim.

Mitigation: Review the semantic audit, confidence grades, and human-review section before relying on the report for submissions or decisions.

## Reference(s):

- [Cite Holmes ClawHub page](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Report template and citation schema](artifact/references/report-template.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)
- [FAQ](artifact/references/faq.md)
- [Nature news analysis on invalid AI-generated references](https://www.nature.com/articles/d41586-026-00969-z)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown research reports with optional HTML, BibTeX, CSV, and audit JSON exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include citation verdicts, CiteScore, confidence grades, and human-review flags for partial, unreachable, invalid, or unverified references.]

## Skill Version(s):

1.11.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
