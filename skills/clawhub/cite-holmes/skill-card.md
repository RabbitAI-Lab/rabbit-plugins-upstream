## Description:

Cite Holmes guides source-checked deep research and verifies bibliographic references against academic registries before producing cited reports or citation audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to investigate questions, check reference lists and in-text citations, and prepare reports or bibliographies with clearly labeled verification results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Checking untrusted reference URLs can follow redirects to internal network targets.

Mitigation: Avoid untrusted reference lists on sensitive networks until the redirect path is fixed; use offline verification when appropriate.

Risk: Reference checks make outbound requests, and optional remote judging endpoints may receive confidential manuscript content.

Mitigation: Use only local or trusted judging endpoints for confidential material; choose --offline to prevent outbound checks or --no-cache to avoid retaining cached results.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Search strategies](artifact/references/search-strategies.md)
- [Verification details](artifact/references/verification-details.md)
- [Medical evidence mode](artifact/references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Bibliography data, Guidance]

**Output Format:** [Cited Markdown research reports and verification reports; optional JSON workpapers and bibliography exports (BibTeX, RIS, GB/T 7714, CSV)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-reference verification verdicts, confidence labels, and human-review flags]

## Skill Version(s):

3.12.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
