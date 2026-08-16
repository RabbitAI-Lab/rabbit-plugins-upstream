## Description:

Guides agents in using Mallary CLI, API, MCP, and workflows for read-only discovery, OAuth setup, and explicit user-authorized social media actions with credential and account-safety boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sammydigits](https://clawhub.ai/user/sammydigits)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and AI agents use this skill to inspect Mallary state, set up authentication, and carry out clearly requested social publishing or account-management workflows while minimizing sensitive data exposure.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mallary can publish content, upload media, send replies, and manage connected social accounts when a request is clear.

Mitigation: Use the skill only for explicit Mallary requests, resolve target profile, destinations, content, timing, and files before acting, and verify results with read-only commands.

Risk: OAuth and API credentials can authorize broad account access if exposed.

Mitigation: Keep OAuth tokens and API keys out of chat, logs, shell tracing, and transcripts; use browser OAuth or masked secret storage.

Risk: Discovery output can expose account identifiers, post metadata, analytics, settings, webhook destinations, or customer data.

Mitigation: Request only the data needed for the task and redact sensitive operational metadata before sharing outputs.

## Reference(s):

- [Mallary Openclaw Skill on ClawHub](https://clawhub.ai/sammydigits/skills/mallary)
- [Mallary Website](https://mallary.ai/)
- [Mallary Documentation](https://docs.mallary.ai)
- [Mallary CLI npm Package](https://www.npmjs.com/package/@mallary/cli)
- [Mallary Agent Repository](https://github.com/mallarylabs/mallary-agent)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes safety boundaries for Mallary account access, publishing, replies, uploads, settings, webhooks, and credential handling.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
