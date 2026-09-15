## Description:

Verify or normalize biomedical and life-science reference lists for AI-caused reference errors by checking identifiers and bibliographic fields, preserving source evidence, and producing a searchable offline report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[emp-tca](https://clawhub.ai/user/emp-tca)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, editors, reviewers, and developers use this skill to verify whether biomedical references are authentic, detect DOI or PMID mismatches, normalize citation style, and generate retained audit reports without overwriting the source document.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification mode contacts public bibliographic services and may disclose DOI, PMID, or reference title values.

Mitigation: Use format-only mode or disable PubMed/OpenAlex when local-only handling is required; provide API keys or contact email only when intentionally sending them to providers.

Risk: Formatting-only output does not prove that references are authentic.

Mitigation: Use the verification pipeline before treating references as verified, and keep unavailable or unresolved references out of final citations.

## Reference(s):

- [Verification Policy](references/verification_policy.md)
- [ClawHub Skill Page](https://clawhub.ai/emp-tca/skills/biomedical-reference-verifier)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration]

**Output Format:** [Markdown reports, HTML report files, JSON audit artifacts, fixed reference-list files, and concise chat summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verification mode can query Crossref, PubMed, and OpenAlex; format-only mode is local-only.]

## Skill Version(s):

1.2.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
