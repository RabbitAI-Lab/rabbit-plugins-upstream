## Description: <br>
Health Guardian helps agents monitor Apple Health exports, detect health patterns, and flag anomalies for humans with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ctsolutionsdev](https://clawhub.ai/user/ctsolutionsdev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, caregivers, and agent developers use this skill to import local Apple Health export data, analyze recent vitals and activity patterns, and surface informational anomaly alerts. It is intended to support monitoring workflows, not to provide medical diagnosis or emergency response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive personal health data from Apple Health exports. <br>
Mitigation: Use it only with explicit consent from the person whose data is involved and restrict file access to the Health Auto Export folder and the skill data directory. <br>
Risk: The setup may involve iCloud-synced health export files and optional third-party alert channels. <br>
Mitigation: Confirm that iCloud sync and any alert channel are acceptable for the user's privacy needs before enabling automated imports or alerts. <br>
Risk: Health alerts may be incomplete, delayed, or clinically inaccurate. <br>
Mitigation: Treat alerts and summaries as informational monitoring signals, not medical advice, diagnosis, or emergency guidance. <br>


## Reference(s): <br>
- [Health Guardian on ClawHub](https://clawhub.ai/ctsolutionsdev/skills/proactive-health) <br>
- [Health Auto Export](https://apps.apple.com/app/health-auto-export/id1115567069) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown summaries, console alerts, JSON configuration, and local JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are informational and depend on local Apple Health export files, thresholds, and baseline settings.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
