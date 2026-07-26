## Description: <br>
Monitor and analyze Weights & Biases training runs for status, failures, loss curves, gradients, comparisons, and experiment health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrisvoncsefalvay](https://clawhub.ai/user/chrisvoncsefalvay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and ML engineers use this skill to inspect W&B training runs, detect stalled or failed jobs, characterize loss and gradient behavior, and compare experiments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the local W&B-authenticated environment to read and display training run data. <br>
Mitigation: Install only when that access is intended, and pass explicit entity, project, and run arguments to avoid querying unintended default targets. <br>
Risk: W&B configs, summaries, and metric histories may contain sensitive metadata that the skill can print. <br>
Mitigation: Avoid storing secrets in W&B configs or summaries, and review generated text or JSON before sharing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrisvoncsefalvay/skills/wandb-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text reports with optional JSON output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include W&B run status, metrics, configs, summaries, history, health alerts, and comparison results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
