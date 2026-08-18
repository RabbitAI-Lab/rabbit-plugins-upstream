## Description:

cn-med-oa retrieves and downloads open-access Chinese medical literature from Weipu OA and verifies Chinese citations with structured metadata, relevance checks, and citation reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and agents use this skill to retrieve open-access Chinese medical articles from Weipu OA, download PDFs when available, generate Vancouver or GB/T 7714 metadata, and verify Chinese citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan says the skill can download files after broad triggers and disables HTTPS certificate verification by default.

Mitigation: Review before installing, run it only for explicit Chinese medical OA literature tasks, set CN_MED_OA_VERIFY_SSL=1, and keep downloads in a bounded directory.

Risk: Downloaded papers may carry license or platform-term obligations outside the skill's control.

Mitigation: Verify each paper's license or terms before storing, sharing, or reusing full text.

Risk: Broad or vague reference-finding prompts can trigger external retrieval with weak user intent.

Mitigation: Require explicit Chinese medical OA retrieval or citation-verification intent before running the skill automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/cn-med-oa-pub)
- [Weipu OA platform](https://oa.cqvip.com)
- [Weipu OA API contract](references/weipu-oa-api-contract.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell commands, Python snippets, JSON manifests, citation text, PDF files, and optional HTML or JSON verification reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include downloaded PDFs, cn_refs.json manifests, GB/T 7714 or Vancouver citation lines, and verification reports.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter, skillhub-meta.json, and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
