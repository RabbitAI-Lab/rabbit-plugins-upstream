## Description: <br>
Find crypto/web3 teams with $10M+ funding and verified Telegram contacts for lead research, contact-list building, funded-startup research, and web3 prospecting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shwchlorine](https://clawhub.ai/user/shwchlorine) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, operators, and business-development teams use this skill to coordinate web3 lead research, identify funded crypto teams, verify public Telegram contacts, and maintain CSV contact records. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can set up persistent background hunter automation. <br>
Mitigation: Remove or avoid the cron and auto-respawn setup unless continuous operation is explicitly approved. <br>
Risk: The skill collects and stores personal Telegram handles. <br>
Mitigation: Limit collection to public business contacts, define deletion rules, and review entries before retaining or using them. <br>
Risk: The skill can write CSV contact records during research. <br>
Mitigation: Require explicit confirmation before writing CSV files and set clear run limits. <br>


## Reference(s): <br>
- [Hunter Subagent Task Template](artifact/references/hunter-task.md) <br>
- [Crypto Contact Research Workflow](artifact/references/workflow.md) <br>
- [Auto-Hunt Setup](artifact/references/auto-hunt-setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/shwchlorine/skills/web3-target-team-research) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown instructions with inline shell commands and CSV schemas] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose CSV entries for researched teams and Telegram contacts.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
