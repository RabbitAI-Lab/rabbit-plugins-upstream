## Description:

成果转化方案生成。当用户提到"技术怎么交易""许可还是转让还是入股""成果转化方案""作价入股怎么操作""技术转让方案""怎么给成果定价"或需要参考科技成果转化案例、借鉴高校院所转化模式时使用。运行时会自动检索内置41个典型案例库（北京31例+全国10例）作为参考依据，输出：转化模式决策（许可/转让/作价入股）、10维度评分、条款清单、税收影响、相似案例对标。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvjin1983](https://clawhub.ai/user/lvjin1983)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to draft technology transfer plans for university, research institute, hospital, enterprise, or individual technology assets. It helps compare licensing, assignment, and equity contribution paths, then produces a case-backed recommendation with scoring, term checklists, tax notes, and next steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Technology transfer, tax, valuation, and deal-structure recommendations may be incomplete or unsuitable for a real transaction.

Mitigation: Use the output as planning assistance and verify legal, tax, valuation, and policy details with qualified professionals before relying on it.

Risk: Case-backed comparisons may not reflect the user's current jurisdiction, institutional policy, or deal-specific constraints.

Mitigation: Confirm applicable policies, current regulations, ownership status, and transaction facts before negotiating or signing terms.

## Reference(s):

- [case_library_guide.md](references/case_library_guide.md)
- [case_library.json](references/case_library.json)
- [case_index.json](references/case_index.json)
- [ClawHub skill page](https://clawhub.ai/lvjin1983/skills/lzy-tech-transfer-plan-generator)

## Skill Output:

**Output Type(s):** [markdown, guidance, shell commands]

**Output Format:** [Markdown plan with decision tables, case comparisons, checklist-style terms, tax notes, and action steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local 41-case reference library and prompts for missing transaction context before producing the plan.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
