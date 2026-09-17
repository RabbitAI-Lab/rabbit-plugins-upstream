## Description:

Radar enables agents to inspect Radar connector schemas and run Radar address and place actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform Radar address and place workflows, including autocomplete, geocoding, reverse geocoding, IP geocoding, and place search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask an agent to run remote installer scripts that change the local environment.

Mitigation: Install the oo CLI only from a trusted OOMOL distribution path, prefer manual verification or a signed/package-managed install, and do not let an agent run pipe-to-shell installers automatically.

Risk: Radar actions marked as write can change service state if run with an incorrect payload.

Mitigation: Fetch the live action schema first and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [Radar homepage](https://radar.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are returned as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
