## Description: <br>
政采质疑答复辅助（采购人版·内部代号"政采盾牌"）帮助政府采购项目采购人或代理机构在收到供应商质疑后依法受理登记、判断质疑是否成立、生成纠正/驳回/切割答复，并预判投诉风险与二阶博弈。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Government procurement buyers, procurement agencies, and their reviewers use this skill to draft and review responses to supplier objections, including intake registration, issue-by-issue legal analysis, formal reply drafting, complaint-risk forecasting, and follow-up action planning. It is scoped to the buyer or agency defense side and excludes bidder-side objection drafting, bid scoring, contract review, and tender-document authoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated legal or procedural reply drafts may contain incorrect law references, incomplete facts, or unsuitable wording for a specific procurement matter. <br>
Mitigation: Require review by qualified legal, procurement, or agency staff before issuing any formal reply, and verify all cited laws, deadlines, project facts, and evidence against current authoritative sources. <br>
Risk: The internal complaint-risk forecast could be mistakenly sent to the supplier with the external reply. <br>
Mitigation: Separate the internal complaint-risk section from the formal reply package and confirm that only approved external text is delivered. <br>
Risk: A fixed author signature may be inappropriate for formal documents. <br>
Mitigation: Remove or explicitly approve the author signature before sending formal documents. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/gp-objection-reply-advisor) <br>
- [README.md](artifact/README.md) <br>
- [Regression summary report](artifact/回归测试总报告_5例.md) <br>
- [Regression test cases](artifact/回归测试用例_v1.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a formal objection reply draft, internal complaint-risk forecast, and follow-up action checklist; legal and procedural outputs require qualified human review before use.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter, manifest, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
