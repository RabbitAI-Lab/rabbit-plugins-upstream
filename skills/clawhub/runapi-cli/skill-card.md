## Description:

Install and use the RunAPI CLI for one-off artifacts and results from registered CLI-backed services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to discover supported RunAPI CLI services, compose JSON-first service requests, run or wait for tasks, manage uploads and files, and handle authentication safely for one-off terminal workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI credentials, callback listener secrets, uploaded files, and cross-agent skill installation commands are sensitive user-approved actions.

Mitigation: Prefer environment credentials or stdin token import, avoid exposing secrets in process arguments or project config, and keep listener secrets out of logs.

Risk: Service commands, actions, flags, or request fields can drift from the installed CLI catalog.

Mitigation: Inspect `runapi --help`, service help, and action help before composing requests, then update the CLI if documented behavior is unavailable.

Risk: Generated file URLs are temporary and may not satisfy durable artifact requirements.

Mitigation: Download every requested URL, verify a non-empty file and expected MIME type, and move generated assets into durable storage within the documented retention window.

Risk: The headless installer executes a remote installation script.

Mitigation: Prefer the Homebrew install path when available; if headless installation is needed, run it only from a trusted network and account and consider inspecting or verifying the installer first.

## Reference(s):

- [RunAPI model and CLI service catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-cli)
- [RunAPI publisher profile](https://clawhub.ai/user/runapi-ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance emphasizes inspecting installed CLI help before composing service commands and preserving generated artifacts outside temporary URLs.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
