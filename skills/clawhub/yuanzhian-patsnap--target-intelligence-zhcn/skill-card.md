## Description:

Generates Chinese biomedical target intelligence reports about target biology, drug pipelines, clinical progress, patents, and competitive landscapes using PatSnap life-science MCP services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and life-science researchers use this skill to answer target, drug, indication, clinical-trial, patent, and competitive-intelligence questions in Chinese. It guides the agent through structured PatSnap data retrieval, optional web-search supplementation, and evidence-based reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PatSnap API keys are credentials and may be exposed if copied into shared prompts, logs, or configuration snippets.

Mitigation: Use a dedicated PatSnap API key, keep it out of shared transcripts and repositories, rotate it if exposed, and remove the MCP configuration when access is no longer needed.

Risk: Target, drug, disease, and clinical queries are sent to PatSnap external life-science data services and may also be sent to web search when database results are insufficient or recency is required.

Mitigation: Install the skill only when this external data access is intended, avoid submitting confidential research questions unless approved, and review organization data-handling requirements before use.

Risk: Biomedical intelligence reports can be incomplete or misleading if search results are summarized without fetching detailed source records.

Mitigation: Follow the skill workflow that requires fetch steps after searches and review final conclusions against the retrieved PatSnap records before relying on the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/target-intelligence-zhcn)
- [PatSnap developer documentation](https://open.patsnap.com/devportal)
- [PatSnap Life Science](https://eureka.patsnap.com/ls-landing)
- [Pharma Intelligence MCP service](https://open.patsnap.com/marketplace/mcp-servers/096456)
- [Biology Modality MCP service](https://open.patsnap.com/marketplace/mcp-servers/06e741)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Chinese Markdown report with structured sections, summary, conclusion, and optional shell commands for MCP setup]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use uppercase Roman-numeral chapters and require a conclusion grounded in retrieved data.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
