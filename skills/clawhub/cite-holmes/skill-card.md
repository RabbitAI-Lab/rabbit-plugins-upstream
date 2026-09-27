## Description:

Cite Holmes helps agents research questions and check citations against source material and academic registries before presenting a sourced report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check claims and bibliographies, and prepare research reports with citation verdicts and evidence grades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation may bring confidential drafts or sensitive medical or legal research into scope.

Mitigation: Review suitability before installation; use --offline for sensitive work and independently review consequential conclusions.

Risk: Online checks send citation titles, identifiers, and checked URLs to external academic services.

Mitigation: Avoid online checks for confidential bibliographies, or use --offline when external disclosure is unacceptable.

Risk: The default local cache may retain sensitive verification data.

Mitigation: Use --no-cache for sensitive work.

Risk: An optional external judge can receive research content at an endpoint chosen by the user.

Mitigation: Do not set --judge-url unless the endpoint is trusted and its data handling is acceptable.

## Reference(s):

- [Cite Holmes release on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Citation verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown reports; optional HTML, JSON, CSV, and BibTeX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verdicts, evidence grades, and optional audit records and verified bibliography.]

## Skill Version(s):

3.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
