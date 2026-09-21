## Description:

Compare industry evidence with saved JishuDB snapshots; report changes, opportunity hypotheses, and risks. First runs establish a baseline. / 对比JishuDB中的历史行业证据，输出变化、机会假设与风险；首次运行建立基线。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bowen-aijishu](https://clawhub.ai/user/bowen-aijishu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and research teams use this skill to compare current industry evidence against saved JishuDB snapshots, produce first-run baselines, and prepare evidence-backed change briefings, opportunity hypotheses, risks, and open questions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill needs scoped JishuDB write access and can retain source records, snapshots, and generated reports.

Mitigation: Grant write access only for the selected knowledge base and approve retention scope before installation or execution.

Risk: Recurring monitoring can continue using an approved schedule, KB, output location, source scope, and notification destination.

Mitigation: Enable recurrence only after explicitly approving those schedule details and confirming the host scheduler is authorized.

Risk: Industry change briefings may be misleading if prior snapshots, source coverage, or comparable periods are incomplete.

Mitigation: Require the skill to label baseline runs, incompatible evidence, coverage limits, and open questions in its generated outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bowen-aijishu/skills/industry-opportunity-radar)
- [Metadata homepage](https://github.com/x-aijishu/jishudb-skills/tree/main/skills/industry-opportunity-radar)
- [Evidence contract](references/evidence-contract.md)
- [199IT report category](https://www.199it.com/archives/category/report)
- [199IT RSS feed](https://www.199it.com/feed)

## Skill Output:

**Output Type(s):** [text, markdown, CSV, configuration, guidance]

**Output Format:** [Markdown briefings, CSV indicator tables, source notes, revision notes, and saved JishuDB records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include baseline or comparison status, source mappings, evidence IDs, snapshot IDs, and scheduling state when recurrence is requested.]

## Skill Version(s):

0.1.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
