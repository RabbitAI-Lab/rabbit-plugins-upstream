## Description: <br>
国企非招标采购领域的合规辅助AI，基于用户上传的企业采购制度与招投标法规体系，辅助判定询比、竞价、谈判、直接采购的适用条件，并识别依法必须招标边界与方式选择风险。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
State-owned enterprise procurement staff, legal and compliance teams, supervisory personnel, and procurement managers use this skill to check whether a non-tender procurement method is appropriate, identify mandatory tendering boundaries, and generate internal reference analysis. It is an advisory aid and does not replace enterprise procurement decisions, legal review, or approval authority. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat advisory procurement analysis as legal advice or final procurement approval. <br>
Mitigation: Require human review by the enterprise procurement decision body, legal/compliance reviewers, and the applicable approval process before acting on outputs. <br>
Risk: Prompts or uploaded documents may contain state secrets, core commercial secrets, personal sensitive information, or identifiable supplier details. <br>
Mitigation: Use only authorized and desensitized inputs, and avoid uploading sensitive or identifiable procurement information unless proper controls are in place. <br>
Risk: Procurement rules, local state-owned asset requirements, and legal references may change or may not match a user's enterprise制度. <br>
Mitigation: Verify current laws, local rules, and the user's own enterprise procurement制度 before relying on a recommended procurement path. <br>
Risk: Direct procurement or non-tender methods can be misapplied if required facts, market research, or approval records are incomplete. <br>
Mitigation: Collect the required project facts, validate every stated condition, retain written justification and approvals, and escalate high-risk cases for compliance review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/nontender-skill-1-0-0) <br>
- [非招标采购法规索引](references/法规索引.md) <br>
- [四种非招标采购方式对照表](references/四种采购方式对照表.md) <br>
- [直接采购七类情形详解](references/直接采购七类情形详解.md) <br>
- [场景路由映射表](references/场景路由映射表.md) <br>
- [非招标采购负面案例库](references/负面案例库.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown compliance analysis with tables, risk levels, cited bases, and decision-record templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces advisory procurement-method analysis only; does not produce executable code or final procurement approvals.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, manifest.yaml, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
