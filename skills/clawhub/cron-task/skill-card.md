## Description: <br>
Cron Task helps agents turn a debugged task into a recurring scheduled workflow with readiness checks, a standalone executor script, a schedule prompt, Feishu notification, and multi-destination archiving. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[edwardwason](https://clawhub.ai/user/edwardwason) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation teams use this skill to convert a debugged task or skill into a stable recurring workflow with readiness validation, generated execution code, scheduling instructions, archiving, and Feishu status notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated recurring automation may run commands, write executor scripts, send Feishu messages, or archive content to external destinations before the user has checked the details. <br>
Mitigation: Review the generated executor and schedule message, confirm timezone and archive paths, and approve destination-specific behavior before enabling the schedule. <br>
Risk: Feishu and IMA credentials or uploaded content may be exposed or over-permissioned if configured broadly. <br>
Mitigation: Use least-privilege Feishu and IMA credentials, avoid printing secret prefixes, and archive only content that is safe for the configured destinations. <br>


## Reference(s): <br>
- [Cron Task on ClawHub](https://clawhub.ai/edwardwason/skills/cron-task) <br>
- [Readiness Checklist](references/readiness-checklist.md) <br>
- [Schedule Prompt Template](references/schedule-prompt-template.md) <br>
- [Archiving Guide](references/archiving-guide.md) <br>
- [Executor Script Template](assets/executor_template.py) <br>
- [Archive Metadata Header Template](assets/metadata_header.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with generated Python code, shell commands, schedule instructions, configuration notes, and readiness tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create standalone executor scripts and schedule messages that depend on user-confirmed credentials, paths, timezone, and archive destinations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata, frontmatter, and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
