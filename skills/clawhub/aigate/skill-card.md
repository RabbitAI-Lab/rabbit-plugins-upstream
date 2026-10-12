## Description:

Guides developers in deploying and using a self-hosted AI gateway that combines model inference and optional tools behind one OpenAI-compatible endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up a self-hosted AI gateway and connect agents to enabled models and tools through a single endpoint. Optional integrations include browser automation, code execution, messaging, storage, and media services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: One bearer token can grant an agent access to many powerful services.

Mitigation: Use separate per-service tokens and give agents only the access needed for a specific task.

Risk: Exposing the gateway can allow unauthorized control of sensitive capabilities.

Mitigation: Keep it off the public internet unless protected by strong authentication.

Risk: Enabled email, Telegram, browser, code execution, and storage tools can act on a user's behalf or affect their data.

Mitigation: Enable only necessary services and review agent actions before granting access.

## Reference(s):

- [aigate on ClawHub](https://clawhub.ai/psyb0t/skills/aigate)
- [aigate setup guide](artifact/references/setup.md)
- [Project homepage (listed in skill)](https://github.com/psyb0t/aigate)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell and API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance depends on which services the operator enables.]

## Skill Version(s):

10.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
