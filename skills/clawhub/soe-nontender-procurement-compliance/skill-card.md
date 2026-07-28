## Description: <br>
国企非招标采购领域的合规辅助 AI，帮助用户判断询比、竞价、谈判、直接采购的适用条件，并识别依法必须招标边界与方式选择风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, legal, compliance, and audit staff at state-owned enterprises use this skill to structure non-tender procurement method analysis, surface required bid thresholds, and produce internal reference guidance for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill provides compliance reference support, not legal advice or procurement approval. <br>
Mitigation: Require enterprise procurement, legal, or compliance reviewers to verify conclusions against enterprise policy and current law before acting. <br>
Risk: Procurement scenarios can contain state secrets, commercial secrets, personal information, supplier details, or pricing data. <br>
Mitigation: Use redacted inputs and follow organizational data-handling rules; do not submit restricted information unless that use is approved. <br>
Risk: Regulatory references and local state-owned enterprise procurement rules can change. <br>
Mitigation: Validate cited laws, local rules, and enterprise procedures before relying on the output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/soe-nontender-procurement-compliance) <br>
- [法规索引](artifact/references/法规索引.md) <br>
- [四种采购方式对照表](artifact/references/四种采购方式对照表.md) <br>
- [直接采购七类情形详解](artifact/references/直接采购七类情形详解.md) <br>
- [负面案例库](artifact/references/负面案例库.md) <br>
- [场景路由映射表](artifact/references/场景路由映射表.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured tables, checklists, risk labels, and cited procurement-law references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are internal reference analyses and require user-provided enterprise policy and human review before procurement action.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and manifest.yaml) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
