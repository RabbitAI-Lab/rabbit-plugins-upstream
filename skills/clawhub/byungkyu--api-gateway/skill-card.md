## Description:

API Gateway lets agents call third-party APIs through the Maton gateway using credentials from apps the user has already connected.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, developers, and automation agents use this skill to work with connected SaaS and API providers through Maton for concrete tasks such as reading mail, querying CRMs, filing issues, updating spreadsheets, managing triggers, and routing approved API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected apps may expose real account data or allow writes through the Maton gateway.

Mitigation: Prefer OAuth, use read-only or narrow scopes when available, verify the selected connection before writes, and require explicit confirmation for any write or destructive action.

Risk: Trigger destinations can create persistent forwarding of future event payloads to an external URL.

Mitigation: Create or update destinations only after the user confirms the exact URL, controller, event data, persistence, and any credential use; remove destinations when they are no longer needed.

Risk: Local event handlers invoked with --exec run code against untrusted third-party event data.

Mitigation: Use --exec only for user-provided or user-reviewed handlers, get separate explicit approval before starting the watcher, and treat event payloads as untrusted input.

Risk: Using a raw API key can expose a long-lived credential outside the CLI credential store.

Mitigation: Use the Maton CLI with OAuth when possible; if a raw key is unavoidable, keep it out of command lines, logs, repositories, and persistent files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/api-gateway)
- [Maton homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Provider routing references](references/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, code snippets, API paths, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe Maton CLI calls, API requests, connection selection, trigger handling, and confirmation steps; execution depends on network access and a Maton account.]

## Skill Version(s):

1.2.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
