## Description: <br>
Helps agents turn uncertain forecasts into calibrated probability estimates grounded in base rates, evidence updates, confidence intervals, next evidence, and later scoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and agents use this skill to reason about uncertain outcomes such as forecasts, diagnoses, sales conversions, hiring decisions, deal closes, geopolitical events, and AI timelines. It guides the agent to state a precise question, anchor in a base rate, update with evidence, report uncertainty, identify next evidence, and keep a calibration log. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat probability estimates as factual guarantees. <br>
Mitigation: Present estimates with base rates, evidence, confidence intervals, and caveats, and review important decisions with domain experts. <br>
Risk: Calibration logs may contain sensitive business or personal forecasts. <br>
Mitigation: Store calibration logs only in approved locations and avoid including unnecessary sensitive details. <br>
Risk: Weak or missing base rates can create false precision. <br>
Mitigation: Use ranges and a Knightian uncertainty caveat when no usable reference class exists. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/probabilistic-thinking) <br>
- [Primary sources](references/sources.md) <br>
- [Tetlock, IARPA, and the Good Judgment Project example](examples/tetlock-iarpa-good-judgment-project-2011-2015.md) <br>
- [Forecasting AI timelines and agentic reliability example](examples/forecasting-ai-timelines-agentic-reliability-2023-2026.md) <br>
- [Bayes, An Essay towards solving a Problem in the Doctrine of Chances](https://royalsocietypublishing.org/doi/10.1098/rstl.1763.0053) <br>
- [Knight, Risk, Uncertainty, and Profit](https://www.econlib.org/library/Knight/knRUP.html) <br>
- [Mellers et al., Psychological Strategies for Winning a Geopolitical Forecasting Tournament](https://journals.sagepub.com/doi/10.1177/0956797614524255) <br>
- [IARPA Aggregative Contingent Estimation program](https://www.iarpa.gov/research-programs/ace) <br>
- [AI Impacts](https://aiimpacts.org/) <br>
- [Metaculus forecasting questions](https://www.metaculus.com/questions/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a structured probability estimate with question, base rate, evidence, Bayesian shift, point estimate, confidence interval, next evidence, and calibration log.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
