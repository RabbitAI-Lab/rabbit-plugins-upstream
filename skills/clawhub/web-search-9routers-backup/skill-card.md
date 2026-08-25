## Description:

Fetches or reads a URL through a local 9Router backup web-fetch service when the primary 9router web-search skill fails or the user requests the backup fetch path.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch web content through a localhost 9Router backup service when the primary 9router web-search path is unavailable. It is intended for user-approved URLs and supports parameters for model selection, output format, and returned content length.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-approved URLs to a local 9Router service using an environment token.

Mitigation: Confirm the localhost:20128 service is expected, keep NINEROUTER_KEY in the environment, and avoid printing or hardcoding the token.

Risk: Fetching arbitrary internal or private-network URLs can create SSRF exposure.

Mitigation: Confirm untrusted URLs before fetching and avoid internal or private-network targets unless the user explicitly approves them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/web-search-9routers-backup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and fetched web content summaries or excerpts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local service at localhost:20128 and expects NINEROUTER_KEY to be supplied from the environment rather than hardcoded.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
