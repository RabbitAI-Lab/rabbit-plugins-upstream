## Description:

Fetches or reads a URL through a local 9Router backup web fetch service when the primary web search skill fails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill as a fallback URL fetch workflow when primary web search fails. It provides guidance for calling a local 9Router fetch endpoint, supplying request parameters, and handling common service or authorization errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bearer tokens could be exposed if pasted directly into commands or chat.

Mitigation: Keep NINEROUTER_KEY in the environment and use environment-variable references in generated commands.

Risk: Fetching arbitrary user-provided URLs can target private or internal systems.

Mitigation: Confirm any URL before fetching when it could resolve to a private, internal, or otherwise sensitive destination.

Risk: The local 9Router backup service may be unavailable or reject requests with expired credentials.

Mitigation: Report connection failures clearly, suggest the primary search skill as a fallback, and ask the user to refresh NINEROUTER_KEY for authorization failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/web-search-9routers-backup)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include URL fetch parameters, token-handling guidance, and error-handling recommendations.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
