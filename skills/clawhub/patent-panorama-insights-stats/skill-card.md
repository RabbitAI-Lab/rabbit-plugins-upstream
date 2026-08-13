## Description:

Generates patent panorama statistics, branch-organized core patent indexes, value-signal files, chart-ready data, and an offline HTML statistics snapshot from validated Patent Panorama search outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts and agent users use this skill after the Patent Panorama search step to turn validated search configuration, candidate pool, and core recall files into landscape statistics, competitor views, core patent indexes, value signals, and a self-contained statistics dashboard.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on PatSnap MCP services and may send patent search scope, candidate patent numbers, and competitor names to those configured services.

Mitigation: Install and run it only in environments where the PatSnap MCP tools are intentionally configured and that data sharing is acceptable.

Risk: Generated patent statistics, value signals, legal-status indicators, and competitor views may be mistaken for legal conclusions.

Mitigation: Review outputs as analytical signals and route legal, FTO, infringement, validity, or enforceability decisions to qualified reviewers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-insights-stats)
- [Open Platform marketplace listing](https://open.zhihuiya.com/marketplace/skill-hub/patent-panorama-insights-stats)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance plus JSON, CSV, chart data, and self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces analytical patent signals and reports; outputs should be reviewed as analysis aids, not legal conclusions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
