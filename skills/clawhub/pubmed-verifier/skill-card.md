## Description:

Batch-verifies PMID citations against PubMed and checks whether real PMIDs match the claimed paper, with five-state verdicts, DOI cross-checking, retraction detection, fallback metadata sources, caching, and HTML, JSON, or text reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, medical writers, evidence teams, and developers use this skill to audit PMID and DOI citations in manuscripts, evidence libraries, teaching materials, and AI-generated content. It helps identify invalid citations, mismatched papers, partial metadata matches, retracted works, and unverifiable network-dependent results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs networked PubMed, Europe PMC, and Crossref lookups despite local-execution wording.

Mitigation: Install it only when networked citation verification is desired, and review outbound API use before running it in restricted environments.

Risk: Scanning broad private directories can expose citation metadata and file context to external scholarly APIs during verification.

Mitigation: Point the verifier only at intended source files or directories, and avoid API key or email options unless sharing those values with the documented APIs is acceptable.

Risk: The verifier can cache citation metadata locally.

Mitigation: Use the documented no-cache behavior when local citation metadata retention is not desired.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docsor1212/skills/pubmed-verifier)
- [PubMed E-utilities API Quick Reference](references/api_examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, HTML, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands; generated verifier reports in text, JSON, or HTML.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verdicts use correct, mismatch, partial, invalid, and unknown states; network failures are reported as unknown rather than invalid.]

## Skill Version(s):

2.3.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
