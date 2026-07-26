## Description: <br>
Proactive health monitoring for AI agents. Apple Health integration, pattern detection, anomaly alerts. Built for agents caring for humans with chronic conditions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ctsolutionsdev](https://clawhub.ai/user/ctsolutionsdev) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and caregivers use this skill to configure an agent to import Apple Health exports, analyze recent health trends, and surface anomaly alerts for humans with chronic conditions or disabilities. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles highly sensitive health data and the security evidence notes weak scoping and misleading privacy wording. <br>
Mitigation: Install only with explicit consent from the person whose health data is involved, restrict local file access, and protect or periodically delete generated data files. <br>
Risk: Scheduled imports and external alert channels can expose health information or send alerts to unintended recipients. <br>
Mitigation: Verify the real import directory before enabling automation, and use Telegram or other external notifications only after confirming message contents and recipients. <br>
Risk: Health anomaly output may be mistaken for medical safety guidance, and the security evidence flags an importer/analyzer storage mismatch. <br>
Mitigation: Treat alerts as review prompts rather than medical advice, and resolve the storage mismatch before relying on the skill for ongoing monitoring. <br>


## Reference(s): <br>
- [Health Auto Export App](https://apps.apple.com/app/health-auto-export/id1115567069) <br>
- [Health Guardian on ClawHub](https://clawhub.ai/ctsolutionsdev/skills/egvert-health-guardian) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown summaries, terminal alert text, JSON configuration, and local JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Handles sensitive local health data and may be paired with scheduled imports or notification channels.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter, package.json, and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
