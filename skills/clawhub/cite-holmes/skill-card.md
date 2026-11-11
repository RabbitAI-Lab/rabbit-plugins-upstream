## Description:

Research topics and check bibliographies by finding sources, verifying citation details against academic registries, and producing evidence-graded reports and bibliography exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Researchers, students, and developers use Cite Holmes to investigate questions, build literature reviews, check citations, and prepare bibliographies for submission. Its reports distinguish verified, partial, unreachable, invalid, and unchecked references so readers can review uncertain entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Link checks visit URLs supplied in a bibliography, which can expose private services or sensitive information to online checks.

Mitigation: Use restricted network access for untrusted bibliographies, and keep confidential titles and token-bearing URLs out of online checks.

Risk: Citation labels may overstate what the checks establish; registry consistency does not guarantee that a source supports a claim.

Mitigation: Independently inspect important citations and confirm their support in the source, including entries labeled verified or READY.

Risk: The --offline option is not an enforced network boundary, and cached results can persist sensitive material.

Mitigation: Enforce network restrictions outside the skill when required, disable caching for sensitive material, and pin reviewed installation sources.

## Reference(s):

- [Cite Holmes security and behavior declaration](artifact/references/security.md)
- [Cite Holmes verification details](artifact/references/verification-details.md)
- [Crossref API](https://api.crossref.org/)
- [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
- [arXiv API](https://export.arxiv.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Bibliography exports, Shell commands]

**Output Format:** [Markdown or HTML reports, JSON workpapers, and optional BibTeX, RIS, CSV, and GB/T 7714 exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include citation verdicts and human-review flags; registry checks reflect the data available when run.]

## Skill Version(s):

6.3.0 (source: release metadata, SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
