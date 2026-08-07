## Description:

Hilft Agenten, Musik in Audio-, Video- und Stream-Quellen mit AudD zu erkennen und AudD-Konto, Token, Kontingente, Streams und Planfragen sicher zu verwalten.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kikikari](https://clawhub.ai/user/kikikari)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to identify songs from audio clips, files, links, videos, live streams, DJ sets, podcasts, and radio sources. They also use it to manage AudD OAuth/API-token workflows, account usage, stream configuration, trial or paid plan limits, and quota-sensitive recognition jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to interact with a user's AudD account and handle sensitive API tokens.

Mitigation: Prefer OAuth with minimal scopes or an encrypted secret vault, avoid plaintext token storage unless the user accepts that risk, and never echo token values back to the conversation or files.

Risk: Recognition jobs, enterprise uploads, and stream monitoring can consume quota or create paid usage.

Mitigation: Estimate request usage before long files, batches, or new streams, check account status when available, and require confirmation before quota-heavy or paid actions.

Risk: Stream changes, payment-link creation, and token rotation can change account state or immediately invalidate existing integrations.

Mitigation: Require explicit user confirmation before stream-changing, billing-related, or token-rotation actions, and update known token storage locations after rotation.

Risk: Untrusted web, audio, video, or upload context could be paired with account tools in ways that trigger unsafe requests.

Mitigation: Treat external content as untrusted and keep confirmation enabled for sensitive AudD operations such as token reads, token rotation, paid actions, and stream changes.

## Reference(s):

- [AudD API Documentation](https://docs.audd.io/)
- [AudD MCP Server](https://docs.audd.io/mcp)
- [AudD Streams](https://docs.audd.io/streams)
- [AudD Enterprise](https://docs.audd.io/enterprise)
- [AudD SDKs](https://docs.audd.io/sdks)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with inline shell commands, API request examples, configuration steps, and concise recognition results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AudD account, quota, stream, token, and cost guidance; should avoid exposing secret token values.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
