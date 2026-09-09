## Description:

Know exactly where your AI tokens go with multi-provider tracking, budget alerts, and a local REST API in one dashboard.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT

## Use Case:

Developers and operators use this skill to monitor Anthropic, OpenAI, Google Gemini, and Manus token or credit usage, set monthly budgets, and expose local budget status to agent workflows. It is intended for local, user-managed deployments where credentials, transcript parsing, provider environment reuse, and live probes are controlled by explicit user choices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review reports that fallback credential file handling can follow symlinks.

Mitigation: Use the OS keychain path whenever possible and avoid the plaintext fallback until the symlink-handling issue is fixed.

Risk: The local REST API exposes spend data through unauthenticated GET endpoints to callers that can reach the port.

Mitigation: Keep the API bound to 127.0.0.1 and do not expose port 8765 beyond the local machine.

Risk: Mutating API endpoints depend on the TOKEN_PANEL_API_TOKEN setting.

Mitigation: Set TOKEN_PANEL_API_TOKEN before enabling writes; leave it unset only when mutating endpoints should remain closed.

Risk: Transcript parsing, generic provider environment-variable reuse, and live provider probes expand local data access or may create billable provider requests.

Mitigation: Enable TOKEN_PANEL_READ_TRANSCRIPTS, TOKEN_PANEL_ALLOW_PROVIDER_ENV, or --probe only when those specific behaviors are intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/token-panel-ultimate)
- [TinkerClaw project repository](https://github.com/globalcaos/tinkerclaw)
- [Anthropic Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
- [Google Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Manus plans documentation](https://manus.im/docs/introduction/plans)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration]

**Output Format:** [Markdown guidance with shell command examples and local JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local budget summaries, alerts, and provider usage counts without storing prompts, message content, or task titles.]

## Skill Version(s):

2.6.1 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
