## Description: <br>
Elderly AI Assistant helps Chinese senior users with accessible health reminders, medication prompts, companionship, daily briefings, memory support, and family contact workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to provide Chinese-language, elder-friendly assistance for seniors, including short responses and large-font HTML pages for health reminders, medication schedules, companionship, daily briefings, memory reminders, and family contact guidance. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat health or medication output as professional medical advice. <br>
Mitigation: Present health and medication content as reminders or general guidance, include doctor-consultation language, and avoid diagnosis or medication changes. <br>
Risk: Users may share medical secrets, identity numbers, bank details, passwords, or other sensitive personal information. <br>
Mitigation: Warn users not to disclose sensitive information and avoid requesting identifiers, bank details, passwords, or unnecessary medical secrets. <br>
Risk: The skill uses broad local agent tools, including Bash and file-editing permissions. <br>
Mitigation: Install and run only in environments where those permissions are acceptable, and review generated files or commands before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/elderly-assistant) <br>
- [Research report](references/research_report.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Chinese text responses, Markdown guidance, and large-font HTML files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are intended to be concise and elder-friendly; complex health, medication, and daily-briefing information may be rendered as accessible HTML.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
