## Description:

生成药物、赛道或技术模态的周期性情报简报，用于按周或按月汇总研发、临床、监管、交易和关键竞争动态，形成管理层简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Pharmaceutical R&D, strategy, and competitive-intelligence users use this skill to generate time-bounded briefs across patents, papers, clinical activity, trial results, deals, and news. It emphasizes deduplication, source traceability, coverage disclosure, and clear separation between facts and inferred implications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated briefs may be mistaken for medical, legal, freedom-to-operate, or final business advice.

Mitigation: Use the brief as monitoring and strategy support only; have qualified reviewers validate clinical, patent, regulatory, and commercial conclusions before action.

Risk: External search coverage or filtering gaps can lead to incomplete or stale intelligence.

Mitigation: Review the skill's retrieval log, coverage notes, failed modules, post-filtering disclosures, source IDs, and unresolved fields before relying on the report.

Risk: The bundled renderer creates local HTML outputs that may include sensitive search topics or organization-specific strategy context.

Mitigation: Write reports to a dedicated workspace folder and apply the user's normal access controls and retention policy for generated outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/pharma-intelligence-brief)
- [Drug type mapping](artifact/references/drug_type_mapping.md)
- [Legacy pharmaceutical intelligence module contracts](artifact/references/legacy-module-contracts.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Validated JSON inputs and HTML intelligence reports rendered by the bundled Python script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill requires explicit monitoring windows, stable source identifiers where available, and visible reporting of empty modules, failed retrievals, post-filtering, and unresolved fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
