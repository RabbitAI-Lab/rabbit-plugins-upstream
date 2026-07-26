## Description: <br>
Litigation Hub helps legal practitioners process court SMS messages, court service links, and document photos into extracted case information, downloaded or OCRed court documents, organized case files, deadline checks, and calendar, email, or local reminders. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leahlu0124-creator](https://clawhub.ai/user/leahlu0124-creator) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External legal practitioners and legal operations teams use this skill to parse court delivery messages, service links, and scanned or photographed court documents, then archive materials into case folders and create litigation deadline reminders. It is intended for sensitive litigation workflows where users supervise downloads, folder writes, calendar entries, scheduled tasks, and reminder emails. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has broad local, network, email, installation, and persistent reminder authority in a sensitive litigation workflow. <br>
Mitigation: Use it only on a trusted machine, review it before installing, and require explicit confirmation before installs, browser automation, folder writes, reminder creation, or email transmission. <br>
Risk: It may install global npm tools and use browser automation or command-line downloads to retrieve court documents. <br>
Mitigation: Prefer preinstalling and pinning dependencies yourself, and confirm each browser automation or download step before execution. <br>
Risk: It may write case files and raw OCR or SMS data locally. <br>
Mitigation: Configure a secure case folder, verify target paths before existing-folder writes, and avoid running it on shared or untrusted systems. <br>
Risk: It may create calendar entries, OS scheduled tasks, desktop reminder files, and case reminder emails. <br>
Mitigation: Confirm reminder creation and email recipients before scheduling or sending, and periodically review configured OS tasks and reminder files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leahlu0124-creator/skills/litigation-hub) <br>
- [Project homepage from clawdis metadata](https://github.com/leahlu0124-creator/litigation-hub) <br>
- [Attribution and upstream reference notes](references/ATTRIBUTION.md) <br>
- [Archive format](references/archive-format.md) <br>
- [Report format](references/report-format.md) <br>
- [SMS patterns and platform rules](references/sms-patterns.json) <br>
- [Deadline rules](references/deadline-rules.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, structured text summaries, JSON configuration and archive records, and generated local files such as reminders or calendar fallbacks.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or run local scripts that download court documents, OCR uploaded images, write case files, create calendar entries, schedule OS reminders, and send configured email reminders.] <br>

## Skill Version(s): <br>
2.2.3 (source: server release, SKILL.md frontmatter, CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
