## Description:

Provides a backup URL fetch and read workflow through the local 9Router service when the primary web-search skill fails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch or read a URL with a backup 9Router web-fetch service when the primary web-search skill is unavailable or fails.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials can be exposed if NINEROUTER_KEY is hardcoded, logged, or copied into command output.

Mitigation: Keep NINEROUTER_KEY in the environment and redact secrets from logs, commands, and responses.

Risk: Fetching untrusted or internal-sensitive URLs can create SSRF-style exposure.

Mitigation: Confirm URLs before fetching and avoid internal-sensitive targets unless the user explicitly intends that access.

Risk: The backup fetch service may be unavailable or return authorization errors.

Mitigation: Report service or token failures clearly and fall back to the primary web-search skill or ask the user to refresh credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/web-search-9routers-backup)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and fetched content returned as HTML or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the NINEROUTER_KEY environment variable for authorization and supports HTML or text fetch output.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
