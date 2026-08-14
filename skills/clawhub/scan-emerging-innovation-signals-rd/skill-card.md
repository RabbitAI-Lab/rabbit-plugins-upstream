## Description:

Identify potentially protectable technical contributions in R&D updates, meeting notes, design documents, architecture descriptions, experiment records, and technical-improvement narratives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, engineering, and IP teams use this skill to screen technical updates, design records, meeting notes, and experiment materials for innovation signals that may need patent review, trade-secret review, evidence collection, or invention-disclosure follow-up. It supports early triage only and keeps screening separate from legal conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive R&D records and IP-triage materials.

Mitigation: Confirm authorization and approved handling before providing confidential materials.

Risk: Optional patent-search queries may send source-derived technical details to external patent-search tools.

Mitigation: Minimize query content, avoid unauthorized confidential details, and document search scope, cutoff, and coverage limits.

Risk: Early screening could be mistaken for a legal conclusion about patentability, ownership, infringement, validity, freedom to operate, or filing strategy.

Mitigation: Treat outputs as triage signals and route legal, filing, trade-secret, disclosure, ownership, inventorship, infringement, validity, and FTO questions to qualified IP professionals or counsel.

## Reference(s):

- [Innovation Extraction Prompt](references/innovation_extraction_prompt.md)
- [Innovation Taxonomy](references/innovation_taxonomy.md)
- [Follow-up Question Library](references/followup_questions.md)
- [PatSnap MCP Search Guide](references/mcp_usage_guide.md)
- [Screening and Technical-Evidence Criteria](references/patentability_criteria.md)
- [Protection-Path Decision Framework](references/protection_decision.md)
- [Innovation Signal Radar HTML Report Template](references/html_template.md)
- [PatSnap Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Structured analysis and self-contained HTML report guidance, with optional tool queries and reproducible search logs when authorized.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs distinguish source facts, analyst paraphrases, analyst inferences, missing evidence, screening signals, follow-up questions, and specialist-review needs.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
