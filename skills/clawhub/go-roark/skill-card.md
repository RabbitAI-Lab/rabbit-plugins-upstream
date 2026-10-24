## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Roark for voice-agent testing and monitoring, including calls, transcripts, simulations, metrics, and project operations. It provides typed-client usage guidance and examples for authenticated API requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials and call transcripts or recordings may be sensitive.

Mitigation: Prefer project-scoped API keys and protect transcripts and recordings.

Risk: The Go dependency is unofficial.

Mitigation: Review and pin the dependency before using it with sensitive data.

Risk: Live requests or changes to project data can have real effects.

Mitigation: Explicitly request live operations or resource changes, and check API responses before relying on results.

## Reference(s):

- [Go Roark source repository](https://github.com/psyb0t/go-roark)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Roark API](https://api.roark.ai)
- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with Go code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usage examples and integration guidance; does not itself perform live API operations.]

## Skill Version(s):

0.2.0 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
