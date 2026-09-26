## Description:

Cite Holmes guides sourced deep research and checks bibliography entries against academic registries before reporting citation verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check claims and bibliography entries, and produce evidence-graded reports or citation audits, including for medical literature review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research topics, reference titles, identifiers, and some scholarly context may be sent to academic services during verification.

Mitigation: Use --offline for sensitive bibliographies; review what will be queried before running online checks.

Risk: Optional external judging or proxy routing may expose claim and evidence text beyond the academic services named in the skill's security declaration.

Mitigation: Avoid --judge-url and --proxy unless you trust the configured endpoint and understand its data handling.

Risk: Cached verdicts can retain sensitive bibliography details locally.

Mitigation: Use --no-cache for sensitive work.

Risk: A verified citation establishes bibliographic consistency, not that a source supports a claim or that a medical conclusion is sound.

Mitigation: Read the cited source, inspect semantic support and human-review flags, and seek qualified review for clinical decisions.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical research mode](artifact/references/medical-mode.md)
- [Report template and reference schema](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Research reports, Citation audits, Guidance, Shell commands, Files]

**Output Format:** [Markdown reports; optional HTML, JSON, CSV, and BibTeX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verdicts, evidence grades, and human-review flags; optional machine-readable audit trail.]

## Skill Version(s):

3.0.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
