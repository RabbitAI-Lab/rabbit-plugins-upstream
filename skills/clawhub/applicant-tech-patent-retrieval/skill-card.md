## Description:

Guides agents through applicant-first patent retrieval constrained by a confirmed technology topic, including applicant entity expansion, topic decomposition, PatSnap/Zhihuiya query construction, deduplication, and report or dataset handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent search professionals, analysts, and agents use this skill to build traceable applicant-plus-topic patent retrieval workflows, from applicant disambiguation and topic boundary confirmation through executable PatSnap/Zhihuiya formulas, datasets, and reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may connect an agent to external PatSnap/Zhihuiya MCP services using the user's API key.

Mitigation: Confirm the MCP services and API key authorization before retrieval, and use the setup self-check before relying on live results.

Risk: Patent retrieval formulas and reports can be misleading if applicant entities, topic boundaries, or noise exclusions are accepted without review.

Mitigation: Require the visible pre-retrieval gates, user confirmation of the applicant field, and manual review of generated formulas before execution or downstream use.

Risk: Generated datasets and reports may be mistaken for validated recall or precision results.

Mitigation: Keep source hit counts separate from downstream representative datasets and avoid claiming recall or precision without executed result sets, samples, and labels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/applicant-tech-patent-retrieval)
- [PatSnap/Zhihuiya Open Platform](https://open.zhihuiya.com/)
- [PatSnap/Zhihuiya MCP marketplace](https://open.zhihuiya.com/marketplace/mcp-servers)
- [Applicant-topic patent retrieval workflow](references/applicant-retrieval-workflow.md)
- [Topic limitation workflow](references/topic-limitation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance, files]

**Output Format:** [Markdown with query formulas, structured tables, execution checklists, optional datasets, and optional Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-confirmed applicant field and topic gates before final formulas or retrieval output.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
