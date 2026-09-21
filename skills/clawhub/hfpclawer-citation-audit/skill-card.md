## Description:

Verify academic paper citations through a fallback pipeline that checks a local FTS5 database, Semantic Scholar, and OpenAlex, supporting both single-citation checks and batch reference-list audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, reviewers, literature-survey authors, and agents use this skill to check whether cited academic papers exist and to audit reference lists for potentially hallucinated or unavailable citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the external Python CLI introduces normal package-supply-chain and execution risk.

Mitigation: Review the package source or pin a known version before installation when reproducibility or trust boundaries matter.

Risk: Citation verification can make network calls to public scholarly APIs and may encounter rate limits or upstream availability issues.

Mitigation: Expect network access during verification, handle ERROR statuses, and configure optional API keys or polite-email settings for higher-volume use.

Risk: Initialization, local data paths, and optional Zotero-related features can read or write local files.

Mitigation: Check config and data paths before running init or enabling Zotero write or ingest workflows, and keep private research metadata in local ignored configuration files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/diamond2nv/skills/hfpclawer-citation-audit)
- [hfpclawer project homepage](https://github.com/diamond2nv/hfpapers-crawler)
- [hfpclawer PyPI package](https://pypi.org/project/hfpclawer/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands, YAML configuration, Python examples, and human-readable citation status results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Citation checks can report VERIFIED, SUSPECTED, NOT_FOUND, or ERROR; batch mode can read references from a text file.]

## Skill Version(s):

0.19.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
