## Description: <br>
政采投诉"胜诉率"预判模型（供应商/投诉人攻向）——供应商输入自身遭遇的不公情形，系统通过"投诉事项结构化拆解+5万+真实投诉处理决定类案相似度比对"，以真实检索样本计数给出投诉成功率（成立率）预测，并按"证据充分性"做条件分层（强证据/弱证据分层胜诉率），输出证据收集与补强路线图。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External suppliers and complainants use this skill to assess Chinese mainland government-procurement complaint posture, classify complaint issues, compare similar historical decisions, estimate evidence-conditioned success rates, and plan lawful evidence collection. It is intended as a statistical and procedural aid, not as a legal promise or substitute for professional review. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce percentage-based complaint success estimates that users may overread as legal guarantees. <br>
Mitigation: Require every percentage to be tied to real marked sample counts, confidence notes, Wilson intervals, and a clear disclaimer that outcomes depend on current law and case facts. <br>
Risk: The skill depends on named Chinese government-procurement knowledge bases for case matching and statutory grounding. <br>
Mitigation: Confirm the required knowledge bases are available before use; if unavailable, downgrade to an evidence-pending mode and do not calculate win rates. <br>
Risk: Complaint strategy guidance could encourage unlawful evidence collection if guardrails are ignored. <br>
Mitigation: Limit evidence-collection recommendations to lawful channels such as information requests, third-party testing, public administrative records, and formal review or investigation procedures. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/chesaram/skills/gp-complaint-winrate) <br>
- [complaint-category-taxonomy.md](references/complaint-category-taxonomy.md) <br>
- [winrate-methodology.md](references/winrate-methodology.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown analysis with tables, calculated rates, case anchors, legal-reference notes, and evidence-collection steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should include sample counts, confidence notes, Wilson 95% confidence intervals, evidence-strength layers, and disclaimers that case similarity is non-binding and win rate is not a legal guarantee.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
