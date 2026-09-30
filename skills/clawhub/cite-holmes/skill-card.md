## Description:

Guides deep research and checks citations against scholarly registries before presenting sourced findings or a bibliography audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use the skill to investigate questions, assess whether cited sources support claims, and check reference lists before publication or submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted citation URLs can redirect network checks to internal addresses.

Mitigation: Avoid checking untrusted URLs until redirect-based SSRF handling is fixed.

Risk: Network lookups and the local verdict cache may expose sensitive bibliography data.

Mitigation: For sensitive work, use --offline or --no-cache as appropriate and review which lookups are permitted.

Risk: Optional judge and NLI endpoints may receive text submitted for verification.

Mitigation: Set --judge-url or --nli-url only to endpoints approved to receive that text.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Skill documentation](artifact/README.md)
- [Verification details](artifact/references/verification-details.md)
- [Report template and citation schema](artifact/references/report-template.md)
- [Medical research mode](artifact/references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, CSV, BibTeX, HTML, Guidance]

**Output Format:** [Sourced research reports and citation-verification reports in Markdown or HTML, with optional JSON audit records, CSV, and BibTeX exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation verdicts distinguish verified, partial, unverified, unreachable, and invalid references; reports include a CiteScore and review flags.]

## Skill Version(s):

3.3.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
