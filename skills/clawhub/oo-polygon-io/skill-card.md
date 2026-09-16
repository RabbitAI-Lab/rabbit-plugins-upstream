## Description:

Massive (Polygon.io) (massive.com). Use this skill for Massive (Polygon.io) requests that search, retrieve, and read market reference and aggregate data through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to ask an agent for Polygon.io market data, including aggregate bars, previous-day bars, market status, ticker details, exchange listings, ticker type codes, and filtered ticker searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to run remote installer scripts for the oo CLI.

Mitigation: Verify that OOMOL and the oo CLI distribution path are trusted, and prefer a manual or signed installer with checksum verification before installation.

Risk: Polygon.io credentials are handled through the connected OOMOL account.

Mitigation: Connect the Polygon.io account only when OOMOL is an intended credential-handling intermediary.

## Reference(s):

- [Massive (Polygon.io) homepage](https://massive.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-polygon-io)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are read-only Polygon.io connector results returned through the oo CLI, with execution metadata when commands run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
