## Description:

Fetches the user's saved Signatoro signature and appends it to emails the agent drafts or sends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[m-viable](https://clawhub.ai/user/m-viable)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams using an email-capable agent can add their saved Signatoro signature to drafts, replies, forwards, and sent messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Email actions contact Signatoro and may require access to a Signatoro API key.

Mitigation: Enable only if the user wants signatures on agent-handled email; keep the API key out of messages, files, and logs.

Risk: An email could use the wrong signature when multiple personal or agent identities are available.

Mitigation: Ask the user which signature to use when the intended identity is unclear.

## Reference(s):

- [Signatoro agent setup guide](https://signatoro.com/docs/install-signature/agent)
- [ClawHub skill listing](https://clawhub.ai/m-viable/skills/signatoro-email-signature)

## Skill Output:

**Output Type(s):** [Text, HTML]

**Output Format:** [Plain-text or HTML signature appended to an email body]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches the signature before each email action; sends without one and informs the user if unavailable.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
