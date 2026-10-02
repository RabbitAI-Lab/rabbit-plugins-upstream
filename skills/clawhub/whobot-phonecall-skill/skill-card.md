## Description:

Helps users discover WhoBot AI phone agents, try browser voice or outbound phone calls, and manage sign-in and identity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[whobot-ai](https://clawhub.ai/user/whobot-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users can explore WhoBot's showcase phone agents, try browser voice conversations or phone calls, and manage account sign-in, sign-out, and identity reset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: When the WhoBot CLI is missing, the skill directs the agent to fetch and run the latest npm release without asking first.

Mitigation: Require explicit approval before installation and pin the CLI to a reviewed version.

Risk: Trial calls and login can involve real phone numbers and verification codes.

Mitigation: Confirm the target number and obtain user consent before calls or code requests; do not expose verification codes.

## Reference(s):

- [WhoBot skill listing on ClawHub](https://clawhub.ai/whobot-ai/skills/whobot-phonecall-skill)
- [Product capabilities](artifact/references/product-capabilities.md)
- [Browser voice guidance](artifact/references/webrtc.md)
- [Phone trial guidance](artifact/references/trial-calls.md)
- [Authentication guidance](artifact/references/authentication.md)
- [Installation guidance](artifact/references/installation.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Links, Shell commands, Guidance]

**Output Format:** [Conversational text with links and occasional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report agent listings, call status, and sign-in status.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
