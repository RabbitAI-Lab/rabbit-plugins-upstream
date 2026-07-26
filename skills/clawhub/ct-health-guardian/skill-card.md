## Description: <br>
Proactive health monitoring for AI agents. Apple Health integration, pattern detection, anomaly alerts. Built for agents caring for humans with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ctsolutionsdev](https://clawhub.ai/user/ctsolutionsdev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and caregiver agents use this skill to import Apple Health export data, detect patterns in vitals and sleep, and surface anomaly alerts for people with chronic conditions or disabilities. It is a monitoring aid and should not be treated as a medical alert system. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health data through local files, iCloud-synced export paths, and optional external alert channels. <br>
Mitigation: Use only with explicit consent from the monitored person, restrict access to the local data directory, and protect any configured alert channel. <br>
Risk: Health alerts and pattern detection can be incomplete, stale, or inaccurate. <br>
Mitigation: Treat the skill as an experimental monitoring helper, test import and analysis paths before relying on alerts, and do not use it as an emergency or medical alert system. <br>
Risk: Recurring monitoring can repeatedly process personal data and notify others based on configured thresholds. <br>
Mitigation: Review thresholds, baseline settings, cron behavior, and notification recipients before enabling scheduled operation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ctsolutionsdev/skills/ct-health-guardian) <br>
- [Health Auto Export app](https://apps.apple.com/app/health-auto-export/id1115567069) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries and alerts, JSON configuration, and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Imports health export data into local JSON files and prints alert-oriented summaries from configured thresholds and baselines.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, and ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
