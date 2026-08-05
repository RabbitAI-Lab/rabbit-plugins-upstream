## Description: <br>
Verify OpenClaw after upgrades against an operator-maintained model, cron, and channel ground truth. Use for report-only config integrity, provider liveness, cron integrity, session smoke tests, and channel checks; require explicit approval before applying repairs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jonathanjing](https://clawhub.ai/user/jonathanjing) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
OpenClaw operators use this skill after upgrades or suspected drift to compare runtime configuration, recurring cron jobs, model routing, session behavior, and channel liveness against their maintained ground truth. It produces a redacted verification report and only proposes bounded config or cron repairs after explicit operator approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read OpenClaw runtime configuration and cron state, send channel test messages, and write a local verification report. <br>
Mitigation: Run it only in workspaces where that verification scope is acceptable, and rely on the documented redaction behavior to avoid logging secrets. <br>
Risk: Approved config or cron repairs could change OpenClaw behavior if the maintained ground truth is stale or incorrect. <br>
Mitigation: Review the exact non-secret repair plan immediately before approval and approve changes only when they match the maintained ground truth. <br>


## Reference(s): <br>
- [ground-control ClawHub page](https://clawhub.ai/jonathanjing/ground-control) <br>
- [ground-control Skill page](https://clawhub.ai/jonathanjing/skills/ground-control) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions, redacted verification reports, and operator approval prompts with inline commands or configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report-only by default; approved repairs are limited to non-secret config fields and cron job attributes.] <br>

## Skill Version(s): <br>
0.3.6 (source: server release evidence, frontmatter metadata, and changelog released 2026-08-03) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
