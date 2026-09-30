## Description:

Helps agents manage Make workflows, connections, and resources through Maton-managed authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Make scenarios, connections, data stores, hooks, and related automation, with approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton access to the user's Make account may expose authorized account data.

Mitigation: Install only if Maton is trusted; prefer OAuth and avoid exposing API keys.

Risk: Writes and persistent automations can change resources or continue operating after the conversation.

Mitigation: Confirm each write or persistent automation with the user before execution.

Risk: Trigger destinations can continuously forward future event data.

Mitigation: Review and approve the trigger destination before enabling it.

## Reference(s):

- [Make skill on ClawHub](https://clawhub.ai/byungkyu/skills/make-api)
- [Maton](https://maton.ai)
- [Make API documentation](https://developers.make.com/api-documentation)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Make API operations use the user's authorized connection; writes require explicit approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
