## Description:

面向学生的全科错题本，用于记录具体错题、归类四类错因、统计 28 天内重复弱项，并在需要时生成错题集或交接给学科分析技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Students and education agents use this skill to capture specific wrong-answer cases, identify likely error causes, maintain weak-point counts, and produce review artifacts such as similar-practice prompts, mistake collections, and term mistake reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cross-skill writebacks could change stored learning records if sender identity and route permissions are not enforced outside user-controlled JSON fields.

Mitigation: Require authenticated platform sender identity, type-specific route authorization, and consent checks before accepting profile or deep-analysis writebacks.

Risk: The skill handles student mistake records, weak-point status, and sharing controls that may expose sensitive learning data if persisted or shared unexpectedly.

Mitigation: Honor the documented view, correction, deletion, pause, export, and cross-skill sharing controls before storing records or sending handover payloads.

Risk: Wrong-answer classification and generated practice may be inaccurate when the problem statement, student process, or answer evidence is incomplete.

Mitigation: Ask for missing problem details, label low-confidence judgments as insufficient evidence, require student confirmation before long-term archive writes, and self-check generated practice items.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-correction-notebook)
- [各科错因判定线索与子类型对照](artifact/references/error-analysis-framework.md)
- [全库统一词表](artifact/shared/vocab.md)
- [Handover protocol schema](artifact/shared/handover-protocol.schema.json)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown responses with structured JSON handover payloads when cross-skill coordination is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce wrong-answer archive entries, weak-point summaries, similar-practice prompts, review-pack outlines, term reports, and consent-gated handover payloads.]

## Skill Version(s):

2.1.10 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
