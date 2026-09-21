## Description:

Feeds a paper draft to extract citations, verify them against local, Semantic Scholar, and OpenAlex sources, detect fabricated references, and generate a structured integrity report for researchers, reviewers, and literature-survey authors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[diamond2nv](https://clawhub.ai/user/diamond2nv)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, reviewers, and literature-survey authors use this skill to audit draft citations, flag fabricated or unverifiable references, and produce an integrity report before submission or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local drafts or PDFs and call external scholarly APIs, which may expose confidential manuscript content.

Mitigation: Run it only on material suitable for external API processing, or configure and confirm a local-only workflow before auditing confidential manuscripts.

Risk: The skill can write local reports or configuration and optionally interact with Zotero write/ingest features.

Mitigation: Review generated changes, require explicit approval before Zotero write or ingest actions, and keep backups of Zotero libraries and configuration.

Risk: Citation verification depends on local indexes and upstream services that can be incomplete, unavailable, or rate limited.

Mitigation: Manually review suspected, not-found, fabricated, and error classifications before relying on the report for academic or publication decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/diamond2nv/skills/hfpclawer-academic-integrity)
- [hfpapers-crawler GitHub Repository](https://github.com/diamond2nv/hfpapers-crawler)
- [hfpclawer PyPI Package](https://pypi.org/project/hfpclawer/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain-text integrity reports with inline shell and YAML configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports classify citations as verified, suspected, not found, fabricated, or error and may include remediation recommendations.]

## Skill Version(s):

0.19.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
