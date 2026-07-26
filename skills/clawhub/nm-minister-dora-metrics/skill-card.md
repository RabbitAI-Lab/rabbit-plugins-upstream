## Description: <br>
Computes DORA delivery-performance metrics from git and the GitHub API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and release reviewers use this skill to compute deployment frequency, lead time, change failure rate, and time to restore service for a repository and identify the weakest delivery-performance dimension. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local git and GitHub data for the repository where it is invoked. <br>
Mitigation: Confirm the intended repository path, production branch, and GitHub project before running the workflow. <br>
Risk: Optional charting tool installation and trend-data persistence may affect the local environment or create retained metric snapshots. <br>
Mitigation: Approve optional charting installation and any trend-data persistence explicitly before use. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-minister-dora-metrics) <br>
- [Publisher Profile](https://clawhub.ai/user/athola) <br>
- [Project Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/minister) <br>
- [Agentic Workflow Signals from DORA](modules/agentic-workflow-signals.md) <br>
- [DORA Tier Thresholds](modules/thresholds.md) <br>
- [kuva](https://github.com/Psy-Fer/kuva) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON report with optional shell commands for metric collection and charting] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports per-metric numeric values, tier classifications, an overall tier, and a bottleneck key.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
