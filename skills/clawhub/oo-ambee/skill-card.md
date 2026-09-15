## Description:

Use Ambee through an OOMOL-connected account to geocode locations and retrieve current, forecast, and historical air-quality data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Ambee location and air-quality data from an OOMOL-connected account without handling raw Ambee credentials directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup may lead users to run unverified remote installer scripts directly in a shell.

Mitigation: Review the installer source and prefer a verified, versioned, or package-managed oo CLI installation before first use.

## Reference(s):

- [Ambee homepage](https://www.getambee.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses include data and meta.executionId when commands run successfully.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
