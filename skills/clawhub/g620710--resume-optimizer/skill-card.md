## Description: <br>
Resume Optimizer helps users analyze and improve Chinese resumes for target roles using a paid remote AI service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External job seekers, career changers, students, and resume-service providers use this skill to score, diagnose, rewrite, and tailor Chinese plain-text resumes for target roles or job descriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Resume content and the user key may be sent to the publisher's remote service, including a hard-coded plain-HTTP default endpoint. <br>
Mitigation: Install only if comfortable with that data transfer; redact personal, contact, and confidential employer information, and avoid the default endpoint until HTTPS transport, privacy terms, retention, and backend details are documented. <br>
Risk: The security guidance says the shipped script may need fixes before it runs. <br>
Mitigation: Review and test the script in a controlled environment before using it with real resume data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/resume-optimizer) <br>
- [Publisher profile](https://clawhub.ai/user/g620710) <br>
- [DeepSeek API base URL](https://api.deepseek.com/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Command-line output containing resume scores, diagnostics, sentence rewrites, revised resume text, and role-match suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and RESUME_API_USER_KEY; sends resume content to a remote service.] <br>

## Skill Version(s): <br>
1.1.3 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
