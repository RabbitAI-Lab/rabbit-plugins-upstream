## Description: <br>
政府采购文件审查助手：审查政府采购招标文件、竞争性谈判/磋商文件、询价通知书、采购公告、合同草案等，逐条排查资格条件、评审因素、政策功能落实、公平竞争审查、"过紧日子"等合规风险，输出带法条依据的修改清单。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chesaram](https://clawhub.ai/user/chesaram) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement staff, agencies, and advisors use this skill to review Chinese government procurement files under the Government Procurement Law framework. It identifies compliance risks, cites knowledge-base legal sources, and drafts risk-ranked correction guidance for uploaded procurement documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat AI-generated procurement review as a formal legal opinion or administrative decision. <br>
Mitigation: Present the output as drafting and risk-screening support, include the skill disclaimer, and recommend professional legal or fiscal authority review for final decisions. <br>
Risk: Legal conclusions may be incomplete if the configured knowledge bases are unavailable, outdated, or missing a relevant rule. <br>
Mitigation: Require cited knowledge-base sources for legal conclusions and clearly disclose retrieval failures or missing coverage before giving advice. <br>
Risk: The skill can miss important context if users provide incomplete project details or incomplete procurement documents. <br>
Mitigation: Collect core project facts before review and list unresolved items in the report's pending-confirmation section. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chesaram/skills/gov-procurement-advisor) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown] <br>
**Output Format:** [Markdown risk review report with legal citations and modification checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses risk levels, source-backed legal citations, document locations, consequences, and suggested revisions.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact manifest/frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
