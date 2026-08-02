## Description: <br>
Diagnoses and repairs personal productivity failures such as overwhelm, procrastination, scattered priorities, collapsed habits, broken reviews, and overload by guiding an agent through capacity math, prioritization, planning, and local memory maintenance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and employees use this skill when they want an agent to diagnose productivity bottlenecks, plan work against realistic capacity, and maintain a persistent local productivity memory. It is intended for personal productivity coaching and local note maintenance, not calendar API automation or live task-list operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to write durable local productivity, work, contact, and health-related notes automatically. <br>
Mitigation: Install it only when persistent local productivity memory is desired, and review or back up ~/Clawic/data/ before use. <br>
Risk: Stored notes may include sensitive personal behavior patterns, health facts, medication timing, client details, or commitments. <br>
Mitigation: Avoid saving unnecessary sensitive details and inspect the local notes periodically, especially shared project, contact, and health files. <br>
Risk: The scanner notes no evidence of network exfiltration or credential storage, but local records can still expose private information on the machine. <br>
Mitigation: Keep the local data directory access-controlled and do not place credentials in saved notes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/productivity) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic productivity skill page](https://clawic.com/skills/productivity) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Text, Configuration] <br>
**Output Format:** [Markdown guidance and local plain-text note updates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write durable local notes under configured ~/Clawic/data paths when a session produces commitments, plans, reviews, or related artifacts.] <br>

## Skill Version(s): <br>
1.0.6 (source: frontmatter, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
