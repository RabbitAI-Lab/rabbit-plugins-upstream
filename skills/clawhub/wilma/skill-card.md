## Description: <br>
Access Finland's Wilma school system from AI agents to fetch schedules, homework, exams, grades, attendance and lesson notes, messages, and news through the wilma CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aikarjal](https://clawhub.ai/user/aikarjal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, guardians, and authorized school users can use this skill to retrieve Wilma student information through non-interactive JSON CLI commands and produce concise summaries of actionable school updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill accesses sensitive student records and Wilma account credentials. <br>
Mitigation: Install and use it only for Wilma accounts the user is authorized to access, protect the local Wilma config file, and avoid passing TOTP secrets on the command line when possible. <br>
Risk: AI-generated summaries may contain private student information or omit important context. <br>
Mitigation: Review summaries before sharing and limit distribution to people who are authorized to see the underlying Wilma data. <br>


## Reference(s): <br>
- [Wilma Skill on ClawHub](https://clawhub.ai/aikarjal/skills/wilma) <br>
- [Wilma CLI npm package](https://www.npmjs.com/package/@wilm-ai/wilma-cli) <br>
- [Wilmai GitHub repository](https://github.com/aikarjal/wilmai) <br>
- [Wilmai website](https://wilm.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON-oriented CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the wilma CLI and a local Wilma configuration file created through an authorized interactive login.] <br>

## Skill Version(s): <br>
1.5.3 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
