## Description:

整合单药研发、临床、竞争、交易和专利证据，生成用于立项、管线复盘和 BD 尽调前信息整合的决策支持档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

R&D, BD, portfolio, commercial, and investment-screening teams use this skill to evaluate a single drug across identity, milestones, indications, clinical evidence, competitive landscape, deals, and preliminary patent signals. It supports research and business decision making, not medical, investment, or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Drug, indication, company, and strategy-related queries may be sent to configured pharma intelligence and patent-search services.

Mitigation: Use the skill only for queries that may be shared with those services, and avoid entering confidential or restricted information unless the deployment has approved data-handling controls.

Risk: Generated medical, investment, legal, and patent content can be incomplete or unsuitable for direct decision making.

Mitigation: Treat reports as decision-support research, require expert review, preserve source traceability, and route claim-level patent risk or FTO questions to qualified review.

Risk: Cross-trial comparisons can be misleading when populations, lines of therapy, endpoints, or dates differ.

Mitigation: Use the skill's evidence records, comparability notes, conflict disclosure, and data gap register before relying on comparative conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/drug-lifecycle-evaluation)
- [Legacy deep single-drug report specification](artifact/references/legacy-report-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Structured decision-support report, with deep mode producing an HTML evaluation report file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include source tracking, data cutoffs, disclaimers, cross-validation notes, and data gap disclosure.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
