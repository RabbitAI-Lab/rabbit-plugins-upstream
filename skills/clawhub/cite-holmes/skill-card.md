## Description:

Researches questions and checks citations against source records before presenting findings or exporting a verified bibliography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check whether cited works and identifiers exist, and prepare source-linked reports or audited bibliographies. Its medical mode supports evidence lookup but does not replace clinical review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Citation checks can request supplied URLs, including internal network addresses; the URL checker has an SSRF exposure and network activity is broader than the skill's disclosure.

Mitigation: Review reference URLs before use and avoid running the checker on networks exposing internal HTTP services until redirect and DNS-based protections are tightened.

Risk: Sensitive reference lists may remain in the local verdict cache.

Mitigation: Use --no-cache or a private --cache-path for sensitive bibliographies.

Risk: A verified citation may exist without supporting the report's claim.

Mitigation: Read cited sources, check claim support, and obtain expert review for clinical conclusions.

## Reference(s):

- [Cite Holmes release on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Report template and citation schema](artifact/references/report-template.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, BibTeX, HTML]

**Output Format:** [Source-linked research reports and citation verdicts; optional bibliography and audit exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Five citation verdicts, graded conclusions, and references flagged for human review]

## Skill Version(s):

2.0.0 (source: ClawHub release; bundled SKILL.md frontmatter lists 1.12.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
