## Description:

Zenscrape connector skill for fetching public URLs through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to inspect the live Zenscrape connector schema and fetch public web pages with optional rendering, proxy, header, and wait controls through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive or private URLs could expose target URLs and request details through the connector service.

Mitigation: Use the skill for public URLs by default, and avoid sensitive or private URLs unless that data flow is acceptable.

Risk: Connector authentication, connection scope, or billing state can block execution.

Mitigation: Run first-time setup, reconnection, or billing steps only after commands fail with the matching error.

Risk: Stale assumptions about connector inputs can cause malformed requests.

Mitigation: Inspect the live action schema before constructing each payload.

## Reference(s):

- [Zenscrape homepage](https://zenscrape.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect the live connector schema before running read-only Zenscrape fetch requests that return JSON data and execution metadata.]

## Skill Version(s):

1.0.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
