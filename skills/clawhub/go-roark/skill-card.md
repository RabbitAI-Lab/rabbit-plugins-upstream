## Description:

An unofficial Go client for Roark's voice AI testing and monitoring API, with typed operations for agents, calls, chats, simulations, metrics, and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Go applications with Roark for call and chat monitoring, transcript access, simulations, metrics, and project management. Use project-changing operations only when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial because two referenced paths could not be matched to bundled files; its benign verdict and lack of findings are not a guarantee.

Mitigation: Check the referenced files and keep credentials out of source code, logs, and returned output.

Risk: Calls, transcripts, recordings, and credentials may contain private data, and write operations can affect the Roark project.

Mitigation: Return only the data needed for the task and perform project-changing operations only when the user requested them.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-roark)
- [Declared project homepage](https://github.com/psyb0t/go-roark)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-roark)

## Skill Output:

**Output Type(s):** [Code, API Calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for Go applications using a Roark bearer credential from ROARK_API_KEY.]

## Skill Version(s):

0.21.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
