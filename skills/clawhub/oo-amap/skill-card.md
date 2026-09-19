## Description:

AMap (amap.com) enables agents to search and read AMap data through OOMOL's `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to perform AMap place search, geocoding, reverse geocoding, route planning, IP location, district lookup, place detail, and weather requests through an OOMOL-connected AMap account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of remote installer scripts.

Mitigation: Install the oo CLI only from a verified, versioned source with signature or checksum validation; do not let an agent run curl-to-bash or irm-to-iex installer commands automatically.

Risk: AMap access depends on a connected OOMOL account and server-side credential handling.

Mitigation: Confirm the user has already installed, signed in, and connected AMap before running connector actions; use setup steps only after an authentication or connection failure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-amap)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [AMap homepage](https://www.amap.com)
- [OOMOL app connection console](https://console.oomol.com/app-connections?provider=amap)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live `oo connector schema` checks before constructing request payloads.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
