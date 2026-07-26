## Description: <br>
Helps an agent analyze whether an extreme before-and-after result is likely regression to the mean or evidence of a real causal effect. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and analysts use this skill to evaluate interventions, pilots, performance swings, fund results, AI benchmark spikes, or other noisy extreme observations before assigning causal credit or blame. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat examples involving business, investment, AI benchmarks, or medical scenarios as professional advice or as standalone proof of causality. <br>
Mitigation: Use the skill as an analytical prompt; require domain review and separate evidence before making professional, investment, medical, or operational decisions. <br>
Risk: Before-and-after improvements can be over-credited to an intervention when no control group or baseline regression estimate is available. <br>
Mitigation: Compare against untreated peers, historical variance, or a baseline regression estimate before assigning causal credit or blame. <br>


## Reference(s): <br>
- [Primary Sources](references/sources.md) <br>
- [Galton 1886 and Kahneman 2011 Israeli Air Force Example](examples/galton-1886-kahneman-2011-israeli-air-force.md) <br>
- [AI Hot Streak Benchmark Spike Example](examples/ai-hot-streak-benchmark-spike-2023-2026.md) <br>
- [Chatbot Arena Leaderboard](https://lmarena.ai/) <br>
- [NLP Evaluation in Trouble](https://aclanthology.org/2023.findings-emnlp.722/) <br>
- [ClawHub Skill Page](https://clawhub.ai/deciqai/skills/regression-to-the-mean) <br>
- [Machine-Readable Skill Metadata](https://www.deciqai.com/s/regression-to-the-mean.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown regression analysis with structured fields for observation, intervention, retest, expected regression, control comparison, causal calibration, and adjusted action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask step-by-step coaching questions and stop for user input when the user is new to the framework.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
