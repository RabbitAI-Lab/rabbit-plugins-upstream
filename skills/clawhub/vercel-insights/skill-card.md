## Description:

Reports a Vercel site's runtime error logs, failing requests, traffic, top pages, referrers, and Core Web Vitals through read-only queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anatoli-iliev](https://clawhub.ai/user/anatoli-iliev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and site operators use this skill to inspect a Vercel project's errors, runtime request logs, web analytics, and speed metrics without modifying the project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An account- or team-scoped Vercel read token can expose broad analytics, metrics, and request-log data.

Mitigation: Use the narrowest read scope that still answers the intended questions and prefer an environment or secrets-provider reference instead of storing the token in plaintext.

Risk: Request logs may contain customer data or secrets that the skill cannot generally redact.

Mitigation: Treat log output as sensitive and quote only the minimum needed to answer the user's question.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anatoli-iliev/skills/vercel-insights)
- [Project homepage](https://github.com/anatoli-iliev/openclaw-vercel-insights)
- [Vercel API notes](docs/api-notes.md)
- [CLI contract](docs/cli-contract.md)
- [OpenClaw setup guide](docs/openclaw-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown responses with CLI commands and human-readable tables; optional JSON or CSV from the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Vercel API queries; requires a Vercel token for live requests.]

## Skill Version(s):

1.1.1 (source: server release metadata, SKILL.md frontmatter, pyproject.toml, CHANGELOG released 2026-08-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
