## Description: <br>
Proton Bridge Email helps agents send automated email through Proton Mail Bridge localhost SMTP using age-encrypted credentials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[boilerrat](https://clawhub.ai/user/boilerrat) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to configure Proton Mail Bridge credentials for an agent mailbox and send automated reports, alerts, or test messages through local SMTP. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill decrypts Proton Bridge mail credentials at runtime, so exposed age keys or temporary plaintext env files could disclose mailbox credentials. <br>
Mitigation: Protect the age identity file, keep encrypted secrets in restricted local storage, and delete temporary plaintext env files immediately after encryption. <br>
Risk: A configurable SMTP host with disabled TLS certificate checks could send mail through an unintended or untrusted SMTP endpoint. <br>
Mitigation: Keep SMTP_HOST set to localhost or 127.0.0.1 for Proton Bridge and review host, port, and security settings before use. <br>
Risk: Automated email sending can deliver messages to unintended recipients or send unreviewed content. <br>
Mitigation: Use confirmations or recipient allowlists for automated email workflows. <br>


## Reference(s): <br>
- [Proton Mail Bridge setup](references/proton-bridge-setup.md) <br>
- [Proton Mail Bridge](https://proton.me/mail/bridge) <br>
- [ClawHub release page](https://clawhub.ai/boilerrat/skills/protom-bridge-email) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and Python script usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces email-sending guidance and command examples; the bundled scripts can encrypt local configuration and send messages through Proton Bridge.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
