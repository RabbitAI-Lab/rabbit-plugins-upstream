## Description: <br>
Analyses finished A/B test results and produces a readout covering the outcome, statistical and practical significance, guardrails, segment cuts, experiment risks, and a ship/no-ship recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product managers, analysts, growth teams, and developers use this skill to interpret completed A/B experiments and turn control-versus-variant results into an evidence-based launch decision. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Incomplete experiment inputs can lead the agent to rely on assumptions about significance, sample size, peeking, or decision rules. <br>
Mitigation: Provide the hypothesis, primary metric, control and variant results, sample sizes, duration, guardrails, and any pre-registered decision rule; review all stated assumptions before acting. <br>
Risk: Experiment data may include sensitive product, revenue, retention, latency, complaint, or segment metrics. <br>
Mitigation: Share only the experiment data needed for the readout and remove unnecessary confidential or personal information. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/ab-test-readout) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/ab-test-readout.html) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, guidance, text] <br>
**Output Format:** [Markdown readout with a verdict, metrics table, significance assessment, segment analysis, risk review, and recommendation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask for missing hypothesis, metric, sample size, duration, guardrail, and decision-rule inputs before finalizing the readout.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
