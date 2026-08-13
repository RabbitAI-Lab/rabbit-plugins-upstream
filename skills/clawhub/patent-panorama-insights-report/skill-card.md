## Description:

Generates a client-ready patent panorama insights report from upstream statistics, value signals, tagging outputs, SaaS-tagged patent pools, and related evidence files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP strategy teams, and agent operators use this skill as the final reporting stage of a patent panorama workflow. It turns validated search, statistics, tagging, value-signal, and SaaS-tagged pool inputs into an evidence-labeled HTML insights report and supporting manifest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may process proprietary patent datasets and authorized platform results.

Mitigation: Use it only for the intended patent panorama reporting workflow, confirm the user is authorized to process the data, and review generated reports before sharing.

Risk: Patent signals and generated recommendations could be mistaken for formal legal conclusions.

Mitigation: Keep the report framed as analysis and risk signals; require qualified legal review for FTO, infringement, SEP, validity, novelty, or inventiveness decisions.

Risk: Incomplete upstream inputs or missing platform configuration can reduce report completeness.

Mitigation: Verify required upstream files, data cutoff, report mode, evidence levels, limitations, and requested output language before distributing the report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/patent-panorama-insights-report)
- [Open Platform marketplace listing](https://open.zhihuiya.com/marketplace/skill-hub/patent-panorama-insights-report)
- [PatSnap Open Platform](https://open.zhihuiya.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Self-contained HTML report plus JSON manifest, with optional evidence register, limitations notes, and recommended patent package files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local report files and presents findings with evidence levels, data-source mapping, limitations, and review guidance.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
