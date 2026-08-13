## Description:

Integrate target biology, disease rationale, drug pipeline, clinical, patent, scientific, regulatory, company, and transaction evidence for target or targeted-asset R&D and business-development decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External life-sciences strategy, R&D, portfolio, and business-development teams use this skill to produce evidence-backed target or targeted-asset assessment reports for initiation reviews, opportunity screens, partnering theses, landscape updates, and go/no-go decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill supports high-impact R&D and business-development research and may influence medical, legal, intellectual-property, financial, or investment-adjacent decisions.

Mitigation: Treat outputs as decision support only and require qualified clinical, regulatory, CMC, commercial, financial, IP, and legal review before material decisions.

Risk: The skill may route queries or supplied information to authorized PatSnap MCPs or public sources.

Mitigation: Use only clearly scoped and approved data, confirm permitted external services before retrieval, and avoid unapproved confidential inputs.

Risk: Dynamic pipeline, clinical, patent, regulatory, transaction, and guideline evidence can become stale or incomplete.

Mitigation: Refresh source retrieval at the decision date, document coverage gaps, and distinguish unavailable evidence from verified zero results.

## Reference(s):

- [Skill release page](https://clawhub.ai/yuanzhian-patsnap/skills/assess-target-drug-bd-opportunities-ls)
- [Deep 21-Section Target and Drug BD Report Specification](references/legacy-report-spec.md)
- [PatSnap target-disease MCP](https://open.patsnap.com/marketplace/mcp-servers/target-disease)
- [PatSnap drug-asset MCP](https://open.patsnap.com/marketplace/mcp-servers/drug-asset)
- [PatSnap clinical-trials MCP](https://open.patsnap.com/marketplace/mcp-servers/clinical-trials)
- [PatSnap patent-search MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [PatSnap patent-briefing MCP](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [PatSnap scientific-translational-evidence MCP](https://open.patsnap.com/marketplace/mcp-servers/scientific-translational-evidence)
- [PatSnap regulatory-guidelines MCP](https://open.patsnap.com/marketplace/mcp-servers/regulatory-guidelines)
- [PatSnap current-awareness MCP](https://open.patsnap.com/marketplace/mcp-servers/current-awareness)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files, Guidance]

**Output Format:** [Markdown or HTML evidence-backed assessment report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed data, analyst inference, assumptions, recommendations, evidence gaps, sources, and monitoring plans.]

## Skill Version(s):

1.0.0 (source: skill.manifest.json and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
