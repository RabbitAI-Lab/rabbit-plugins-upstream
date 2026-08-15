## Description:

Retrieves Chinese medical open-access literature from Weipu OA, downloads available PDFs, extracts citation-ready metadata, and verifies Chinese references for hallucinated or mismatched citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to find Chinese medical OA articles, retrieve PDF or metadata records, generate Vancouver/GB-T 7714 style citation data, and verify Chinese references before using them in literature reviews or reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TLS certificate verification is disabled by default for network requests.

Mitigation: Set CN_MED_OA_VERIFY_SSL=1 before use and review downloaded PDFs and metadata before relying on them.

Risk: The skill downloads PDFs from a third-party OA platform and may write files to local output directories.

Mitigation: Keep retrieval user-directed, use explicit output directories, respect the platform terms, and confirm that each downloaded article is open access.

Risk: Weipu OA search can return loosely related results because the platform has broad OR-style matching.

Mitigation: Use specific medical phrases, review the skill's relevance disclosure, and run citation verification before using references.

Risk: Some PDF text layers do not expose page numbers or enough text for full cross-checking.

Mitigation: Treat missing page or PDF verification gaps as requiring human review, and use strict verification when the workflow depends on complete citation metadata.

## Reference(s):

- [ClawHub release: Cn Med Oa Pub](https://clawhub.ai/docsor1212/skills/cn-med-oa)
- [Publisher profile: docsor1212](https://clawhub.ai/user/docsor1212)
- [Weipu OA Platform](https://oa.cqvip.com)
- [Weipu OA API Contract](references/weipu-oa-api-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with shell commands, Python snippets, citation lines, JSON manifest paths, PDF file paths, and verification report summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When retrieval or verification is run, the skill may create downloaded PDFs, cn_refs.json manifests, and HTML or JSON verification reports in user-selected output directories.]

## Skill Version(s):

2.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
