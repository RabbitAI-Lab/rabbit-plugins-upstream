## Description: <br>
Calculates true annual percentage rates for common loan products by parsing Chinese natural-language loan descriptions, running bundled Python IRR/APR calculations, and producing single-loan or multi-option comparison reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[riyuexingchen1234](https://clawhub.ai/user/riyuexingchen1234) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze Chinese loan offers, expose packaged fee terminology, calculate true APR with IRR, compare multiple loan options, and generate repayment and risk summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided loan text could be mishandled if an agent interpolates it directly into a shell or python3 -c command. <br>
Mitigation: Pass loan text as data to a fixed local script entrypoint or apply strict quoting; do not paste arbitrary user text into executable command strings. <br>
Risk: Loan APR calculations and comparisons may be mistaken for individualized financial advice. <br>
Mitigation: Present outputs as calculation support, preserve the skill's disclaimer, and encourage users to verify contract terms or consult a qualified professional before borrowing. <br>
Risk: Manual model calculations could produce inaccurate IRR/APR values. <br>
Mitigation: Run the bundled Python calculator/report workflow and report script-generated numbers instead of estimating or recalculating them by hand. <br>


## Reference(s): <br>
- [Loan Types Reference](references/loan-types.md) <br>
- [Common Loan Tricks Reference](references/common-tricks.md) <br>
- [Calculation Formulas Reference](references/formulas.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown-style loan analysis report generated from local Python script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports can include true APR, stated-rate comparison, total repayment cost, risk warnings, repayment schedules, and sorted multi-option comparisons.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence; artifact SKILL.md frontmatter reports 1.2.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
