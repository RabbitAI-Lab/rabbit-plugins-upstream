## Description: <br>
An interactive login helper for 动环综合网管 that recognizes image captchas, encrypts the password with RSA-OAEP-SHA256, triggers SMS 2FA, and saves a reusable session cookie. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[antarctic-penguin971](https://clawhub.ai/user/antarctic-penguin971) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to complete interactive login to a 动环综合网管 temperature and humidity monitoring platform, including captcha confirmation, SMS 2FA, and session cookie generation for scripts or scheduled tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles login passwords and reusable session cookies. <br>
Mitigation: Use it only in a trusted internal environment, avoid passing real passwords on the command line, and store cookies with 0600 permissions or a credential store. <br>
Risk: The login script bypasses TLS certificate verification for self-signed internal endpoints. <br>
Mitigation: Remove TLS bypass before broader use or pin the trusted server certificate. <br>
Risk: Temporary plaintext password material and example credentials could expose secrets. <br>
Mitigation: Prevent plaintext password temp files, restrict the working directory, and rotate any example credentials if they are real. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/antarctic-penguin971/skills/donguan-interactive-login) <br>
- [Publisher profile](https://clawhub.ai/user/antarctic-penguin971) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces an interactive login workflow and writes a reusable WEB_SESSION_ID_KEY cookie when login succeeds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
