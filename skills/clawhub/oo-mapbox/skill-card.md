## Description:

Connects an agent to Mapbox geocoding, directions, and matrix actions through the OOMOL oo CLI with server-side credential handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run Mapbox connector actions for forward, reverse, and batch geocoding, route calculation, and travel time or distance matrices. It is intended for Mapbox tasks where OOMOL brokers credentialed requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The OOMOL CLI installation path uses remote installer scripts, which the security evidence flags as a disclosed installer safety caveat.

Mitigation: Before installing, review the OOMOL CLI installer source or use a safer official or package-manager installation path when available.

Risk: The skill brokers Mapbox requests through OOMOL-connected credentials.

Mitigation: Use it only for intended Mapbox connector tasks, and complete OOMOL sign-in or Mapbox connection setup only when the user intentionally wants OOMOL to broker those requests.

## Reference(s):

- [ClawHub Mapbox skill page](https://clawhub.ai/oomol/skills/oo-mapbox)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Mapbox homepage](https://www.mapbox.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, json]

**Output Format:** [Markdown guidance with inline shell commands and JSON action payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include a data object and meta.executionId when run with --json.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
