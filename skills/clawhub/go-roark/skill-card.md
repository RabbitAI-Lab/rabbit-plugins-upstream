## Description:

Guides Go developers in using the unofficial, typed go-roark client to access Roark's voice AI testing and monitoring API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to write Go code that accesses the Roark voice AI testing and monitoring API, including agents, calls, chats, simulations, metrics and project resources. It guides authentication, operation selection, pagination and response handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reported no findings but was partial because two references in SKILL.md could not be resolved.

Mitigation: Review the referenced materials if available before installing, as advised by the security review.

Risk: Roark calls and transcripts may contain private data, and some API operations create, delete or modify project resources or start simulations.

Mitigation: Use credentials from ROARK_API_KEY without hardcoding, committing or logging them; return only needed data and perform consequential operations only when requested.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code, shell commands and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Go project context and a ROARK_API_KEY bearer credential may be required.]

## Skill Version(s):

0.16.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
