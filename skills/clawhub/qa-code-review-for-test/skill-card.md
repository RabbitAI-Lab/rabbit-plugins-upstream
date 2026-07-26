## Description: <br>
Provides Chinese-language QA review guidance for code changes, focusing on change impact, high-risk patterns, test gaps, and the minimum regression test scope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and test leads use this skill after pull requests or code changes to identify affected areas, likely defect zones, missing tests, and focused regression coverage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad code review prompts and can read workspace code while assessing test impact. <br>
Mitigation: Use it only in repositories where QA review access to code changes is appropriate. <br>
Risk: Review findings may be incomplete or misleading if dependency impact is missed. <br>
Mitigation: Confirm the change scope and regression risk with the development team, and supplement with boundary analysis when dependency coverage is uncertain. <br>
Risk: Users may treat the review report as direct implementation guidance. <br>
Mitigation: Use the report to plan testing and review coverage; do not modify source code solely from the report without developer confirmation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-code-review-for-test) <br>
- [Publisher profile](https://clawhub.ai/user/kokxi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report with structured review findings, test gaps, impact analysis, high-risk patterns, and regression scope recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses traceability identifiers for each code review and links findings to a change or requirement identifier when available.] <br>

## Skill Version(s): <br>
1.6.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
