## Description: <br>
Birthday Reminder helps agents add, query, list, and remind users about birthdays from natural-language requests while calculating ages and upcoming dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[manantra](https://clawhub.ai/user/manantra) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and personal-productivity agents use this skill to remember birthdays, answer birthday and age questions, list upcoming birthdays, and produce reminder messages before important dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Birthday records can contain personal names and dates stored locally on disk. <br>
Mitigation: Store only birthday data appropriate for this machine and remove entries when they are no longer needed. <br>
Risk: The documentation mentions birthdays.md, while the security evidence identifies /home/clawd/clawd/data/birthdays.json as the actual storage file. <br>
Mitigation: Treat /home/clawd/clawd/data/birthdays.json as authoritative when reviewing, backing up, or deleting stored birthday data. <br>


## Reference(s): <br>
- [Birthday Reminder ClawHub page](https://clawhub.ai/manantra/skills/birthday-reminder) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown-like text and command-line output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes birthday dates, days remaining, and age calculations when birth years are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
