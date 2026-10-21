## Description:

Guides research and literature discovery while checking citations against registries and reporting evidence strength and verification status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check bibliographies for fabricated or retracted sources, and produce reports with clearly labeled citation verdicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live reference checks may send research material to external services, beyond the services listed in the skill's security description.

Mitigation: For sensitive or unpublished work, use --offline where suitable and only enable external judging endpoints or proxies that are approved for the data.

Risk: Local caching may retain research material after a verification run.

Mitigation: Use --no-cache when retention is inappropriate and review local cache handling.

Risk: A mutable GitHub install path mentioned in the documentation may differ from the reviewed release.

Mitigation: Prefer the reviewed ClawHub package unless the separately installed source has also been reviewed.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](references/verification-details.md)
- [Security and data handling](references/security.md)
- [Report template](references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Bibliography files, Guidance]

**Output Format:** [Markdown research or verification reports, JSON workpapers, and optional BibTeX, GB/T 7714, RIS, or CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes evidence grades and citation verdicts; unavailable checks are labeled for human review.]

## Skill Version(s):

4.5.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
