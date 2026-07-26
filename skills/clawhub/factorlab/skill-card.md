## Description: <br>
FactorLab analyzes A-share stocks with a three-factor quantitative model and returns factor scores, buy labels, supporting reasons, and risk notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hunkguo](https://clawhub.ai/user/hunkguo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to run single-stock or batch A-share factor analysis and summarize the resulting scores, buy labels, and caveats in natural language. It is intended as a quantitative research helper, not as personalized financial advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Buy labels could be mistaken for personalized financial advice. <br>
Mitigation: Present outputs as quantitative research signals, include the skill's risk caveats, and require users to make independent investment decisions. <br>
Risk: Results may use simulated data or insufficient market history. <br>
Mitigation: Check the output data-source label and data-point count before relying on a score; treat simulated or short-history results as test or low-confidence outputs. <br>
Risk: Live mode may contact external TDX market-data servers with requested stock codes. <br>
Mitigation: Use simulated mode when external market-data access is not acceptable, or disclose live data access before running live analysis. <br>


## Reference(s): <br>
- [FactorLab factor theory reference](references/factor_theory.md) <br>
- [FactorLab ClawHub page](https://clawhub.ai/hunkguo/skills/factorlab) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown reports by default, with optional JSON output from the analysis script.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include factor scores, recommendations, confidence, supporting reasons, risk notes, and a live-versus-simulated data source label.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
