## Description:

Public, environment-independent status reporting skill that gathers user-provided tokens and identifiers at runtime, queries configured provider APIs, skips missing sources, and returns a daily report without exposing keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kikikari](https://clawhub.ai/user/kikikari)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate a daily, multi-provider status and usage report from configured services such as GitHub, Vercel, Docker Hub, OpenAI, Anthropic, Tailscale, and ClawHub. It is also useful as a pattern for extending status dashboards with additional provider loaders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses user-provided provider API tokens and identifiers, including admin or personal access tokens for some services.

Mitigation: Use least-privilege or read-only tokens where available, avoid production admin keys for browser use, and rotate credentials regularly.

Risk: Credentials may be stored in plaintext in browser localStorage or a local keys.env file.

Mitigation: Keep keys.env private and out of version control, avoid shared browsers for saved tokens, and prefer CI or scheduler secret stores for recurring automation.

Risk: Some browser-based provider API calls can fail because of CORS or authentication restrictions.

Mitigation: Treat those failures as unavailable data, and use a server-side scheduled task or CI workflow for providers that block browser requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kikikari/skills/tagesstatus-live-public)
- [README.md](artifact/README.md)
- [SKILL.md](artifact/SKILL.md)
- [keys.env.template](artifact/keys.env.template)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown status report with a TL;DR, provider sections, and an error log]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Skips sources with missing credentials or identifiers and should not print secrets.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
