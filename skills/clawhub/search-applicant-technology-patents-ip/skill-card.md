## Description:

Search patents owned or filed by one or more specified applicants within a defined technology topic.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

IP searchers and patent analysts use this skill to build applicant-first, topic-constrained PatSnap search strategies, with a gated path for either formula-only work or executed retrieval and dataset preparation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live retrieval requires PatSnap access and may expose credentials if API keys are copied into reports, logs, or version control.

Mitigation: Configure PatSnap only when retrieval is needed, keep API keys out of generated artifacts, and use the official Connect panel for current connection details.

Risk: Generated patent datasets may be incomplete or unsuitable for business or legal decisions without review.

Mitigation: Review retrieved records, deduplication choices, representative-family selection, and boundary assumptions before relying on outputs.

Risk: Formula shortcuts or premature retrieval can produce poorly scoped applicant-topic results.

Mitigation: Follow the required Step 0-7 pre-retrieval gate and stop when any gate fails or requires user confirmation.

## Reference(s):

- [Applicant-Topic Patent Retrieval Workflow](references/applicant-retrieval-workflow.md)
- [Topic Limitation Workflow](references/topic-limitation-workflow.md)
- [PatSnap Open Platform](https://open.patsnap.com/)
- [PatSnap Authentication Guide](https://open.patsnap.com/devportal/guides/authentication)
- [Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown reports, PatSnap query formulas, retrieval audit tables, dataset handoff notes, and setup guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [In formula-only mode, outputs an executable search strategy and checklist with dataset_status: not_executed. In retrieval-dataset mode, outputs retrieval provenance, deduplicated datasets when available, Markdown report, and Word report unless opted out.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
