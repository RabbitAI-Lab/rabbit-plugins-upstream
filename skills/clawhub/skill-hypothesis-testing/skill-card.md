## Description: <br>
统计假设检验工具；支持正态性检验(Shapiro-Wilk/K-S)、t检验(单样本/独立/配对)、卡方检验(拟合优度/独立性)、ANOVA、Levene检验、Mann-Whitney U检验；自动计算统计量、p值、置信区间与效应量；提供结果解释指南 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[duding-engicool](https://clawhub.ai/user/duding-engicool) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students, analysts, researchers, and developers use this skill to run common statistical hypothesis tests on numeric or tabular data and interpret p-values, confidence intervals, and effect sizes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper reads local file paths supplied by the user and can write an output file. <br>
Mitigation: Provide only intended data files and output locations, and review generated JSON before relying on it. <br>
Risk: Statistical conclusions can be misleading when test assumptions, sample size effects, or effect sizes are ignored. <br>
Mitigation: Check the documented assumptions for the selected test and interpret p-values alongside confidence intervals, effect sizes, and the reference guide. <br>


## Reference(s): <br>
- [Hypothesis Test Interpretation Guide](references/interpretation_guide.md) <br>
- [Server-resolved source repository](https://github.com/duding-engicool/skill-hypothesis-testing) <br>
- [ClawHub skill page](https://clawhub.ai/duding-engicool/skills/skill-hypothesis-testing) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; the helper script emits JSON results to stdout or an output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads comma-separated values or local CSV/TXT/Excel paths and can write JSON results when an output path is provided.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
