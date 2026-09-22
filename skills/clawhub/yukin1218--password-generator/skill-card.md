## Description:

Generates random 12-16 character passwords containing uppercase letters, lowercase letters, digits, and symbols when a user asks for a new or random password.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yukin1218](https://clawhub.ai/user/yukin1218)

### License/Terms of Use:


## Use Case:

External users and agent operators use this skill to generate a random password on request. The generated password is displayed to the user and saved to a local memory file.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated passwords are printed and appended in plaintext under the OpenClaw workspace memory directory.

Mitigation: Use only where plaintext password output and storage are acceptable; prefer an encrypted password manager or secret store for sensitive credentials.

Risk: The security evidence reports weak randomness for password generation.

Mitigation: Review before operational use and prefer a version that uses cryptographic randomness.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yukin1218/skills/password-generator)
- [Publisher profile](https://clawhub.ai/user/yukin1218)

## Skill Output:

**Output Type(s):** [text, markdown]

**Output Format:** [Plain text status output and a Markdown password entry]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Passwords are printed and appended to memory/passwords.md.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
