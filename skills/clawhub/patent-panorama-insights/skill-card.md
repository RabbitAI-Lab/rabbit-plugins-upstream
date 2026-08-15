## Description:

Patent Panorama Insights helps an agent run PatSnap/zhihuiya-based patent panorama workflows for landscape analysis, competitor intelligence, technology roadmaps, portfolio planning, and evidence-backed single-file HTML reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

External patent, product, R&D, and IP teams use this skill to turn business questions into reproducible PatSnap/zhihuiya patent searches, panorama statistics, taxonomy checkpoints, manual tagging handoffs, and evidence-backed HTML decision reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill queries PatSnap/zhihuiya patent MCP services and writes local CSV, JSON, and HTML report files.

Mitigation: Install only when this patent MCP use is intended, configure credentials through the host platform, and review query checkpoints before execution.

Risk: Legal, licensing, transfer, invalidation, and risk outputs could be mistaken for legal advice.

Mitigation: Treat those outputs as follow-up signals and route legal conclusions to qualified counsel.

Risk: Missing PatSnap/zhihuiya MCP credentials or endpoint permissions can prevent the workflow from running.

Mitigation: Confirm required MCP endpoints and credentials in the host platform before starting a patent analysis.

## Reference(s):

- [Query & Taxonomy Construction Methodology](artifact/references/query-and-taxonomy-methodology.md)
- [Report HTML Blueprint](artifact/references/report-html-blueprint.md)
- [Report Visual Style](artifact/references/report-visual-style.md)
- [Scenario: Industry Landscape](artifact/references/scenario-industry-landscape.md)
- [Scenario: Technology Evolution](artifact/references/scenario-technology-evolution.md)
- [Scenario: Competitor Portrait](artifact/references/scenario-competitor-portrait.md)
- [Scenario: Solution Deep Dive](artifact/references/scenario-solution-deep-dive.md)
- [Scenario: Patent Package And Index](artifact/references/scenario-patent-package-and-index.md)
- [Scenario: Asset And Risk Signals](artifact/references/scenario-asset-and-risk-signals.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus generated CSV, JSON, and self-contained HTML report files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connected PatSnap/zhihuiya patent MCP endpoints and may write local CSV, JSON, and HTML files during workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
