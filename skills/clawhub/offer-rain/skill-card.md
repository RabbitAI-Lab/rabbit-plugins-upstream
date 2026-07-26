## Description: <br>
当用户想要以邮箱方式投递简历时，使用这个 Skill 为用户发送邮件至招聘方邮箱。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[eric-zhou-0302](https://clawhub.ai/user/eric-zhou-0302) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to prepare and send resume application emails to recruiters from job posting requirements. It helps collect sender credentials, recipient details, subject, body, resume path, and attachment naming before sending through the bundled SMTP script. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and duplicates email authorization codes, resume paths, recipient addresses, and message contents in local plaintext JSON files. <br>
Mitigation: Review before installing, prefer prompting for the authorization code at send time or using a secure secret store, and delete generated user and log configuration files after sending. <br>
Risk: The skill sends email through an SMTP script using user-provided recruiter addresses and attachments. <br>
Mitigation: Require the documented field-by-field self-check and explicit user confirmation before executing the send command. <br>


## Reference(s): <br>
- [163 Mail SMTP service](https://mail.163.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration files and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user confirmation before sending email; generated local configuration files may contain email credentials and resume paths.] <br>

## Skill Version(s): <br>
0.1.1 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
