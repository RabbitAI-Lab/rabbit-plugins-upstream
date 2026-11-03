## Description:

Provides an unofficial, typed Go client for the Latitude LLM ops API, with examples for authenticated requests and endpoint-specific response handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that calls the Latitude LLM API to inspect projects, traces, scores, and issues or perform authorized organization operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer API keys and OAuth tokens can expose organization data or enable privileged operations if leaked.

Mitigation: Load credentials from protected runtime configuration, never hardcode or log them, and send them only to the trusted API URL.

Risk: Trace contents and member information may be exposed through logs or exports.

Mitigation: Keep trace and member data out of logs, and confirm export recipients and scope before requesting emailed exports.

Risk: Organization-changing calls can create, modify, revoke, invite, or delete resources.

Mitigation: Perform these actions only when requested by the user and confirm the intended target and change.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-latitude-llm)
- [Source repository](https://github.com/psyb0t/go-latitude-llm)
- [ClawHub release](https://clawhub.ai/psyb0t/skills/go-latitude-llm)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Technical guidance]

**Output Format:** [Markdown with Go code examples and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and implementation guidance for the typed Go client.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
