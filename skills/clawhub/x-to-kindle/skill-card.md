## Description: <br>
Send X/Twitter posts to Kindle for distraction-free reading. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brianlu365ai](https://clawhub.ai/user/brianlu365ai) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
External users and developers use this skill to convert X/Twitter posts or threads into Kindle-readable documents and send selected local files to a configured Kindle email address. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can email arbitrary local files using configured SMTP credentials. <br>
Mitigation: Use it only with files or X/Twitter content explicitly selected for Kindle delivery, and review the file path and Kindle recipient before execution. <br>
Risk: SMTP app passwords can be exposed if stored in markdown files or other repository-visible configuration. <br>
Mitigation: Store SMTP credentials in protected environment secrets or a secret manager, and prefer a dedicated revocable sender account or app password. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/brianlu365ai/skills/x-to-kindle) <br>
- [fxtwitter status API example](https://api.fxtwitter.com/status/1234567890) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline code and shell commands; generated Kindle-readable HTML files and SMTP delivery confirmations when executed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided SMTP credentials and Kindle email configuration.] <br>

## Skill Version(s): <br>
0.1.1 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
