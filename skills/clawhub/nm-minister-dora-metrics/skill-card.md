## Description: <br>
Computes DORA delivery-performance metrics from git and GitHub API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and release leads use this skill to compute DORA delivery-performance metrics from repository history and GitHub delivery data, classify each metric, and identify the weakest improvement dimension. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local repository history and GitHub delivery data for DORA analysis. <br>
Mitigation: Run it only in the intended repository and review GitHub token scopes before API use. <br>
Risk: Optional plugin and kuva charting installs add separate dependencies outside the skill artifact. <br>
Mitigation: Verify those dependencies independently before installing or using them. <br>
Risk: DORA results can be misleading when the production branch, release cadence, or failure labels are incorrect. <br>
Mitigation: Re-run reports over a narrower window and sample contributing GitHub issues to confirm labels and events. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-minister-dora-metrics) <br>
- [claude-night-market minister plugin](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>
- [DORA tier thresholds](modules/thresholds.md) <br>
- [Agentic workflow signals from DORA](modules/agentic-workflow-signals.md) <br>
- [kuva charting tool](https://github.com/Psy-Fer/kuva) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON report output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces per-metric values, tier classifications, an overall tier, and a bottleneck key.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
