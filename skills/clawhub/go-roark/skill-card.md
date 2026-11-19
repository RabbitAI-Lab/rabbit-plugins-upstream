## Description:

Unofficial Go client for the Roark voice AI agent testing and monitoring API. Package roark (github.com/psyb0t/go-roark), generated with oapi-codegen, has typed methods for agents, calls and transcripts, chats, simulations, run plans, personas, metrics, webhooks and projects, authenticated with a bearer key. Use when Go code needs Roark API access or already imports github.com/psyb0t/go-roark.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add Go code that connects to Roark for voice agent monitoring, testing, and project management. It guides setup, authentication, endpoint selection, and safe handling of responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was benign with medium confidence, but its analysis was partial because two references in SKILL.md were unresolved, leaving some evidence incomplete.

Mitigation: Review the skill's referenced material and decide whether it suits the project before installing.

Risk: Bearer credentials and call, transcript, or recording data may be sensitive, and write operations can change project resources or start processing.

Mitigation: Read ROARK_API_KEY from the environment, never hardcode or log it, return only necessary private data, and perform changes only when requested.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Project homepage](https://github.com/psyb0t/go-roark)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Go client code and setup guidance; API response content depends on the requested operation.]

## Skill Version(s):

0.20.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
