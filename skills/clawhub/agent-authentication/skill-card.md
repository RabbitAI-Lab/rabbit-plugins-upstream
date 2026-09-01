## Description:

Allows the AI agent to independently register, login, and authenticate using Firebase.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kingdestinythe1st](https://clawhub.ai/user/kingdestinythe1st)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent operators use this skill when an agent needs to create or access a Firebase-backed account, including registration, login, email verification, and password reset workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles account passwords and Firebase Auth ID tokens, so exposed credentials or tokens could enable account misuse.

Mitigation: Use dedicated agent credentials, avoid high-value personal passwords, and treat returned auth tokens as secrets.

Risk: The skill requires network access for Firebase-backed registration, login, verification, and password reset flows.

Mitigation: Install it only in environments where outbound authentication requests are expected and permitted.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown instructions with JSON tool schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The login workflow can return Firebase Auth ID tokens that must be treated as sensitive.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
