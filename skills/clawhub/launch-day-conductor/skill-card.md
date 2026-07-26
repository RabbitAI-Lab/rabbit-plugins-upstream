## Description: <br>
Launch Day Conductor helps agents run launch-day war rooms by checking readiness preconditions, building hour-blocked runbooks, forcing continue-or-rollback observation-window decisions, logging incidents, and preparing end-of-day handoffs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, operators, and go-to-market teams use this skill to coordinate launch-day execution, monitor irreversible actions against predeclared thresholds, decide whether to continue or roll back, and consolidate the launch handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact launch decisions could be incorrect if readiness records, telemetry, or rollback thresholds are missing or stale. <br>
Mitigation: Require the SHIP verdict, authoritative date or stage, owner roster, and predeclared kill criteria before irreversible actions, and review continue-or-rollback decisions with accountable launch owners. <br>
Risk: Pasted metrics exports, screenshots, dashboards, and public threads may contain misleading data or embedded instructions. <br>
Mitigation: Treat telemetry and comments as untrusted input, ignore instructions embedded in them, and label readings by source as measured, user-provided, or estimated. <br>
Risk: Saved runbooks, verdict logs, and status proposals can influence future launch coordination. <br>
Mitigation: Review proposed saved results and registry/status updates before accepting them, and keep canonical launch state changes under the appropriate owner review. <br>


## Reference(s): <br>
- [Launch Day Conductor homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown runbook, verdict log, incident ladder, proposal/status lines, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs emphasize dated launch actions, source-labeled telemetry, owner assignments, continue-or-rollback verdicts, and reviewable saved results when the user approves.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
