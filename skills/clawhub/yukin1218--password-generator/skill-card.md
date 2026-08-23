## Description: <br>
Generates a random 12- to 16-character password containing uppercase letters, lowercase letters, digits, and symbols. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[Yukin1218](https://clawhub.ai/user/Yukin1218) <br>

### License/Terms of Use: <br>


## Use Case: <br>
People using an agent can ask for a random password when they need a short generated credential. The skill runs a local script that prints the generated password and records it in a markdown memory file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated passwords are printed and saved in plaintext under the OpenClaw workspace memory directory. <br>
Mitigation: Use this only for low-sensitivity credentials, or modify the skill to avoid saving passwords unless explicitly requested and to use a trusted password manager for real account credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/Yukin1218/password-generator) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Console text plus a markdown entry in a password history file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated passwords are 12 to 16 characters long and include uppercase letters, lowercase letters, digits, and symbols.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
