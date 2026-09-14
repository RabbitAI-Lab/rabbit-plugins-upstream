## Description:

Industry Deep-Dive Pipeline turns topic briefs, research materials, vendor cases, policy events, or industry questions into an approved Markdown deep-dive article with evidence tables, originality review, planning gates, review records, and final checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External writers, analysts, and research teams use this skill to convert sourced technology, AI, data, cloud, or enterprise-software briefs into a single evidence-backed long-form Markdown article. It is intended for structured research writing that needs fact verification, originality checks, human planning gates, review records, revision, and final evidence packaging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private writing profiles, local source paths, or sensitive source materials may be exposed in article work files if the operator provides them carelessly.

Mitigation: Keep private writing profiles and source materials in a project-private directory, review local paths before use, and rely on the documented scanner checks for credentials, personal paths, and profile red lines before final delivery.

Risk: A draft can become misleading if unverified facts, stale dates, vendor-reported numbers, or user assumptions are promoted into strong conclusions.

Mitigation: Use the fact table, source-tier rules, originality review, human gates, and final re-check before approving the Markdown article.

Risk: Skipping the planning and review gates may produce a complete article around an unapproved angle or unresolved editorial tension.

Mitigation: Require Gate A before drafting, use Gate B for real trade-off decisions, and rerun the machine gate after revisions.

## Reference(s):

- [Evidence and Originality](references/evidence-and-originality.md)
- [Planning Schema](references/planning-schema.md)
- [Replay Evaluation](references/replay-evaluation.md)
- [Writing Profile Interface](references/writing-profile-interface.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown files, JSON gate reports, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a local case bundle ending in an approved article, fact table, originality review, planning brief, review record, final check, and final package; it does not produce publication layouts, covers, social copy, CMS drafts, or external publishing actions.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
