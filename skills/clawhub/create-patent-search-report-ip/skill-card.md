## Description:

Create the final evidence-backed patent-landscape insight report from validated search, statistics, taxonomy, patent-package, and human-tagging artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent, R&D, strategy, and IP teams use this skill at Stage 4 of a patent-landscape workflow to turn validated upstream search, statistics, taxonomy, value-signal, patent-package, and human-tagging artifacts into a bounded decision-readable report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may summarize confidential patent strategy or analysis data.

Mitigation: Install and use the skill only in workspaces where the upstream patent-search artifacts are intended to be processed, and review generated reports before sharing.

Risk: Patent evidence, value proxies, or package actions may be mistaken for legal, transaction, freedom-to-operate, validity, or valuation advice.

Mitigation: Keep conclusions bounded to the defined dataset and route legal, commercial, transaction, or portfolio decisions to qualified reviewers.

Risk: Missing, incompatible, or unreconciled upstream artifacts can lead to unsupported population, technology-route, value-signal, or package claims.

Mitigation: Use the skill's declared stop or degraded modes, validate input schema/version/count/checksum consistency, and record limitations in report_manifest.json.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-patent-search-report-ip)
- [PatSnap Skill Hub](https://open.patsnap.com/marketplace/skill-hub)
- [PatSnap MCP Marketplace](https://open.patsnap.com/marketplace/mcp-servers)
- [Advanced Patent Search connector](https://open.patsnap.com/marketplace/mcp-servers/patent-search)
- [Patent Briefing connector](https://open.patsnap.com/marketplace/mcp-servers/patent-briefing)
- [Deep Patent Mining connector](https://open.patsnap.com/marketplace/mcp-servers/patent-mining)
- [Global Core Patent Database connector](https://open.patsnap.com/marketplace/mcp-servers/core-patents)

## Skill Output:

**Output Type(s):** [Files, Analysis, JSON, HTML]

**Output Format:** [Self-contained HTML report and JSON report manifest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces report.html and report_manifest.json from validated local patent-landscape artifacts; outputs should be reviewed before sharing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
