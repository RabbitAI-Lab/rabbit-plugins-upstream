## Description: <br>
Performs mean-variance optimization on Traditional IRA strategies, eliminating weak ones and outputting optimized portfolio weights without forced exclusions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[plato-1](https://clawhub.ai/user/plato-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and finance-focused users use this skill to analyze local Composer Traditional IRA strategy data, score candidate strategies, and generate optimized allocation weights for review before taking any portfolio action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The allocation report is financial decision support based on local cached strategy data and rough synthetic assumptions. <br>
Mitigation: Review the generated recommendations, assumptions, and source data before making any trading or allocation decision. <br>
Risk: The release changelog and security guidance identify different output paths for the optimized JSON report. <br>
Mitigation: Confirm the actual generated file path in the artifact before wiring downstream automation to the report. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/plato-1/skills/composer-optimizer) <br>
- [Publisher profile](https://clawhub.ai/user/plato-1) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Python script output plus JSON allocation report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes dashboard/composer_trad_ira_optimized.json and prints an allocation summary.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
