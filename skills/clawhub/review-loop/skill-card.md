## Description: <br>
Runs a bounded subagent review loop that verifies findings, applies accepted fixes, reruns relevant tests, and reports residual risk when explicitly invoked. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wufei-png](https://clawhub.ai/user/wufei-png) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill to run an iterative review-and-remediation loop that asks fresh review agents for important findings, accepts or rejects them, applies accepted fixes, reruns tests, and summarizes decisions and remaining risks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is labeled as read-only, but accepted findings can lead to code edits, test runs, subagent delegation, and commits. <br>
Mitigation: Invoke only when code changes and test execution are acceptable, and review accepted findings plus resulting diffs before relying on or publishing changes. <br>


## Reference(s): <br>
- [Review Loop on ClawHub](https://clawhub.ai/wufei-png/skills/review-loop) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown summary with file and line findings, acceptance decisions, fixes, verification results, and residual risks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Bounded by max_rounds; defaults to 3 rounds when no positive integer is provided.] <br>

## Skill Version(s): <br>
0.1.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
