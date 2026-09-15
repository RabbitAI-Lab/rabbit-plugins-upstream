## Description:

SwaggerHub enables agents to search and read SwaggerHub APIs, domains, templates, and projects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and API teams use this skill to fetch SwaggerHub definitions, list versions, list projects and templates, and search registry content without handling raw SwaggerHub tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct remote installer execution for the oo CLI.

Mitigation: Review setup before installing and prefer a verified, pinned, or package-manager installation path.

Risk: SwaggerHub requests are routed through an OOMOL-connected account.

Mitigation: Confirm that OOMOL routing, account scopes, billing, and data handling fit the user's policies before use.

## Reference(s):

- [ClawHub SwaggerHub skill](https://clawhub.ai/oomol/skills/oo-swaggerhub)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [SwaggerHub homepage](https://swagger.io/tools/swaggerhub/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI with JSON payloads and server-side credential injection through OOMOL.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
