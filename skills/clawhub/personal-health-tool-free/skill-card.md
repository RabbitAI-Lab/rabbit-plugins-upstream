## Description: <br>
个人健康管家免费版 helps personal users manage local health data, including exercise, sleep, diet, physical-exam report analysis, health suggestions, plans, and trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal users use this skill to record and review local health information, interpret common physical-exam indicators, and generate exercise, diet, reminder, and trend-analysis guidance. It is not a substitute for professional medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores personal health information locally under ~/.health, which can expose sensitive records if the user account or file permissions are weak. <br>
Mitigation: Install only when local storage is acceptable, review file permissions, avoid entering data that should not persist, and consider encryption or a private user account for real medical or fitness records. <br>
Risk: Health suggestions and physical-exam interpretations can be incomplete or misleading if treated as medical diagnosis. <br>
Mitigation: Use the output as general wellness guidance and consult a qualified medical professional for abnormal indicators, symptoms, diagnosis, or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/personal-health-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON, YAML, Python, and shell-command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create, query, export, or format local health records under ~/.health.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
