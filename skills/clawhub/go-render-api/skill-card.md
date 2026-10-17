## Description:

Guides Go developers in using an unofficial typed client for Render's public REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to write Go code that authenticates to the Render API, inspects services and deploys, handles paginated responses, and performs requested resource operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unofficial dependency receives access to a Render API key.

Mitigation: Review the dependency before installation, read the key from an environment variable, and never commit or log it.

Risk: Deploy, suspend, scale, update, or delete requests can affect live infrastructure.

Mitigation: Use only the intended Render account and explicitly named service IDs; perform changes only when requested.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/go-render-api)
- [Setup and reference](references/setup.md)
- [Go client project homepage](https://github.com/psyb0t/go-render-api)
- [Render API pagination documentation](https://api-docs.render.com/reference/pagination)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typed API responses and cursor-based pagination guidance]

## Skill Version(s):

0.1.3 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
