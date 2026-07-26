## Description: <br>
Generates local 12-16 character random passwords, evaluates password strength, and saves password history as Markdown. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individuals and developers use this skill to generate local random passwords for personal accounts, temporary credentials, and development or test environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated passwords are automatically saved locally in plaintext. <br>
Mitigation: Avoid generating real account passwords unless you know where memory/passwords.md is stored, disable history when possible, and delete the file when saved passwords are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/password-generator-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown instructions with Python and shell examples; generated passwords are shown as text and saved to memory/passwords.md.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally with Python 3.8+ and no API key; generated passwords may be written to a local plaintext history file.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
