## Description:

Designs, audits, and executes user-requested modernization of historical folders into privacy-aware, reviewable Agent Assets for personal knowledge retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lee-agi](https://clawhub.ai/user/lee-agi)

### License/Terms of Use:

Apache-2.0 OR MIT-0

## Use Case:

Developers, knowledge workers, and agent operators use this skill to plan, review, and run local-first conversion of mixed historical folders into Agent-readable assets, review workbenches, durable manifests, and optional retrieval indexes. It is intended for user-selected assetization, audit, review, sync, and indexing workflows rather than ordinary file reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filesystem-changing stages can move, archive, delete, synchronize, or index local content when explicitly enabled.

Mitigation: Review the selected root, scope, and decisions first; use plan-only or dry-run before enabling execution flags such as --execute-decisions, --execute-extraction, --execute-sync, or --execute-index.

Risk: Personal or sensitive material could be included in generated assets or indexes if scope and privacy review are wrong.

Mitigation: Keep PII and secret-like paths out of content extraction, treat unknown privacy as not final, and index only reviewed non-PII assets after a clean readiness audit.

Risk: Optional provider-backed summaries, embeddings, or reranking can transmit bounded note or index text to an external provider.

Mitigation: Leave remote provider features disabled unless the user has approved the provider, transmitted text scope, and flags such as --allow-semantic-rerank.

Risk: Local review workbench actions can save or apply decisions when write or apply capabilities are enabled.

Mitigation: Keep the workbench read-only unless additional capability is needed, and enable file-open, write, or apply actions separately for the selected review page.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lee-agi/skills/agent-os-asset)
- [README](artifact/README.md)
- [Security boundaries and migration](artifact/references/security-boundaries.md)
- [License](artifact/LICENSE)
- [Third-party notices](artifact/THIRD_PARTY_NOTICES.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated Agent-readable Markdown assets, JSON/JSONL manifests and decisions, optional HTML review workbenches, and local index files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Filesystem-changing stages require explicit execution flags; provider-backed summaries, embeddings, and reranking are optional opt-ins.]

## Skill Version(s):

0.2.0 (source: SKILL.md frontmatter, package.json, pyproject.toml, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
