## Description: <br>
Proactive health monitoring for AI agents with Apple Health integration, pattern detection, and anomaly alerts for agents caring for humans with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cgtreadw](https://clawhub.ai/user/cgtreadw) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use Health Guardian to import local Apple Health exports, summarize recent vitals, and flag threshold-based or baseline-based anomalies for caregivers or people managing chronic conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health telemetry and stores imported readings locally. <br>
Mitigation: Review before installing, protect or encrypt the data directory, and use it only where local health data handling is appropriate. <br>
Risk: The configured data source may read Apple Health exports from an iCloud-synced location. <br>
Mitigation: Verify the exact source path and sync behavior before enabling imports. <br>
Risk: External alert channels and scheduled hourly processing can disclose health information or continue running unexpectedly. <br>
Mitigation: Use external alerts only with explicit consent from the user and recipients, and enable cron scheduling only when the operator knows how to disable it. <br>


## Reference(s): <br>
- [Health Guardian on ClawHub](https://clawhub.ai/cgtreadw/skills/health-guardian) <br>
- [Health Auto Export](https://apps.apple.com/app/health-auto-export/id1115567069) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and terminal text with JSON configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include health summaries, anomaly alerts, configuration guidance, and commands for local import and analysis scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact/SKILL.md frontmatter, artifact/package.json, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
