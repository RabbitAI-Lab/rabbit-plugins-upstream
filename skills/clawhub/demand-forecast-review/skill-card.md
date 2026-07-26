## Description: <br>
Interrogate a demand forecast before the business commits supply and inventory to it, producing a credibility review with baseline/uplift decomposition, MAPE and bias history, anomaly flags, an assumption register, and consensus-vs-statistical divergence analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Supply planners, demand planners, and business operators use this skill to challenge a demand plan before purchase orders, capacity, or inventory commitments are made. It helps separate statistical baseline from uplift, check historical accuracy and bias, flag unsupported ramps, and identify which forecast number supply should plan to. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The review may require sensitive demand, sales, inventory, and forecast-accuracy data. <br>
Mitigation: Use only business data appropriate for the agent environment and redact confidential details when they are not needed for the forecast review. <br>
Risk: A forecast without accuracy history can be mistaken for a validated planning signal. <br>
Mitigation: State when accuracy history is unavailable and treat the forecast as unvalidated until history or prior forecast-vs-actual data is provided. <br>


## Reference(s): <br>
- [Demand Forecast Review on ClawHub](https://clawhub.ai/mohitagw15856/skills/demand-forecast-review) <br>
- [Demand Forecast Review homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/demand-forecast-review.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown forecast credibility review with tables and decision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a verdict, baseline/uplift decomposition, MAPE and bias history, anomaly flags, assumption register, divergence analysis, and questions for the demand owner.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
