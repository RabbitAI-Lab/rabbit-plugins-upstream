## Description: <br>
Analyse a finished A/B test and write an honest results readout with real statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, analysts, and experiment owners use this skill to evaluate completed A/B tests from supplied metric data, guardrails, and test setup details. It helps turn experiment results into an explicit ship, no-ship, iterate, or re-run recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The referenced significance helper script is not included in the inspected package, so computed statistics may depend on the agent's own calculation or separately supplied tooling. <br>
Mitigation: Require the agent to show the input counts, formulas or calculation method, p-value, confidence interval, and lift before using the recommendation. <br>
Risk: Experiment recommendations can be misleading when inputs omit guardrails, minimum meaningful effect, planned sample size, or whether the test stopped early. <br>
Mitigation: Provide the metric data, hypothesis, practical significance threshold, guardrail metrics, and test plan context before asking for a ship or no-ship decision. <br>


## Reference(s): <br>
- [Experiment Readout Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/experiment-readout.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/mohitagw15856/skills/experiment-readout) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown readout with tables, computed statistics, validity checks, and a recommendation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include helper-command examples for significance calculations when suitable.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
