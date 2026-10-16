## Description:

Supports source-grounded research and checks bibliographic references against publication registries before they are cited.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate questions, check whether cited works exist and support claims, and prepare research reports or pre-submission bibliography reviews. It distinguishes incomplete or unreachable checks from verified references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live citation checks may follow bibliography URLs or redirects to internal network locations.

Mitigation: Review untrusted citation URLs before running live checks; use a restricted network environment where appropriate.

Risk: Optional external judging endpoints may receive claim and evidence text from private drafts.

Mitigation: Do not enable optional judge or NLI endpoints for private material unless you control and trust the endpoint.

Risk: Verification writes a local cache and may be incomplete when network checks fail.

Mitigation: Review locally stored material and treat incomplete checks as requiring human follow-up rather than verified citations.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](artifact/references/verification-details.md)
- [Report template](artifact/references/report-template.md)
- [Scope and limitations](artifact/references/out-of-scope.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Bibliography exports]

**Output Format:** [Markdown research and citation-verification reports; optional JSON workpapers and BibTeX, RIS, or CSV exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts, confidence grades, and flags for unresolved checks]

## Skill Version(s):

4.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
