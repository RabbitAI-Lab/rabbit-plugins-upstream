## Description: <br>
Generate secure random strings, passwords, and cryptographic tokens using OpenSSL. Use when creating passwords, API keys, secrets, or any secure random data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[asleep123](https://clawhub.ai/user/asleep123) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to ask an agent for OpenSSL commands that generate passwords, API keys, session tokens, and other cryptographic random data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated passwords, API keys, and tokens are sensitive and can leak through logs, screenshots, or chat transcripts. <br>
Mitigation: Handle generated secrets as confidential and avoid storing or sharing them in transcripts or shared logs. <br>
Risk: The skill proposes local OpenSSL commands, and output depends on the local OpenSSL installation and shell pipeline behavior. <br>
Mitigation: Review commands before running them and use a trusted local OpenSSL installation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/asleep123/skills/openssl) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands assume local OpenSSL availability and generated secrets should be handled as sensitive.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
