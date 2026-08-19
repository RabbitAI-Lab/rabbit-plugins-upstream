## Description:

Monitors patent-litigation exposure for a primary company and up to four comparison parties, including potentially litigated patent identification, family and claim analysis, proceeding timelines, case deep dives, inventor activity, geographic exposure, alerts, technology trends, and evidence-backed HTML, JSON, or CSV reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, IP teams, and legal operations users use this skill to monitor patent-litigation exposure around a named target company and comparison parties. It supports evidence-backed reporting while preserving distinctions among allegations, verified records, procedural posture, and analyst inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent-data connector use, public-record research, and local reports can involve confidential parties, scope, or business analysis.

Mitigation: Provide only the parties and scope intended for research, verify PatSnap connections through the official marketplace flow, and keep generated reports out of the skill package when they contain confidential analysis.

Risk: Users could overread monitoring outputs as legal advice, litigation predictions, or final merits conclusions.

Mitigation: Use the skill as an intelligence workflow, not as counsel, and preserve distinctions among allegations, findings, procedural rulings, legal status, exposure, and analyst inference.

Risk: Stale or incomplete proceeding records can misstate current litigation posture.

Mitigation: Verify material case facts against primary tribunal, court, agency, or official-register records current to the report cutoff and label evidence state for each material fact.

Risk: Generated report artifacts may include unsafe links, images, or external text from source material.

Mitigation: Use the artifact's safe rendering behavior: escape external text, reject unsafe URLs and active content, avoid remote JavaScript, and omit unsafe images without dropping the substantive analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/monitor-patent-litigation-risk-ip)
- [PatSnap Global Core Patent Database MCP](https://open.patsnap.com/marketplace/mcp-servers/core-patents)
- [PatSnap Patent Briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap Advanced Patent Search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [HTML report with structured JSON or CSV attachments, plus agent-facing text, Markdown, commands, and configuration guidance as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are target-centric, evidence-backed, and tied to a stated cutoff date; generated reports should remain outside the skill package when they contain confidential analysis.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
