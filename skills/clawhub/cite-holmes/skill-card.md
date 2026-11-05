## Description:

Researches questions and checks bibliography records against academic registries, then produces evidence-graded reports and exportable citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and writing teams use Cite Holmes to discover literature, check references for existence and metadata issues, and produce evidence-graded research reports or bibliography exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Redirects may reach private services, and offline mode may not prevent every network request.

Mitigation: Restrict private-network access and outbound traffic, especially when processing untrusted or confidential bibliographies; review the selected options before running.

Risk: Online lookups disclose citation metadata, and configured judges receive claims and evidence.

Mitigation: Use only data approved for those external services, review configured endpoints, and independently review citation results.

Risk: The reported security validation used source inspection and isolated mocks; live endpoints and resolved dependencies were not tested.

Mitigation: Pin installation sources and review the skill and its citation results before use.

## Reference(s):

- [Verification details](artifact/references/verification-details.md)
- [Security and behavior declaration](artifact/references/security.md)
- [Report template](artifact/references/report-template.md)
- [Cite Holmes project (linked in README)](https://github.com/docsor1212/cite-holmes)
- [ModelScope mirror (linked in README)](https://modelscope.cn/skills/Docsor/cite-holmes)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Bibliography formats (BibTeX, RIS, GB/T 7714)]

**Output Format:** [Evidence-graded research and citation-verification reports, with optional structured workpapers and bibliography exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports distinguish verified, partial, unverified, and unreachable references; a verified record alone does not establish that the source supports a claim.]

## Skill Version(s):

6.1.0 (source: artifact/SKILL.md frontmatter, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
