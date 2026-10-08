## Description:

Researches questions and checks citations against source material and scholarly registries, reporting verification status and unresolved gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, writers, and developers use this skill to investigate a question or audit a bibliography before relying on citations. It provides source-checked reports, reference verdicts, and exportable audit records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Online verification can send reference identifiers and titles to external services; untrusted reference URLs can trigger outbound requests.

Mitigation: Avoid unpublished or confidential material unless using offline/local-only settings; review untrusted reference lists before online checks.

Risk: Optional judge and NLI endpoints can receive material submitted for evaluation.

Mitigation: Configure those endpoints only when they are trusted and under your control.

Risk: A default local cache can retain earlier reference-check results.

Mitigation: Disable the cache when local reuse is unwanted.

Risk: A reference that exists may still fail to support a claim, and retrieval failures do not prove fabrication.

Mitigation: Read the underlying sources and review partial or unreachable citations before relying on the report.

## Reference(s):

- [Cite Holmes on ClawHub](https://clawhub.ai/docsor1212/skills/cite-holmes)
- [Verification details](references/verification-details.md)
- [Medical evidence mode](references/medical-mode.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, BibTeX, CSV, Guidance]

**Output Format:** [Research summaries and citation-check reports, with optional structured audit and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reference verdicts distinguish verified, partial, unverified, unreachable, and invalid; offline checks cannot establish verification.]

## Skill Version(s):

3.8.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
