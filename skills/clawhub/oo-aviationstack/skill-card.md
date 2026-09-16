## Description:

Aviationstack lets agents search and read Aviationstack flight, route, and aviation reference data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query Aviationstack data through an OOMOL-connected account, including real-time or recent historical flights, airline routes, and aviation reference datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can lead an agent to execute unverified remote installer scripts directly in a shell.

Mitigation: Install the oo CLI manually from a trusted source and prefer a pinned release or verification step before allowing the skill to run Aviationstack queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-aviationstack)
- [Aviationstack homepage](https://aviationstack.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live oo connector schema before submitting action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
