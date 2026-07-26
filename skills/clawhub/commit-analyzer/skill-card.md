## Description: <br>
Commit Analyzer analyzes local Git commit frequency, categories, and timing to assess autonomous operation health and identify idle or high-activity periods. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bobrenze-bot](https://clawhub.ai/user/bobrenze-bot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and AI agent operators use this skill to run local Git-history reports that assess commit cadence, category mix, hourly activity, and idle gaps for operational health monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Git history may contain sensitive commit messages or activity patterns that should not be broadly shared. <br>
Mitigation: Run the skill only in repositories whose commit history is acceptable to analyze, and review generated reports before storing or sharing them. <br>
Risk: Heartbeat integration can place commit-health summaries into local agent memory. <br>
Mitigation: Enable the integration only where that storage is acceptable, and avoid retaining sensitive commit details in memory files. <br>
Risk: Commit-rate thresholds are diagnostic heuristics and may misclassify normal development pauses as operational issues. <br>
Mitigation: Treat reports as advisory signals and compare them with task context, blockers, and expected work patterns before acting. <br>


## Reference(s): <br>
- [Commit Analyzer on ClawHub](https://clawhub.ai/bobrenze-bot/skills/commit-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text terminal reports or JSON objects from analyzer.sh.] <br>
**Output Parameters:** [1D: command plus optional days, hours, and --json flag.] <br>
**Other Properties Related to Output:** [Runs read-only Git log analysis in the local repository; requires git and bc for calculated metrics.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
